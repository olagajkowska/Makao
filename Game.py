from Hand import Hand
from Deck import Deck
from Stack import Stack
from Rulebook import Rulebook
from Effect import Effect
from Card import Card

debug = True


class Game:
    __slots__ = ['__deck', '__stack', '__player', '__rulebook', '__empty_deck', '__active']

    def __init__(self, N_Players=8, N_Decks=1):
        self.__deck = Deck(N_Decks)
        self.__stack = Stack()
        self.__player = []
        self.__rulebook = Rulebook()
        self.__empty_deck = False
        self.__active = Card('8', '-')

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

        k=0
        draw=0
        wait=0
        while not any(len(hand.content) == 0 for hand in self.__player):
            k+=1
            print("* * * * * Round: ", k, " * * * * *\n")
            print('Stack:\n', self.__stack, '\n')   
            winner, wait = self.__round(draw, wait)

        print("End of the game")
        print("Player ",(winner)%N_Players+1, " wins in ", k, " turns!\n")

    def __start(self):
        for i in range(5):
            for player in self.__player:
                player.draw(self.__deck)

        while not self.__stack.valid:
            card = self.__deck.get_top
            self.__deck.remove(card.id)
            self.__stack.add(card)
            self.__stack.check_top()
            self.__activate(self.__stack.content[-1])

        for player in self.__player:
            player.sort_hand()

    def __round(self, draw, wait):
        win=0
        for count, hand in enumerate(self.__player):
            if win == 1:
                return count-1, wait
            print("* * * Player ", count+1, " * * *")
            if wait == 1:
                wait = 0
                print("Turn skipped!\n")
                continue
            print(self.__player[count])
            ok_cards = self.__rulebook.check(hand.content, self.__active, [], draw)
            if len(ok_cards) == 0:
                 draw=max(draw, 1)
                 print('card: Draw ' + str(draw) + '\n')                    
                 for i in range(draw):
                     if len(self.__deck.content) == 0:
                         if len(self.__stack.content) <5:
                            print("Too few cards! Dealing aditional deck of cards!")
                            self.__deck = Deck(1) 
                         else: 
                            print("Deck is empty!")
                            self.__restock()
                     hand.draw(self.__deck)
                 draw=0
                 continue

            to_play, special = hand.strategy(ok_cards, hand.content)
            for k, karta in enumerate(to_play):
                self.__activate(karta)
                hand.play_card(karta, self.__stack)  
                draw, wait, self.__active= Effect.efekt(special[k], draw, wait, self.__active)
                if len(hand.content)==1:
                    print("Player ", count+1, " says: MACAU!\n")  
                elif len(hand.content)==0:
                    win=1
                hand.renumber(hand.content)
        return count, wait


    def __restock(self):
                self.__deck.content = self.__stack.content
                self.__stack.content = []
                card = self.__deck.get_top
                self.__deck.remove(card.id)
                self.__stack.add(card)
                self.__deck.shuffle()

                if debug:
                    print(self.__deck)
                    print(self.__stack)

    def __activate(self, card):
        self.__active = Card(card.value, card.suit)
