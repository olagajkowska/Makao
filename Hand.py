from Base_container import Base_container


class Hand(Base_container):
    __slots__ = []

    def __init__(self):
        super().__init__()

    def __str__(self):
        for item in self.content:
            print(item)
        return ''

    def sort_hand(self):
        srt = {b: i for i, b in enumerate(['♣', '♦', '♥', '♠'])}
        self.content.sort(key=lambda x: x.value_rank)
        self.content.sort(key=lambda x: srt[x.suit[0]])
        new_id = 0
        for card in self.content:
            card.set_id(new_id)
            new_id += 1

    def play_card(self, ok_cards, stack):
        self.remove(ok_cards[0].id)  # tutaj strategia powinna wybrać odpowiednią kartę z ok_cards
        stack.add(ok_cards[0])
        new_id = 0
        for card in self.content:
            card.set_id(new_id)
            new_id += 1
        print('card: ', ok_cards[0], '\n')

    def draw(self, deck):
        card = deck.get_top
        deck.remove(card.id)
        self.add(card)






