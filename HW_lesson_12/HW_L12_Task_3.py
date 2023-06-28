class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index > len(self.__sequence) or self.__end_index > len(self.__sequence) or \
                self.__end_index < self.__start_index:
            raise IndexError("Invalid data!")
        elif self.__start_index != self.__end_index:
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    my_list = CustomIterator([2, 4, 6, 8, 10, 12, 14], 2, 6)
    print(my_list.__next__())
    print(my_list.__next__())
    print(my_list.__next__())
    print(my_list.__next__())
    # print(my_list.__next__())
