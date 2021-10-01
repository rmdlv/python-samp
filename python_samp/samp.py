import pymem

from pymem import Pymem


class SAMP:
    def __init__(self) -> None:
        self.process = Pymem("gta_sa.exe")
        self.module = pymem.process.module_from_name(
            self.process.process_handle, "samp.dll"
        ).lpBaseOfDll
