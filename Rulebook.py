import copy
from Card import Card

class Rulebook:

    def __init__(self, N_players):
        self.__rules = [Jack(), Ace(), Queen(), sameSuit(), sameValue()]
        self.__num_players = N_players
        self.__count = N_players

    def check(self, player_cards, top_card, draw):
        ok_cards = []
        if isinstance(top_card.value, list):
            Rules.isThere = "J"
            Jack.tempCard = copy.deepcopy(top_card)
            top_card.set_value("J")
            self.__count = self.__num_players
            self.__count -= 1
        elif self.__count < self.__num_players and self.__count > 1:
            self.__count -= 1
            Rules.isThere = "J"
        elif self.__count == 1:
            Rules.isThere = "J"
            self.__count = self.__num_players

        for my_card in player_cards:
            for rule in self.__rules:
                if rule(top_card, my_card, draw):
                    ok_cards.append(my_card)
                    break
                elif rule.isThere == "J" or rule.isThere == "A":
                    if rule.isThere == "A":
                        rule.isThere = None
                    break

        if Rules.isThere == "J":
            Rules.isThere = None
        elif isinstance(top_card.suit, list):
            top_card.set_suit(top_card.suit[0])

        return ok_cards


class Rules:

    def __init__(self):
        self.__isThere = None

    def __call__(self, top_card, ok_cards, draw):
        raise NotImplemented("to be implemented in by a derived class")

    @property
    def isThere(self): return self.__isThere

    @isThere.setter
    def isThere(self, there_is): self.__isThere = there_is


class sameSuit(Rules):
    def __init__(self):
        super().__init__()

    def __call__(self, top_card, my_card, draw):
        if draw != 0:
            if my_card.value == "2" or my_card.value == "3":
                if my_card.suit == top_card.suit:
                    return True
            elif top_card.suit == "♠" or top_card.suit == "♥":
                if my_card.suit == top_card.suit and my_card.value == "K":
                    return True
        else:
            if my_card.suit == top_card.suit:
                return True
        return False


class sameValue(Rules):
    def __init__(self):
        super().__init__()

    def __call__(self, top_card, my_card, draw):
        if my_card.value in top_card.value:
            return True
        return False


class Queen(Rules):
    def __init__(self):
        super().__init__()

    def __call__(self, top_card, my_card, draw):
        if draw == 0:
            if (top_card.value == "Q" or my_card.value == "Q"):
                return True
        return False

class Ace(Rules):
    def __init__(self):
        super().__init__()

    def __call__(self, top_card, my_card, draw):
        if isinstance(top_card.suit, list):
            self.isThere == "A"
            if my_card.suit == top_card.suit[1] or my_card.value == "A":
                return True
        return False

class Jack(Rules):
    def __init__(self):
        super().__init__()
        self.__tempCard = Card("8","-")

    def __call__(self, top_card, my_card, draw):
        if self.isThere == "J":
            if my_card.value == self.tempCard.value[1]:
                return True
            elif top_card.value == "J" and my_card.value == "J":
                return True
        return False

    @property
    def tempCard(self): return self.__tempCard

    @tempCard.setter
    def tempCard(self, Card): self.__tempCard = Card
