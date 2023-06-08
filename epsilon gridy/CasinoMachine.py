import numpy as np


class CasinoMachine:
    def __init__(self, success_rate: float):
        if success_rate < 0 or success_rate > 1:
            raise Exception(f'success rate is out of boundary, passed success rate = {success_rate}')

        self.__success_rate = success_rate

    def pull(self) -> float:
        return self.__success_rate + np.random.randn()

