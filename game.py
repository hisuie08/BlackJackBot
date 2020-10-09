from gamelib import Trump, Card, Player


class Game():
    def __init__(self, player: Player):
        self.player = player
        self.deck = Trump()

    def start(self):
        pass
