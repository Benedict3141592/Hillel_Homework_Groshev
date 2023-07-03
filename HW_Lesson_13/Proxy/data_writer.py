class DataWriter:
    def __init__(self, data_path, data):
        self.__data_path = data_path
        self.__data = data

    def writer(self):
        with open(self.__data_path, "a") as database:
            database.write(f"\n{self.__data}")
