from .memory_constants import (
    FUNC_SAMP_SENDSAY,
    FUNC_SAMP_SENDCMD,
    ADDR_POSITION_X,
    ADDR_POSITION_Y,
    ADDR_POSITION_Z,
    ADDR_SET_POSITION,
    ADDR_SET_POSITION_OFFSET,
    ADDR_SET_POSITION_X_OFFSET,
    ADDR_SET_POSITION_Y_OFFSET,
    ADDR_SET_POSITION_Z_OFFSET,
    SAMP_INFO_OFFSET,
    SAMP_PPOOLS_OFFSET,
    SAMP_PPOOL_PLAYER_OFFSET,
    SAMP_SLOCALPLAYERID_OFFSET,
    SAMP_SZLOCALPLAYERNAME_OFFSET,
    SAMP_ILOCALPLAYERSCORE_OFFSET,
    SAMP_ILOCALPLAYERPING_OFFSET,
    SAMP_PREMOTEPLAYER_OFFSET,
    SAMP_SZPLAYERNAME_OFFSET,
    SAMP_ISCORE_OFFSET,
    SAMP_IPING_OFFSET,
    SAMP_ISNPC_OFFSET,
    SAMP_FIRST_CHAT_MESSAGE_OFFSET,
    SAMP_CHAT_MESSAGE_SIZE,
    ADDR_SAMP_CHATMSG_PTR,
    ADDR_GTA_KEYS,
    ADDR_CAMERA_ROTATION,
)
from .samp_constants import SAMP_PLAYER_MAX, SAMP_MAX_CHAT_MESSAGES

from .samp import SAMP

from .objects import Player, Coordinates

from typing import List


class API:
    def __init__(self, samp: SAMP) -> None:
        self.samp = samp

    def send_chat(self, message: str, encoding: str = "utf8") -> None:
        address = self.samp.process.allocate(len(message))
        self.samp.process.write_bytes(address, message.encode(encoding), len(message))
        self.samp.process.start_thread(self.samp.module + FUNC_SAMP_SENDSAY, address)
        self.samp.process.free(address)

    def send_cmd(self, cmd: str, encoding: str = "utf8") -> None:
        address = self.samp.process.allocate(len(cmd))
        self.samp.process.write_bytes(address, cmd.encode(encoding), len(cmd))
        self.samp.process.start_thread(self.samp.module + FUNC_SAMP_SENDCMD, address)
        self.samp.process.free(address)

    def get_coordinates(self) -> Coordinates:
        x = self.samp.process.read_float(ADDR_POSITION_X)
        y = self.samp.process.read_float(ADDR_POSITION_Y)
        z = self.samp.process.read_float(ADDR_POSITION_Z)
        return Coordinates(x=x, y=y, z=z)

    def set_coordinates(self, x: float, y: float, z: float) -> None:
        address = self.samp.process.read_int(
            self.samp.process.read_int(ADDR_SET_POSITION) + ADDR_SET_POSITION_OFFSET
        )
        self.samp.process.write_float(address + ADDR_SET_POSITION_X_OFFSET, x)
        self.samp.process.write_float(address + ADDR_SET_POSITION_Y_OFFSET, y)
        self.samp.process.write_float(address + ADDR_SET_POSITION_Z_OFFSET, z)

    def get_local_scoreboard_data(self) -> Player:
        players = self._get_player_pool()
        id = self.samp.process.read_int(players + SAMP_SLOCALPLAYERID_OFFSET)
        name = self.samp.process.read_string(players + SAMP_SZLOCALPLAYERNAME_OFFSET)
        score = self.samp.process.read_int(players + SAMP_ILOCALPLAYERSCORE_OFFSET)
        ping = self.samp.process.read_int(players + SAMP_ILOCALPLAYERPING_OFFSET)
        return Player(id=id, name=name, score=score, ping=ping, npc=False)

    def get_remote_scoreboard_data(self) -> List[Player]:
        data = []
        players = self._get_player_pool()
        for id in range(SAMP_PLAYER_MAX):
            player = self.samp.process.read_int(
                players + SAMP_PREMOTEPLAYER_OFFSET + id * 4
            )
            if not player:
                continue
            name = self.samp.process.read_string(player + SAMP_SZPLAYERNAME_OFFSET)
            score = self.samp.process.read_int(player + SAMP_ISCORE_OFFSET)
            ping = self.samp.process.read_int(player + SAMP_IPING_OFFSET)
            npc = self.samp.process.read_bool(player + SAMP_ISNPC_OFFSET)
            data.append(Player(id=id, name=name, score=score, ping=ping, npc=npc))
        return data

    def _get_player_pool(self) -> int:
        address = self.samp.process.read_int(self.samp.module + SAMP_INFO_OFFSET)
        address = self.samp.process.read_int(address + SAMP_PPOOLS_OFFSET)
        pool = self.samp.process.read_int(address + SAMP_PPOOL_PLAYER_OFFSET)
        return pool

    def read_chat(self, line: int = 0, encoding: str = "utf8") -> str:
        address = self.samp.process.read_int(self.samp.module + ADDR_SAMP_CHATMSG_PTR)
        text = self.samp.process.read_bytes(
            address
            + SAMP_FIRST_CHAT_MESSAGE_OFFSET
            + (SAMP_MAX_CHAT_MESSAGES - line) * SAMP_CHAT_MESSAGE_SIZE,
            SAMP_CHAT_MESSAGE_SIZE,
        )
        return text.decode(encoding)

    def get_key_state(self, key: int) -> int:
        state = self.samp.process.read_int(ADDR_GTA_KEYS + key)
        return state

    def set_key_state(self, key: int, state: int) -> None:
        self.samp.process.write_int(ADDR_GTA_KEYS + key, state)

    def get_camera_rotation(self) -> float:
        angle = self.samp.process.read_float(ADDR_CAMERA_ROTATION)
        return angle * 90

    def set_camera_rotation(self, angle: float) -> None:
        self.samp.process.write_float(ADDR_CAMERA_ROTATION, angle / 90)
