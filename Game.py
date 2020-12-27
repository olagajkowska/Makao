from Hand import Hand
from Deck import Deck
from Stack import Stack
from Rulebook import Rulebook

debug = True


class Game:
    __slots__ = ['__deck', '__stack', '__player', '__rulebook', '__empty_deck']

    def __init__(self, N_Players=4, N_Decks=1):
        self.__deck = Deck(N_Decks)
        self.__stack = Stack()
        self.__player = []
        self.__rulebook = Rulebook()
        self.__empty_deck = False

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

        while not any(len(hand.content) == 0 for hand in self.__player):
            self.__round()
            if self.__empty_deck:
                break
            for j in range(N_Players):
                print("Player " + str(j + 1))
                print(self.__player[i])
            print('updated stack:\n', self.__stack, '\n')

        print("End of the game")

    def __start(self):
        for i in range(5):
            for player in self.__player:
                player.draw(self.__deck)

        while not self.__stack.valid:
            card = self.__deck.get_top
            self.__deck.remove(card.id)
            self.__stack.add(card)
            self.__stack.check_top()

        for player in self.__player:
            player.sort_hand()

    def __round(self):
        for hand in self.__player:
            ok_cards = self.__rulebook.check(hand.content, self.__stack.content[-1], [])
            if len(ok_cards) == 0:
                if len(self.__deck.content) == 0:
                    self.__empty_deck = True
                    print("Deck is empty!")
                    return
                else:
                    print('card: -\n')
                    hand.draw(self.__deck)
                    continue

            hand.play_card(ok_cards, self.__stack)
