from Apple import Apple


class Asus(Apple):
    def __init__(self, model, screen_diagonal, screen_rate, cpu, gpu, ssd, ram, logo, operating_system):
        super().__init__(model, screen_diagonal, screen_rate, cpu, gpu, ssd, ram, logo)
        self._operating_system = operating_system
        self.__price = 0

    def __model_price(self):
        if self._model not in ["TUF Gaming", "Rog", "ProArt"]:
            raise TypeError("Error! Check your data and try again!")
        elif self._model == "TUF Gaming":
            self.__price += 200
        elif self._model == "Rog":
            self.__price += 250
        elif self._model == "ProArt":
            self.__price += 300

    def __screen_diagonal_price(self):
        if self._screen_diagonal not in [13.4, 15, 16]:
            raise TypeError("Error! Check your data and try again!")
        elif self._screen_diagonal == 13.4:
            self.__price += 50
        elif self._screen_diagonal == 15:
            self.__price += 100
        elif self._screen_diagonal == 16:
            self.__price += 175

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
        if self._cpu not in ["Ryzen 7", "Intel i7", "Ryzen 9", "Intel i9"]:
            raise TypeError("Error! Check your data and try again!")
        elif self._cpu == "Ryzen 7":
            self.__price += 50
        elif self._cpu == "Intel i7":
            self.__price += 100
        elif self._cpu == "Ryzen 9":
            self.__price += 150
        elif self._cpu == "Intel i9":
            self.__price += 200

    def __gpu_price(self):
        if self._gpu not in [8, 16, 32]:
            raise TypeError("Error! Check your data and try again!")
        elif self._gpu == 8:
            self.__price += 75
        elif self._gpu == 16:
            self.__price += 150
        elif self._gpu == 32:
            self.__price += 300

    def __ssd_price(self):
        if self._ssd not in [512, 1024, 2048, 4096]:
            raise TypeError("Error! Check your data and try again!")
        elif self._ssd == 512:
            self.__price += 45
        elif self._ssd == 1024:
            self.__price += 75
        elif self._ssd == 2048:
            self.__price += 105
        elif self._ssd == 4096:
            self.__price += 105

    def __ram_price(self):
        if self._ram not in [8, 16, 32, 64]:
            raise TypeError("Error! Check your data and try again!")
        elif self._ram == 8:
            self.__price += 20
        elif self._ram == 16:
            self.__price += 40
        elif self._ram == 32:
            self.__price += 60
        elif self._ram == 64:
            self.__price += 80

    def __add_logo(self):
        if self._logo not in [True, False]:
            raise TypeError("Error! Check your data and try again!")
        elif self._logo:
            self.__price += 15

    def __os_price(self):
        if self._operating_system not in ["DOS", "Windows 11"]:
            raise TypeError("Error! Check your data and try again!")
        elif self._operating_system == "Windows 11":
            self.__price += 35

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
        self.__os_price()
        return f"Your laptop will be cost: {self.__price} $\n"

    @staticmethod
    def help():
        print("Create your own notebook by entering the parameters from the following:\n"
              "Model: TUF Gaming, Rog, ProArt\n"
              "Screen diagonal: 13.4, 15, 16\n"
              "Screen rate: 60, 120, 144\n"
              "CPU: Ryzen 7, Intel i7, Ryzen 9, Intel i9\n"
              "GPU: 8, 16, 32\n"
              "SSD: 512, 1024, 2048, 4096\n"
              "RAM: 8, 16, 32, 64\n"
              "Add Logo: True or False\n"
              "Operating system: DOS, Windows 11\n")


if __name__ == '__main__':
    first = Asus("TUF Gaming", 15, 120, "Intel i7", 16, 2048, 32, False, "DOS")
    first.help()
    print(first.price)
