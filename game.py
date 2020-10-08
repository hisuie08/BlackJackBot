from gamelib import Trump, Card, Player


class Game():
    def __init__(self, playerid):
        self.dealer = Player(0)
        self.player = Player(playerid)
        self.deck = Trump()

    def start(self):
        pass
