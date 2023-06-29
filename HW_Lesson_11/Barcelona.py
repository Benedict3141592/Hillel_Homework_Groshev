from Hillel.HW_Lesson_11.I_game import IGame
from Hillel.HW_Lesson_11.I_team import ITeam
from random import sample, randrange
from time import sleep


# Inheritance
# Abstraction
class Barca(ITeam, IGame):
    def __init__(self, squad_power_gk: list, squad_power_cd: list, squad_power_cm: list, squad_power_fw: list,
                 stadium: str):
        super().__init__(squad_power_gk, squad_power_cd, squad_power_cm, squad_power_fw)
        # Hiding
        self.__power = 0
        self.__opponent_team = self.opponent_team()
        self.__opponent_power = self.opponent_power()
        self.__stadium = stadium

    # Encapsulation
    @property
    def stadium(self):
        return self.__stadium

    @stadium.setter
    def stadium(self, new_stadium):
        if isinstance(new_stadium, str):
            self.__stadium = new_stadium
        else:
            raise TypeError("Wrong format!")

    # Polymorphism
    def _check_gk(self):
        for players_power in self._squad_power_gk:
            if type(players_power) != int or players_power < 1 or players_power > 100:
                raise "Power of GK must be in range from 1 to 100"
        if len(self._squad_power_gk) < 1:
            raise "You must have at least one GK"

    def _check_cd(self):
        if len(self._squad_power_cd) < 4:
            raise "You must have at least four CD"
        for players_power in self._squad_power_cd:
            if type(players_power) != int or players_power < 1 or players_power > 100:
                raise "Power of CD must be in range from 1 to 100"

    def _check_cm(self):
        if len(self._squad_power_cm) < 4:
            raise "You must have at least four CM"
        for players_power in self._squad_power_cm:
            if type(players_power) != int or players_power < 1 or players_power > 100:
                raise "Power of CM must be in range from 1 to 100"

    def _check_fw(self):
        if len(self._squad_power_fw) < 2:
            raise "You must have at least two FW"
        for players_power in self._squad_power_fw:
            if type(players_power) != int or players_power < 1 or players_power > 100:
                raise "Power of FW must be in range from 1 to 100"

    def choose_best_eleven(self):
        self._check_gk()
        self._check_cd()
        self._check_cm()
        self._check_fw()
        self.__power += sum(sample(self._squad_power_gk, 1))
        self.__power += sum(sample(self._squad_power_cd, 4))
        self.__power += sum(sample(self._squad_power_cm, 4))
        self.__power += sum(sample(self._squad_power_fw, 2))

    def score(self):
        first_score = randrange(0, 2)
        second_score = randrange(3, 6)
        if self.__power > self.__opponent_power:
            print(f"Final score: {second_score} - {first_score}")
        elif self.__power == self.__opponent_power:
            print(f"Final score: {first_score} - {first_score}")
        else:
            print(f"Final score: {first_score} - {second_score}")

    def game(self):
        self.choose_best_eleven()
        print(f"Barca against {self.__opponent_team} at the stadium {self.__stadium}")
        sleep(2)
        if self.__power > self.__opponent_power:
            print(f"Barca team won the game. Barca power: {self.__power} and {self.__opponent_team} power: "
                  f"{self.__opponent_power}")
            sleep(1)
            self.score()
        elif self.__power == self.__opponent_power:
            print(f"Draw. Barca power: {self.__power} and {self.__opponent_team}: {self.__opponent_power} power:")
            sleep(2)
            self.score()
        else:
            print(
                f"{self.__opponent_team} team won the game. Barca power: {self.__power} and {self.__opponent_team} "
                f"power: "
                f"{self.__opponent_power}")
            sleep(1)
            self.score()


if __name__ == '__main__':
    team = Barca([66, 80, 90], [68, 85, 82, 87, 66, 78], [80, 88, 86, 82, 76, 69], [90, 83, 63, 78], "Olympic stadium")
    team.stadium = "Camp Nou"
    team.game()
