from .memory import *


class API:
    def __init__(self, samp) -> None:
        self.samp = samp

    def getUsername(self):
        data = self.samp.process.read_string(self.samp.module + ADDR_SAMP_USERNAME)
        return data
