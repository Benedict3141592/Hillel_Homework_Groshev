from Dell import Dell


class Lenovo(Dell):
    def __init__(self, model: str, screen_diagonal: int or float, screen_rate: int, cpu: str, gpu: int, ssd: int,
                 ram: int, operating_system: str, discount: int):
        super().__init__(model, screen_diagonal, screen_rate, cpu, gpu, ssd, ram, operating_system)
        self.__price = 0
        self._discount = discount
        self._model_options = {"ThinkPad": 500, "Legion": 400}
        self._screen_diagonal_options = {15: 95, 15.6: 105, 16: 110}
        self._screen_rate_option = {120: 55, 144: 85}
        self._cpu_option = {"Ryzen 7": 50, "Intel i7": 65, "Ryzen 9": 150, "Intel i9": 155}
        self._gpu_option = {8: 75, 16: 100, 32: 250}
        self._ssd_option = {512: 55, 1024: 75, 2048: 105, 4096: 155}
        self._ram_option = {8: 20, 16: 40, 32: 80, 64: 160}
        self._operating_system_option = {"DOS": 0, "Windows": 45, "Linux": 0}
        self._discount_options = {0: 0, 10: 0.1, 15: 0.15}

    def __model_price(self):
        if self._model not in self._model_options.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._model_options.get(self._model)

    def __screen_diagonal_price(self):
        if self._screen_diagonal not in self._screen_diagonal_options.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._screen_diagonal_options.get(self._screen_diagonal)

    def __screen_rate_price(self):
        if self._screen_rate not in self._screen_rate_option.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._screen_rate_option.get(self._screen_rate)

    def __cpu_price(self):
        if self._cpu not in self._cpu_option.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._cpu_option.get(self._cpu)

    def __gpu_price(self):
        if self._gpu not in self._gpu_option.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._gpu_option.get(self._gpu)

    def __ssd_price(self):
        if self._ssd not in self._ssd_option.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._ssd_option.get(self._ssd)

    def __ram_price(self):
        if self._ram not in self._ram_option.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._ram_option.get(self._ram)

    def __os_price(self):
        if self._operating_system not in self._operating_system_option.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._operating_system_option.get(self._operating_system)

    def __discount(self):
        if self._discount not in self._discount_options.keys():
            raise TypeError("Error! Check your data and try again!")
        elif self._discount == 0:
            pass
        else:
            self.__price -= (self.__price * self._discount_options.get(self._discount))

    @property
    def price(self):
        self.__model_price()
        self.__screen_diagonal_price()
        self.__screen_rate_price()
        self.__cpu_price()
        self.__gpu_price()
        self.__ssd_price()
        self.__ram_price()
        self.__os_price()
        self.__discount()
        return f"Your laptop will be cost: {self.__price} $\n"

    @staticmethod
    def help():
        print("""Create your own notebook by entering the parameters from the following:
                  Model: Alienware, Precision, XPS
                  Screen diagonal: 15, 15.6, 16
                  Screen rate: 120, 144
                  CPU: Ryzen 7, Intel i7, Ryzen 9, Intel i9
                  GPU: 8, 16, 32
                  SSD: 512, 1024, 2048, 4096
                  RAM: 8, 16, 32, 64
                  Operating system: DOS, Windows, Linux\n""")


if __name__ == '__main__':
    first = Lenovo("ThinkPad", 16, 120, "Intel i9", 32, 2048, 64, "Windows", 10)
    first.help()
    print(first.price)
