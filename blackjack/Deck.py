import random
from blackjack.cards import Card
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
class deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def __str__(self):
        deck_comp=''
        for Card in self.all_cards:
            deck_comp += '\n'+Card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        single_card=self.all_cards.pop()
        return single_card 

# mydeck=deck()
# mydeck.shuffle()
# mydeck.deal_one()
# print(mydeck.deal_one())