from .memory import *
from .samp import SAMP


class API:
    def __init__(self, samp: SAMP) -> None:
        self.samp = samp

    def getUsername(self) -> str:
        username = self.samp.process.read_string(self.samp.module + ADDR_SAMP_USERNAME)
        return username

    def sendChat(self, message: str) -> None:
        address = self.samp.process.allocate(len(message))
        self.samp.process.write_string(address, message)
        self.samp.process.start_thread(self.samp.module + FUNC_SAMP_SENDSAY, address)
        self.samp.process.free(address)
