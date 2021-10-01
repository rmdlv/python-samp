from .memory import *
from .samp import SAMP


class API:
    def __init__(self, samp: SAMP) -> None:
        self.samp = samp

    def get_username(self) -> str:
        """
        Get local player username
        """
        username = self.samp.process.read_string(self.samp.module + ADDR_SAMP_USERNAME)
        return username

    def send_chat(self, message: str) -> None:
        """
        Send message to chat
        """
        address = self.samp.process.allocate(len(message))
        self.samp.process.write_string(address, message)
        self.samp.process.start_thread(self.samp.module + FUNC_SAMP_SENDSAY, address)
        self.samp.process.free(address)

    def send_cmd(self, cmd: str) -> None:
        """
        Send command to server
        """
        address = self.samp.process.allocate(len(cmd))
        self.samp.process.write_string(address, cmd)
        self.samp.process.start_thread(self.samp.module + FUNC_SAMP_SENDCMD, address)
        self.samp.process.free(address)

    def get_coordinates(self) -> float:
        """
        Get local player coordinates
        """
        x = self.samp.process.read_float(ADDR_POSITION_X)
        y = self.samp.process.read_float(ADDR_POSITION_Y)
        z = self.samp.process.read_float(ADDR_POSITION_Z)
        return x, y, z

    def set_coordinates(self, x: float, y: float, z: float) -> None:
        """
        Set local player coordninates
        """
        address = self.samp.process.read_int(
            self.samp.process.read_int(ADDR_SET_POSITION) + ADDR_SET_POSITION_OFFSET
        )
        self.samp.process.write_float(address + ADDR_SET_POSITION_X_OFFSET, x)
        self.samp.process.write_float(address + ADDR_SET_POSITION_Y_OFFSET, y)
        self.samp.process.write_float(address + ADDR_SET_POSITION_Z_OFFSET, z)
