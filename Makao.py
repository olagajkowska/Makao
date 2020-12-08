import random


class Card:
    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit
        self.__id = -1

    def __str__(self):
        s = self.__value + " " + self.__suit
        if debug == True:
            s += "\t Card ID = " + str(self.__id)
        return s

    def set_id(self, id):   self.__id = id

    @property
    def get_id(self): 
        if self.__id == -1:
            raise NotImplemented
        return self.__id

    @property
    def get_info(self): return (self.__value, self.__suit)
          

class Base_container:

    def __init__(self):
        self.__content = []

    def __str__(self):
        for item in self.__content:
            print(item)
        return "\n"

    def __add(self, card):
        self.__content.append(card)
        id = len(self.__content)-1
        self.__content[id].set_id(id)
        pass
    
    def __remove(self, card_id):
        self.__content.pop(card_id)
        pass

    @property
    def get_length(self): return len(self.__content)
    

class Deck(Base_container):
    def __init__(self, values, colors, N_Decks):
        super().__init__()
        self.__initiate(values, colors, N_Decks)
        self.shuffle

        if debug == True:   print(self)

        print("Deck ready!")
        pass

    @property
    def shuffle(self):
        for i in range(5):
            random.shuffle(self._Base_container__content)
        for i in range(self.get_length):
            self._Base_container__content[i].set_id(i)
        print("Deck is shuffled")

    @property
    def get_top(self): return self._Base_container__content[self.get_length-1]

    def __initiate(self, values, colors, N_Decks):
        i=0
        for N in range(N_Decks):
            for col in colors:
                for val in values:
                    c = Card(val, col)
                    self._Base_container__content.append(c)
                    self._Base_container__content[i].set_id(i)
                    i += 1

        print("Deck is full")



class Stack(Base_container):
    def __init__(self):
        super().__init__()
        pass    



class Hand(Base_container):
    def __init__(self):
        super().__init__()
        pass

    def __sort(self):
        
        pass


class rulebook:
    pass

class Game:

    def __init__(self, value_list, color_list, N_Players = 4, N_Decks = 1):
        #stworzenie obiektów początkowych
        self.__deck = Deck(value_list, color_list, N_Decks)
        self.__stack = Stack()
        self.__player = []
        for i in range(N_Players):
            hand = Hand()
            self.__player.append(hand)

        self.__start    #rozpoczęcie gry

        if debug == True:
            print("deck: \n")
            print(self.__deck)
            print("stack: \n")
            print(self.__stack)
            print("players: \n")
            for i in range(N_Players):
                print("Player " + str(i+1) )
                print(self.__player[i])


    @property
    def __start(self):
        for i in range(5):
            for id in range(len(self.__player)):
                self.__draw(id)
        card = self.__deck.get_top
        self.__deck._Base_container__remove(card.get_id)
        self.__stack._Base_container__add(card)



    def __draw(self, i):
        card = self.__deck.get_top
        self.__deck._Base_container__remove(card.get_id)
        self.__player[i]._Base_container__add(card)

debug = True

if __name__ == "__main__":
    value_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    color_list = ['♣', '♦', '♥', '♠']
    play = Game(value_list, color_list, N_Players = 2, N_Decks = 1)
