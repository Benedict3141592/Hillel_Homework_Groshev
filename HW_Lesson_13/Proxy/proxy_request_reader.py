from Hillel.HW_Lesson_13.Proxy.data_reader import DataProxyReader
from Hillel.HW_Lesson_13.Proxy.data_writer import DataWriter
from Hillel.HW_Lesson_13.Proxy.request_reader import RequestReader


class RequestProxyReader:
    def __init__(self, request_path, data_path):
        self.__current_request = RequestReader(request_path)
        self.__current_data = DataProxyReader(data_path)
        self.__writer = DataWriter(data_path, self.__current_request.read_request())

    def check_request_and_data(self):
        if self.__current_request.read_request() in self.__current_data.read_proxy_data():
            return self.__current_data.read_proxy_data()
        else:
            self.__writer.writer()
            return self.__current_data.read_proxy_data()


if __name__ == '__main__':
    request = RequestProxyReader("request.txt", "data.txt")
    data = request.check_request_and_data()
    print(data)
