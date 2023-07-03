class Oplot:
    def __init__(self):
        self.origin = "Ukraine"
        self.smoothbore_gun = "125 mm"
        self.rate_of_fire = "8 shots/min"
        self.dynamic_protection = True
        self.engine_power = "1200 hp"
        self.frontal_armour = "1100 mm"
        self.power_reserve = "400 km"
        self.maximum_speed = "70 km/h"
        self.transmission = "7 forward and 4 reverse gears"
        self.weight = "51 t"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"


if __name__ == '__main__':
    tank = Oplot()
    print(tank)
