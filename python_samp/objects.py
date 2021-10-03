from pydantic import BaseModel


class Player(BaseModel):
    id: int
    name: str
    score: int
    ping: int
    npc: bool
