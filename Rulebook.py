class Rulebook:

    def __init__(self):
        self.__rules = [Queen(), Ace(), Jack(), sameSuit(), sameValue()]

    def check(self, player_cards, top_card, effect):
        ok_cards = []

        for my_card in player_cards:
            for rule in self.__rules:
                if rule(top_card, my_card, effect):
                    ok_cards.append(my_card)
                    break
                elif rule.isThere == "J" or rule.isThere == "A":
                    rule.isThere = None
                    break

        return ok_cards



class Rules:

    def __init__(self):
        self.__isThere = None

    def __call__(self, top_card, ok_cards, effect):
        raise NotImplemented("to be implemented in by a derived class")

    @property
    def isThere(self): return self.__isThere

    @isThere.setter
    def isThere(self, there_is): self.__isThere = there_is


class sameSuit(Rules):
    def __init__(self):
        super().__init__()

    def __call__(self, top_card, my_card, effect):
        if len(effect) > 0 and top_card.value != 4:
            if my_card.value == "2" or my_card.value == "3":
                if my_card.suit == top_card.suit:
                    return True
            elif top_card.suit == "♠" or top_card.suit == "♥":
                if my_card.suit == top_card.suit and my_card.value == "K":
                    return True
        elif len(effect) == 0:
            if my_card.suit == top_card.suit:
                return True
        return False


class sameValue(Rules):
    def __init__(self):
        super().__init__()

    def __call__(self, top_card, my_card, effect):
        if my_card.value == top_card.value:
            return True
        return False


class Queen(Rules):
    def __init__(self):
        super().__init__()

    def __call__(self, top_card, my_card, effect):
        if (top_card.value == "Q" or my_card.value == "Q") and len(effect) == 0:
            return True
        return False

class Ace(Rules):
    def __init__(self):
        super().__init__()

    def __call__(self, top_card, my_card, effect):
        if top_card.value == "A":
            self.isThere = "A"
            if my_card.suit == effect[len(effect) - 1]:
                return True
            elif my_card.value == "A":
                return True
        return False

class Jack(Rules):
    def __init__(self):
        super().__init__()

    def __call__(self, top_card, my_card, effect):
        if top_card.value == "J":
            self.isThere = "J"
            if my_card.value == effect[len(effect) - 1]:
                return True
            elif my_card.value == "J":
                return True
        elif len(effect) > 0:
            if isinstance(effect[len(effect) - 1], str):
                self.isThere = "J"
                if my_card.value == effect[len(effect) - 1]:
                    return True
        return False
