from Samsung import Samsung


class Xiaomi(Samsung):
    def __init__(self, model: str, screen_diagonal: int or float, screen_rate: int, cpu: str, gpu: int, ssd: int,
                 ram: int, colour: str, fingerprint_scanner: bool):
        super().__init__(model, screen_diagonal, screen_rate, cpu, gpu, ssd, ram, colour)
        self._fingerprint_scanner = fingerprint_scanner
        self.__price = 0
        self._model_options = {"Redmi": 250, "RedmiBook": 150}
        self._screen_diagonal_options = {14: 85, 15.6: 95, 16: 110}
        self._screen_rate_option = {60: 35, 120: 55, 144: 85}
        self._cpu_option = {"Ryzen 7": 50, "Intel i7": 65, "Ryzen 9": 150, "Intel i9": 155}
        self._gpu_option = {8: 75, 16: 100, 32: 250}
        self._ssd_option = {512: 55, 1024: 75, 2048: 105, 4096: 155}
        self._ram_option = {8: 20, 16: 40, 32: 80, 64: 160}
        self._colour_option = {"Gold": 10, "White": 5, "Red": 5, "Black": 5}
        self._fingerprint_scanner_option = {True: 20, False: 0}

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

    def __colour_price(self):
        if self._colour not in self._colour_option.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._colour_option.get(self._colour)

    def __fingerprint_scanner_price(self):
        if self._fingerprint_scanner not in self._fingerprint_scanner_option.keys():
            raise TypeError("Error! Check your data and try again!")
        else:
            self.__price += self._fingerprint_scanner_option.get(self._fingerprint_scanner)

    @property
    def price(self):
        self.__model_price()
        self.__screen_diagonal_price()
        self.__screen_rate_price()
        self.__cpu_price()
        self.__gpu_price()
        self.__ssd_price()
        self.__ram_price()
        self.__colour_price()
        self.__fingerprint_scanner_price()
        return f"Your laptop will be cost: {self.__price} $\n"

    @staticmethod
    def help():
        print("""Create your own notebook by entering the parameters from the following:
                  Model: Galaxy, Notebook
                  Screen diagonal: 14, 15.6, 16
                  Screen rate: 60, 120, 144
                  CPU: Ryzen 7, Intel i7, Ryzen 9, Intel i9
                  GPU: 8, 16, 32
                  SSD: 512, 1024, 2048, 4096
                  RAM: 8, 16, 32, 64
                  Colour: Gold, White, Red, Black
                  Fingerprint scanner: True, False\n""")


if __name__ == '__main__':
    first = Xiaomi("Redmi", 14, 60, "Intel i7", 16, 1024, 8, "Gold", True)
    first.help()
    print(first.price)
