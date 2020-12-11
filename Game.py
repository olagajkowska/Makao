from Hand import Hand
from Deck import Deck
from Stack import Stack

debug = True


class Game:
    __slots__ = ['__deck', '__stack', '__player']

    def __init__(self, value_list, color_list, N_Players=4, N_Decks=1):
        self.__deck = Deck(value_list, color_list, N_Decks)
        self.__stack = Stack()
        self.__player = []
        for i in range(N_Players):
            hand = Hand()
            self.__player.append(hand)

        self.__start()

        if debug:
            print("deck: \n")
            print(self.__deck)
            print("stack: \n")
            print(self.__stack)
            print("players: \n")
            for i in range(N_Players):
                print("Player " + str(i + 1))
                print(self.__player[i])

    def __start(self):
        for i in range(5):
            for id in range(len(self.__player)):
                self.__draw(id)
        card = self.__deck.get_top
        self.__deck.remove(card.id)
        self.__stack.add(card)

    def __draw(self, i):
        card = self.__deck.get_top
        self.__deck.remove(card.id)
        self.__player[i].add(card.suit, card)
