debug = True

class Card:

    rank = {'2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
            }

    suit_list = ['♣', '♦', '♥', '♠']

    __slots__ = ['__value', '__suit', '__id', '__value_rank']

    def __init__(self, value, suit):
        self.__value = value
        self.__value_rank = self.rank[value]
        self.__suit = suit
        self.__id = -1

    def __str__(self):
        s = str(self.__value) + " " + str(self.__suit)
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
    def value_rank(self):
        return self.__value_rank

    @property
    def suit(self):
        return self.__suit

    def set_value(self, value): self.__value = value

    def set_suit(self, suit): self.__suit = suit

