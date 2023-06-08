from datetime import date


class Employee:
    def __init__(self, name: str, company: str, age: int, salary: int or float):
        self.name = name
        self._company = company
        self.__salary = salary
        self.__age = age

    def get_info(self):
        return f"{self.name} is working at {self._company}."

    def get_name(self):
        return self.name

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, new_company):
        if isinstance(new_company, str):
            self._company = new_company
        else:
            raise TypeError("Error! Wrong format!")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, int or float):
            self.__salary = new_salary
        else:
            raise TypeError("Wrong format")

    @classmethod
    def salary_with_bonus(cls, name: str, company: str, age: int, salary: int or float, bonus: int):
        salary_with_bonus = salary + bonus
        return cls(name, company, age, salary_with_bonus)

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def get_age(self, new_age):
        if type(new_age) == int and new_age >= 18 and new_age <= 70:
            self.__age = new_age
        else:
            print("Something went wrong! Try again late!")

    @classmethod
    def calculate_age(cls, name, company, year_of_birth, salary):
        return cls(name, company, date.today().year - year_of_birth, salary)


if __name__ == '__main__':
    Jack = Employee("Jack Sullivan", "Apple", 125000, 35)
    print(Jack.get_info())
    print(Jack.get_name())

    Jack.company = "Microsoft"
    print(Jack.company)

    Jack.salary = 124500
    print(Jack.salary)

    Jack.get_age = 36
    print(Jack.get_age)

    Marta = Employee.salary_with_bonus("Marta Keen", "Audi", 30, 125000, 20000)
    print(Marta.salary)

    John = Employee.calculate_age("John Snow", "BMW", 1995, 150000)
    print(John.get_age)
