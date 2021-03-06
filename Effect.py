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

    @staticmethod
    def efekt(special, draw, wait, card):
        if special == 2:
            draw = draw + 2
        elif special == 3:
            draw = draw + 3
        elif special == 4:
            wait = 1
        elif special in ['5', '6', '7', '8', '9', '10']:
            print("Requested cards: ", special, "\n")
            card.set_value(['J', special])
        elif special == 'K':
            draw = draw + 5
        elif special in ['♣', '♦', '♥', '♠']:
            print("Color changed to: ", special, "\n")
            card.set_suit([card.suit, special])
        return draw, wait, card




