production = False
data_string = None

encoding = 'iso-8859-1'


class FileHandler:
    @staticmethod
    def open(p, **kwargs):
        if production:
            raise ValueError()
        return open(p, **kwargs)

    @staticmethod
    def set_production(data_str):
        global production, data_string
        production = True
        data_string = data_str



with FileHandler.open("..\\out\\copy.py") as f:
    print(f.read())
