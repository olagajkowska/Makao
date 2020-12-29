class Effect:

    def __init__(self):
        self.__effect = []

    def __call__(self, card):
        self.__fill_effect(card)

    def __str__(self):
        for item in self.__effect:
            print(item)
        return ''

    @property
    def effect(self):
        return self.__effect

    def __fill_effect(self, card):
        if card.value in ["2", "3", "4", "J", "Q", "A"]:
            self.__effect.append(card.value)
            return
        if card.value == "K":
            if card.suit in ["♥", "♠"]:
                self.__effect.append(card.value)
                return
        else:
            pass




