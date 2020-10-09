import random
from collections import deque
import os
import pathlib
import json
path = pathlib.Path()

PATH = os.path.dirname(os.path.abspath(__file__))
PLAYERDIR = path.cwd() / "players"

DECK = [("JOKER", "JOKER", "<:JOKER:763965286519930911>"),
        ("CLV", "A", "<:CLV_A:763965285782781962>"),
        ("CLV", "2", "<:CLV_2:763965285652758558>"),
        ("CLV", "3", "<:CLV_3:763965285626544138>"),
        ("CLV", "4", "<:CLV_4:763965285690114078>"),
        ("CLV", "5", "<:CLV_5:763965285640044604>"),
        ("CLV", "6", "<:CLV_6:763965285416960021>"),
        ("CLV", "7", "<:CLV_7:763965286105350204>"),
        ("CLV", "8", "<:CLV_8:763965285517885481>"),
        ("CLV", "9", "<:CLV_9:763965285661147156>"),
        ("CLV", "10", "<:CLV_10:763965285467947049>"),
        ("CLV", "J", "<:CLV_J:763965286121865227>"),
        ("CLV", "Q", "<:CLV_Q:763965286944473089>"),
        ("CLV", "K", "<:CLV_K:763965287082229760>"),
        ("DIA", "A", "<:DIA_A:763965285736513576>"),
        ("DIA", "2", "<:DIA_2:763965285740838912>"),
        ("DIA", "3", "<:DIA_3:763965285866143775>"),
        ("DIA", "4", "<:DIA_4:763965285711216672>"),
        ("DIA", "5", "<:DIA_5:763965285510152193>"),
        ("DIA", "6", "<:DIA_6:763965285883445248>"),
        ("DIA", "7", "<:DIA_7:763965285870075935>"),
        ("DIA", "8", "<:DIA_8:763965285941903380>"),
        ("DIA", "9", "<:DIA_9:763965285790515200>"),
        ("DIA", "10", "<:DIA_10:763965285807947836>"),
        ("DIA", "J", "<:DIA_J:763965287288537099>"),
        ("DIA", "Q", "<:DIA_Q:763965286868189204>"),
        ("DIA", "K", "<:DIA_K:763965287040811008>"),
        ("HRT", "A", "<:HRT_A:763965285803622440>"),
        ("HRT", "2", "<:HRT_2:763965285811355659>"),
        ("HRT", "3", "<:HRT_3:763965285824462858>"),
        ("HRT", "4", "<:HRT_4:763965285798510642>"),
        ("HRT", "5", "<:HRT_5:763965285833113670>"),
        ("HRT", "6", "<:HRT_6:763965285904285718>"),
        ("HRT", "7", "<:HRT_7:763965285848842290>"),
        ("HRT", "8", "<:HRT_8:763965285854085140>"),
        ("HRT", "9", "<:HRT_9:763965285581062166>"),
        ("HRT", "10", "<:HRT_10:763965285853560852>"),
        ("HRT", "J", "<:HRT_J:763965286532644874>"),
        ("HRT", "Q", "<:HRT_Q:763965287522893825>"),
        ("HRT", "K", "<:HRT_K:763965286679969822>"),
        ("SPD", "A", "<:SPD_A:763965286201163786>"),
        ("SPD", "2", "<:SPD_2:763965285999837229>"),
        ("SPD", "3", "<:SPD_3:763965285681594399>"),
        ("SPD", "4", "<:SPD_4:763965285966544906>"),
        ("SPD", "5", "<:SPD_5:763965285849497611>"),
        ("SPD", "6", "<:SPD_6:763965285631787009>"),
        ("SPD", "7", "<:SPD_7:763965286088310805>"),
        ("SPD", "8", "<:SPD_8:763965286055280680>"),
        ("SPD", "9", "<:SPD_9:763965286008487957>"),
        ("SPD", "10", "<:SPD_10:763965285899436033>"),
        ("SPD", "J", "<:SPD_J:763965435405271050>"),
        ("SPD", "Q", "<:SPD_Q:763965435934015489>"),
        ("SPD", "K", "<:SPD_K:763965436655566868>")]


class Card():
    def __init__(self, card):
        card = tuple(card)
        self.symbol = str(card[0])
        num = card[1]
        if num == "A":
            self.num = 1
        elif num == "J" or num == "Q" or num == "K":
            self.num = 10
        elif num == "JOKER":
            self.num = 0
        else:
            self.num = int(num)
        self.emoji = str(card[3])


class Trump:
    def __init__(self, contain_joker=False, doshufflefirst=True):
        self.deck = deque(DECK)
        if contain_joker:
            self.deck.appendleft(("JOKER", "JOKER"))
        if doshufflefirst:
            self.shuffle()

    def choice(self) -> tuple:
        return self.deck.popleft()

    def shuffle(self):
        random.shuffle(self.deck)


class Player():
    def __init__(self, userid: int):
        pdataformat = {
            "chip": 500,
            "game_total": 0,
            "game_win": 0
        }
        self.userid = userid
        playerdata = PLAYERDIR / f"{userid}.json"
        if not playerdata.exists():
            with open(playerdata, "w") as w:
                json.dump(pdataformat, w, ensure_ascii=False)
        with open(playerdata) as r:
            self.chip = int(r.read())
        self.cards = []

    def calc_hand(self):
        result = 0
        for c in self.cards:
            c = Card(c)
            result += c.num
        return result


class Dealer(Player):
    def __init__(self, userid):
        super().__init__(userid)
