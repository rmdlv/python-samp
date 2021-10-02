import time

from .memory_constants import (
    FUNC_CHEATS_JETPACK,
    ADDR_GAME_SPEED,
    ADDR_GAME_GRAVITY,
    ADDR_HUD_MONEY,
)

from . import SAMP, API


class Misc:
    def __init__(self, samp: SAMP) -> None:
        self.samp = samp
        self.api = API(self.samp)

    def get_jetpack(self) -> None:
        self.samp.process.start_thread(FUNC_CHEATS_JETPACK)

    def set_game_speed(self, speed: float) -> None:
        self.samp.process.write_float(ADDR_GAME_SPEED, speed)

    def get_game_speed(self) -> float:
        speed = self.samp.process.read_float(ADDR_GAME_SPEED)
        return speed

    def set_world_gravity(self, gravity: float) -> None:
        self.samp.process.write_float(ADDR_GAME_GRAVITY, gravity)

    def get_world_gravity(self) -> float:
        gravity = self.samp.process.read_float(ADDR_GAME_GRAVITY)
        return gravity

    def set_player_money(self, money: int) -> None:
        self.samp.process.write_int(ADDR_HUD_MONEY, money)

    def get_player_money(self) -> int:
        money = self.samp.process.read_int(ADDR_HUD_MONEY)
        return money

    def coordmaster(
        self, x: float, y: float, z: float, sections: int = 50, sleep: int = 0.25
    ) -> None:
        _x, _y, _z = self.api.get_coordinates()
        sx = (x - _x) / sections
        sy = (y - _y) / sections
        sz = (z - _z) / sections
        for _ in range(sections):
            _x += sx
            _y += sy
            _y += sz
            self.api.set_coordinates(_x, _y, _z)
            time.sleep(sleep)
