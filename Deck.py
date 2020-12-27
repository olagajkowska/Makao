from Base_container import Base_container
from Card import Card
import random

debug = True


class Deck(Base_container):
    def __init__(self, N_Decks):
        super().__init__()
        self.__initiate(N_Decks)
        self.shuffle()

        # if debug:
        #     print(self)

        print("Deck ready!")

    def shuffle(self):
        for i in range(5):
            random.shuffle(self._Base_container__content)
        for i in range(self.length):
            self._Base_container__content[i].set_id(i)
        print("Deck is shuffled")

    @property
    def get_top(self):
        return self._Base_container__content[self.length - 1]

    def __initiate(self, N_Decks):
        i = 0
        for N in range(N_Decks):
            for col in Card.suit_list:
                for val in Card.rank:
                    c = Card(val, col)
                    self._Base_container__content.append(c)
                    self._Base_container__content[i].set_id(i)
                    i += 1

        print("Deck is full")
