class Base_dictionary:
    __slots__ = ['__dict_content']

    def __init__(self):
        self.__dict_content = {}

    def add_keys(self, list_of_keys):
        self.__dict_content = {key: [] for key in list_of_keys}
        return self.__dict_content

    def add(self, key, item):
        self.__dict_content[key].append(item)