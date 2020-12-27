class Base_container:
    __slots__ = ['__content']

    def __init__(self):
        self.__content = []

    def __str__(self):
        for item in self.__content:
            print(item)
        return "\n"

    def add(self, card):
        self.__content.append(card)
        id = len(self.__content) - 1
        self.__content[id].set_id(id)

    def remove(self, card_id):
        self.__content.pop(card_id)

    @property
    def length(self): return len(self.__content)

    @property
    def content(self):
        return self.__content
