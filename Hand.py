from Base_container import Base_container
from collections import Counter


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

    def play_card(self, ok_card, stack):
        self.remove(ok_card.id)  # tutaj strategia powinna wybrać odpowiednią kartę z ok_cards
        stack.add(ok_card)
        print('card: ', ok_card, '\n')

    def renumber(self,cards):
        for new_id, card in enumerate(self.content):
            card.set_id(new_id)
            new_id += 1

    def draw(self, deck):
        card = deck.get_top
        deck.remove(card.id)
        self.add(card)

    def strategy(self, cards, hand):
        karty = []
        karty.append(cards[0])
        if len(cards)>1:
            for item in hand:
                if item.value == karty[0].value and item.id != karty[0].id:
                    karty.append(item)
        #karty.reverse()
        special = []

        for item in karty:
            special.append(0)

        for k, item in enumerate(karty):
            if item.value == '2':
                special[k]=2
            elif item.value == '3':
                special[k]=3
            elif item.value == '4':
                special[k]=4
            elif item.value == 'J':
                if len(hand)>1:
                    val_list=[]
                    n=0
                    for item in hand:
                        val_list.append(item.value)
                    z=Counter(val_list)
                    for val in ['5', '6', '7', '8', '9', '10']:
                        if z[val] > n:
                            special[k] = val
                            n = z[val]
                    if special[k] == 0:
                        print("No requests!\n")
            elif item.value == 'K':
                if cards[0].suit in ["♥", "♠"]:
                    special[k]='K'
            elif item.value == 'A':
                if len(hand)>1:
                    suit_list=[]
                    n=0
                    for item in hand:
                        suit_list.append(item.suit)
                    z=Counter(suit_list)
                    for suit in ['♣', '♦', '♥', '♠']:
                        if z[suit] > n:
                            special[k] = suit
                            n = z[suit]
            
        return karty, special






