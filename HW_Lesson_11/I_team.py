from abc import ABC, abstractmethod


class ITeam(ABC):
    def __init__(self, squad_power_gk: list, squad_power_cd: list, squad_power_cm: list, squad_power_fw: list):
        self._squad_power_gk = squad_power_gk
        self._squad_power_cd = squad_power_cd
        self._squad_power_cm = squad_power_cm
        self._squad_power_fw = squad_power_fw

    @abstractmethod
    def _check_gk(self): ...

    @abstractmethod
    def _check_cd(self): ...

    @abstractmethod
    def _check_cm(self): ...

    @abstractmethod
    def _check_fw(self): ...

    @abstractmethod
    def choose_best_eleven(self): ...
