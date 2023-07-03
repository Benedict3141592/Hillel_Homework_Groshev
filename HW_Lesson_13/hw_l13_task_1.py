class FromDataAdapter:
    def __init__(self, file_path):
        self.file_path = file_path

    def convert_from_txt_to_html(self):
        with open(self.file_path) as file:
            lines = file.readlines()
        headers = lines[0].replace("\n", "")
        headers = headers.split(",")
        bodies = lines[1:]
        bodies = [item.replace("\n", "").split(",") for item in bodies]
        res = ""
        for bodies_item in bodies:
            for head, data in zip(headers, bodies_item):
                res += f"<{head}>{data}</{head}>\n"
        return res


if __name__ == '__main__':
    convert = FromDataAdapter("data.txt").convert_from_txt_to_html()
    print(convert)
