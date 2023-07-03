class DataProxyReader:
    def __init__(self, data_path):
        self.data_path = data_path

    def read_proxy_data(self):
        with open(self.data_path) as database:
            data = database.read()
        return data
