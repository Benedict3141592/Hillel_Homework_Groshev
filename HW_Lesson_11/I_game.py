from abc import ABC, abstractmethod
from random import randrange, sample


class IGame(ABC):

    @abstractmethod
    def game(self): ...

    @abstractmethod
    def score(self): ...

    @staticmethod
    def opponent_team():
        team = ["Hillel", "Ukraine", "Dynamo Kyiv", "Real Madrid", "Manchester City"]
        return "".join(sample(team, 1))

    @staticmethod
    def opponent_power():
        return randrange(500, 1100)
