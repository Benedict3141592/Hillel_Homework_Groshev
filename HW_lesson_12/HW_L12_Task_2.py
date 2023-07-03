class Train:
    def __init__(self):
        self.wagons = []
        self.locomotive = "HEAD"
        self.count = 1

    def add_wagon(self):
        self.wagons.append(self.count)
        self.count += 1

    def __len__(self):
        print("Count of wagons: ")
        return len(self.wagons)

    def __str__(self):
        res = f"<={self.locomotive}"
        for wagon in self.wagons:
            res += f"-{wagon}"
        return res
