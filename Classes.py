class Card:
    def __init__(self, color, number, action):
        self.c = color  # suite
        self.n = number  # number
        self.a = action # action

    def show(self):
        if self.n < 10 and self.n >= 0:
            print("{} of {}".format(self.n, self.s))
        if self.n == 11:
            print("{} of {}".format("Reverse", self.s))
        if self.n == 12:
            print("{} of {}".format("Skip", self.s))
        if self.n == 13:
            print("{} of {}".format("Draw 2", self.s))
        if self.n == 14:
            print("{} of {}".format("Wild", self.s))
        if self.n == 15:
            print("{} of {}".format("Wild Draw 4", self.s))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.discard = []

    def build(self):
        # Standard Numbers
        a = None
        for c in ["Red", "Yellow", "Green", "Blue"]:
            for n in range(0, 9):
                self.cards.append(Card(c, n, a))
        for c in ["Red", "Yellow", "Green", "Blue"]:
            for n in range(1, 9):
                self.cards.append(Card(c, n, a))

        for c in ["Red", "Yellow", "Green", "Blue"]:
            for n in range(1, 9):
                self.cards.append(Card(c, n, a))
        for c in ["Red", "Yellow", "Green", "Blue"]:
            for n in range(1, 9):
                self.cards.append(Card(c, n, a))
        # Action Cards

        for n in range(13,14):
            c = "Wild"
            self.cards.append(Card(c,n,))


    def show(self):
        for card in self.cards:
            card.show()

    def reshuffle_hands(self, player, dealer):
        self.discard.append(player.cards)
        self.discard.append(dealer.cards)
        player.cards = []
        print("emptying player cards")
        dealer.cards = []
        print("emptying dealer cards")
