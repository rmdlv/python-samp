from .memory import *
from .samp import SAMP


class Misc:
    def __init__(self, samp: SAMP) -> None:
        self.samp = samp

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
