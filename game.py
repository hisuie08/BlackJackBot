from gamelib import Trump, Card, Player, Dealer


class Game():
    def __init__(self, myid: int, playerid: int):
        self.player = Player(playerid)
        self.dealer = Dealer(myid)
        self.deck = Trump()

    def start(self):
        d = self.player.read_data()
        chip = int(d["chip"])
        print(str(chip))
        self.first_deal()
        return

    def first_deal(self):
        self.player.hands.append(Card(self.deck.choice()))
        self.player.hands.append(Card(self.deck.choice()))
        while self.dealer.calc_sum() < 17:
            self.dealer.hands.append(Card(self.deck.choice()))

    def bet(self, player):
        return
