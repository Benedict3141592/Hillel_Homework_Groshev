from Hillel.HW_lesson_12.HW_L12_Task_2 import Train


class Wagon:
    def __init__(self, number: int):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def __len__(self):
        print("Count of passengers: ")
        return len(self.passengers)

    def __str__(self):
        return f"Wagon №: {self.number}. Passangers: {'. '.join(self.passengers)}"


if __name__ == '__main__':
    train = Train()

    wagon1 = Wagon(1)
    wagon2 = Wagon(2)
    wagon3 = Wagon(3)

    train.add_wagon()
    train.add_wagon()
    train.add_wagon()
    train.add_wagon()
    train.add_wagon()
    train.add_wagon()
    train.add_wagon()
    train.add_wagon()

    wagon1.add_passenger("Bill Gates")
    wagon1.add_passenger("Elon Musk")
    wagon1.add_passenger("jeffrey bezos")
    wagon2.add_passenger("Valerii Zaluzhnyi")
    wagon2.add_passenger("Volodymyr Zelenskyy")
    wagon3.add_passenger("Joe Byden")
    wagon3.add_passenger("Borys Johnson")

    print(len(wagon1))
    print(len(wagon2))
    print(len(wagon3))

    print(len(train))

    print(wagon1)
    print(wagon2)
    print(wagon3)

    print(train)
