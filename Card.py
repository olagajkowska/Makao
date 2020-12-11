debug = True

class Card:
    __slots__ = ['__value', '__suit', '__id']

    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit
        self.__id = -1

    def __str__(self):
        s = self.__value + " " + self.__suit
        # if debug:
        #     s += "\t Card ID = " + str(self.__id)
        return s

    def set_id(self, id):   self.__id = id

    @property
    def id(self):
        if self.__id == -1:
            raise NotImplemented
        return self.__id

    @property
    def value(self):
        return self.__value

    @property
    def suit(self):
        return self.__suit
