from Hand import Hand
from Deck import Deck
from Stack import Stack
from Rulebook import Rulebook
from Effect import Effect
from Card import Card

debug = True


class Game:
    __slots__ = ['__deck', '__stack', '__player', '__rulebook', '__empty_deck', '__active']

    def __init__(self, N_Players=4, N_Decks=1):
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
            print("* * * * * Round: " + str(k) + " * * * * *\n")
            print('Stack:\n', self.__stack, '\n')   
            winner, wait = self.__round(draw, wait)
            if self.__empty_deck:
                print("dealing aditional deck of cards!")
                self.__deck = Deck(N_Decks)


        print("End of the game")
        print("Player " + str((winner-1)%4+1) + " wins in " + str(k) + " turns!\n")

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
                return count, wait
            print("* * * Player " + str(count + 1)+" * * *")
            if wait == 1:
                wait = 0
                print("Turn skipped!\n")
                continue
            print(self.__player[count])
            ok_cards = self.__rulebook.check(hand.content, self.__active, [], draw)
            if len(ok_cards) == 0:
                if len(self.__deck.content) == 0:

                    print("Deck is empty!")
                    self.__restock()
                    if len(self.__deck.content) == 0:
                        self.__empty_deck = True
                    draw=max(draw, 1)
                    print('card: Draw ' + str(draw) + '\n')                    
                    for i in range(draw):
                        hand.draw(self.__deck)
                    draw=0
                    continue
                else:
                    draw=max(draw, 1)
                    print('card: Draw ' + str(draw) + '\n')                    
                    for i in range(draw):
                        hand.draw(self.__deck)
                    draw=0
                    continue

            to_play, special = hand.strategy(ok_cards)
            draw, wait = Effect.efekt(special, draw, wait)
            hand.play_card(to_play, self.__stack)
            self.__activate(to_play)            
            if len(hand.content)==0:
                win=1
            else:
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
