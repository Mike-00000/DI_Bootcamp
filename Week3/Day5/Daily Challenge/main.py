import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

deck = Deck()
deck.shuffle()

print("Dealing 5 cards:")
for _ in range(5):
    card = deck.deal()
    if card:
        print(f"Card: {card.value} of {card.suit}")
    else:
        print("No more cards in the deck.")
