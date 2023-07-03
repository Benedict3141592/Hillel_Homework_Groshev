class RequestReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_request(self):
        with open(self.file_path) as file:
            text = file.read()
        return text
