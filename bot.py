import sys
import discord
import time
import datetime
import os
import game
from game import *

PATH = os.path.dirname(os.path.abspath(__file__))
with open(PATH + "/token.txt") as t:
    token = t.read()


class BlackJackBot(discord.Client):
    async def on_ready(self):
        pass

    async def on_message(self, message):
        if message.author == self.user:
            pass
        if message.content == "!bjstart":
            g = Game(message.author.id)
            g.start()


bot = BlackJackBot()

bot.run(token)
