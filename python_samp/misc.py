import time
import math

from .memory_constants import (
    FUNC_CHEATS_JETPACK,
    ADDR_GAME_SPEED,
    ADDR_GAME_GRAVITY,
    ADDR_HUD_MONEY,
)
from .key_constants import ( KEY_W, KEY_A )

from .samp import SAMP
from .api import API


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

    def coord_master(
        self, x: float, y: float, z: float, sections: int = 50, sleep: int = 0.25
    ) -> None:
        coordinates = self.api.get_coordinates()
        _x, _y, _z = coordinates.x, coordinates.y, coordinates.z
        sx = (x - _x) / sections
        sy = (y - _y) / sections
        sz = (z - _z) / sections
        for _ in range(sections):
            _x += sx
            _y += sy
            _y += sz
            self.api.set_coordinates(_x, _y, _z)
            time.sleep(sleep)

    def walk_to_point(self, x: float, y: float, radius: int = 15) -> None:
        coordinates = self.api.get_coordinates()
        _x, _y = coordinates.x, coordinates.y
        dx = _x - x
        dy = _y - y
        dist = math.sqrt(dx * dx + dy * dy)
        while dist > radius:
            coordinates = self.api.get_coordinates()
            _x, _y = coordinates.x, coordinates.y
            dx = _x - x
            dy = _y - y
            dist = math.sqrt(dx * dx + dy * dy)
            dxa = abs(dx)
            beta = math.degrees(math.acos(dxa / dist))
            if dx > 0:
                if dy < 0:
                    angle = 270 + beta
                else:
                    angle = 270 - beta
            else:
                if dy < 0:
                    angle = 90 - beta
                else:
                    angle = 90 + beta
            self.api.set_camera_rotation(angle)
            self.api.set_key_state(KEY_A, -255)

    def walk_to_point_new(self, x: float, y: float, radius: int = 15) -> None:
        coordinates = self.api.get_coordinates()
        _x, _y = coordinates.x, coordinates.y
        dx = x - _x
        dy = y - _y
        dist = math.sqrt(dx * dx + dy * dy)
        a_b = dx*0 + dy*500
        angle = math.acos(a_b / (500 * dist)) * 180 / math.pi
        if dx < 0:
            angle *= -1

        while dist > radius:
            self.api.set_camera_rotation(1.5 * angle)
            self.api.set_key_state(KEY_W, 255)

            coordinates = self.api.get_coordinates()
            _x, _y = coordinates.x, coordinates.y
            dx = x - _x
            dy = y - _y
            dist = math.sqrt(dx * dx + dy * dy)
            a_b = dx*0 + dy*500
            angle = math.acos(a_b / (500 * dist)) * 180 / math.pi
            if dx < 0:
                angle *= -1