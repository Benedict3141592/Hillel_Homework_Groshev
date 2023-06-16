class Company:
    def __init__(self, company: str, address: str, number_of_employees: int, company_value: int or float,
                 company_pin: int):
        self.company = company
        self.address = address
        self.number_of_employees = number_of_employees
        self.__company_value = company_value
        self.__company_pin = company_pin

    @property
    def get_info(self):
        return (f"Company {self.company} is situated in {self.address}. "
                f"Currently number of employees is {self.number_of_employees} "
                f"and the company assets are {self.__company_value} billion USD.")

    @property
    def get_company(self):
        return self.company

    @property
    def get_address(self):
        return self.address

    @get_address.setter
    def get_address(self, new_address):
        if isinstance(self.address, str):
            self.address = new_address
        else:
            raise TypeError("Error! Wrong format!")

    @property
    def get_number_of_employee(self):
        return self.number_of_employees

    def change_number_employee(self, enter_pin, new_number):
        if type(new_number) != int:
            raise TypeError("Wrong format. Try again.")
        elif enter_pin == self.__company_pin:
            print("Pin code accepted")
            self.number_of_employees = new_number
        else:
            print("Wrong pin code")

    @property
    def get_company_value(self):
        return self.__company_value

    def add_company_value(self, enter_pin, add_value):
        if type(enter_pin) != int or type(add_value) != int:
            raise TypeError("Wrong format!")
        elif enter_pin == self.__company_pin:
            self.__company_value += add_value
        else:
            print("Wrong pin!")

    @staticmethod
    def help_pin():
        print("If you want to change pin code use function 'pin'")

    @property
    def pin(self):
        return self.__company_pin

    @pin.setter
    def pin(self, new_pin):
        if isinstance(new_pin, int) and len(str(new_pin)) == 3:
            self.__company_pin = new_pin
        else:
            raise TypeError("Error!")


if __name__ == '__main__':
    toshiba = Company("Toshiba", "Minato, Tokyo, Japan", 125648, 31800000000, 777)
    print(toshiba.get_company)
    print(toshiba.get_address)
    toshiba.get_address = "Tokyo"
    toshiba.change_number_employee(777, 125777)
    toshiba.add_company_value(777, 50000)
    print(toshiba.get_info)
    toshiba.help_pin()
    toshiba.pin = 888
    toshiba.add_company_value(888, 50000)

    apple = Company("Apple", "California, USA", 164000, 352.76, 888)
    print(apple.get_info)
