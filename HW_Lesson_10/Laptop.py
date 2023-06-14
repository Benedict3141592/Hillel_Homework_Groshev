from abc import ABC, abstractmethod


class Laptop(ABC):
    def __init__(self, model, screen_diagonal, screen_rate, cpu, gpu, ssd, ram):
        self._model = model
        self._screen_diagonal = screen_diagonal
        self._screen_rate = screen_rate
        self._cpu = cpu
        self._gpu = gpu
        self._ssd = ssd
        self._ram = ram

    @abstractmethod
    def price(self):
        pass
