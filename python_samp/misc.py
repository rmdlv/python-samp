import time

from .memory import *

from .samp import SAMP
from .api import API


class Misc:
    def __init__(self, samp: SAMP) -> None:
        self.samp = samp
        self.api = API(self.samp)

    def get_jetpack(self) -> None:
        """
        Give jetpack to local player
        """
        self.samp.process.start_thread(FUNC_CHEATS_JETPACK)

    def set_game_speed(self, speed: float) -> None:
        """
        Set local game speed
        """
        self.samp.process.write_float(ADDR_GAME_SPEED, speed)

    def get_game_speed(self) -> float:
        """
        Get local game speed
        """
        speed = self.samp.process.read_float(ADDR_GAME_SPEED)
        return speed

    def set_world_gravity(self, gravity: float) -> None:
        """
        Set local world gravity
        """
        self.samp.process.write_float(ADDR_GAME_GRAVITY, gravity)

    def get_world_gravity(self) -> float:
        """
        Get local world gravity
        """
        gravity = self.samp.process.read_float(ADDR_GAME_GRAVITY)
        return gravity

    def set_player_money(self, money: int) -> None:
        """
        Set local player money
        """
        self.samp.process.write_int(ADDR_HUD_MONEY, money)

    def get_player_money(self) -> int:
        """
        Get local player money
        """
        money = self.samp.process.read_int(ADDR_HUD_MONEY)
        return money

    def coordmaster(
        self, x: float, y: float, z: float, sections: int = 50, sleep: int = 0.25
    ) -> None:
        """
        Sectional teleport to coordniates
        """
        _x, _y, _z = self.api.get_coordinates()
        dx = (x - _x) / sections
        dy = (y - _y) / sections
        dz = (z - _z) / sections
        for _ in range(sections):
            _x += dx
            _y += dy
            _y += dz
            self.api.set_coordinates(_x, _y, _z)
            time.sleep(sleep)
