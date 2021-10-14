from pydantic import BaseModel


class Player(BaseModel):
    id: int
    name: str
    score: int
    ping: int
    npc: bool


class Coordinates(BaseModel):
    x: float
    y: float
    z: float
