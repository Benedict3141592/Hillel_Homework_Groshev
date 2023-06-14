from Laptop import Laptop


class Apple(Laptop):

    def __init__(self, model, screen_diagonal, screen_rate, cpu, gpu, ssd, ram, logo):
        super().__init__(model, screen_diagonal, screen_rate, cpu, gpu, ssd, ram)
        self._logo = logo
        self.__price = 0

    def __model_price(self):
        if self._model not in ["MacBook Air", "MacBook Pro", "iMac"]:
            raise TypeError("Error! Check your data and try again!")
        elif self._model == "MacBook Air":
            self.__price += 100
        elif self._model == "MacBook Pro":
            self.__price += 150
        elif self._model == "iMac":
            self.__price += 200

    def __screen_diagonal_price(self):
        if self._screen_diagonal not in [13.3, 13.6, 15.3, 16.2]:
            raise TypeError("Error! Check your data and try again!")
        elif self._screen_diagonal == 13.3:
            self.__price += 50
        elif self._screen_diagonal == 13.6:
            self.__price += 75
        elif self._screen_diagonal == 15.3:
            self.__price += 100
        elif self._screen_diagonal == 16.2:
            self.__price += 125

    def __screen_rate_price(self):
        if self._screen_rate not in [60, 120, 144]:
            raise TypeError("Error! Check your data and try again!")
        elif self._screen_rate == 60:
            self.__price += 35
        elif self._screen_rate == 120:
            self.__price += 55
        elif self._screen_rate == 144:
            self.__price += 75

    def __cpu_price(self):
        if self._cpu not in ["M1", "M2", "M2Pro", "M2Max"]:
            raise TypeError("Error! Check your data and try again!")
        elif self._cpu == "M1":
            self.__price += 50
        elif self._cpu == "M2":
            self.__price += 100
        elif self._cpu == "M2Pro":
            self.__price += 150
        elif self._cpu == "M2Max":
            self.__price += 200

    def __gpu_price(self):
        if self._gpu not in [8, 10, 38]:
            raise TypeError("Error! Check your data and try again!")
        elif self._gpu == 8:
            self.__price += 75
        elif self._gpu == 10:
            self.__price += 150
        elif self._gpu == 38:
            self.__price += 300

    def __ssd_price(self):
        if self._ssd not in [256, 512, 1024]:
            raise TypeError("Error! Check your data and try again!")
        elif self._ssd == 256:
            self.__price += 25
        elif self._ssd == 512:
            self.__price += 50
        elif self._ssd == 1024:
            self.__price += 75

    def __ram_price(self):
        if self._ram not in [4, 8, 16, 32]:
            raise TypeError("Error! Check your data and try again!")
        elif self._ram == 4:
            self.__price += 10
        elif self._ram == 8:
            self.__price += 20
        elif self._ram == 16:
            self.__price += 30
        elif self._ram == 32:
            self.__price += 40

    def __add_logo(self):
        if self._logo not in [True, False]:
            raise TypeError("Error! Check your data and try again!")
        elif self._logo:
            self.__price += 20

    @property
    def price(self):
        self.__model_price()
        self.__screen_diagonal_price()
        self.__screen_rate_price()
        self.__cpu_price()
        self.__gpu_price()
        self.__ssd_price()
        self.__ram_price()
        self.__add_logo()
        return f"Your laptop will be cost: {self.__price} $\n"

    @staticmethod
    def help():
        print("Create your own notebook by entering the parameters from the following:\n"
              "Model: MacBook Air, MacBook Pro, iMac\n"
              "Screen diagonal: 13.3, 13.6, 15.3, 16.2\n"
              "Screen rate: 60, 120, 144\n"
              "CPU: M1, M2, M2Pro, M2Max\n"
              "GPU: 8, 10, 38\n"
              "SSD: 256, 512, 1024\n"
              "RAM: 4, 8, 16, 32\n"
              "Add Logo: True or False\n")


if __name__ == '__main__':
    first = Apple("MacBook Air", 13.3, 60, "M1", 8, 256, 4, False)
    first.help()
    print(first.price)
    second = Apple("iMac", 16.2, 144, "M2Max", 38, 1024, 32, True)
    second.help()
    print(second.price)
