from Base_dictionary import Base_dictionary


class Hand(Base_dictionary):
    __slots__ = ['__hand']

    def __init__(self):
        super().__init__()
        self.__hand = self.add_keys(['♣', '♦', '♥', '♠'])

    def __str__(self):
        for key, cards in self.__hand.items():
            print(*cards)
        return ''
