import sys
import discord
import time
import datetime
from discord.ext import commands
import game
from game import *
import pathlib

PATH = pathlib.Path()
HOMEPATH = PATH.cwd()

PLAYERDIR = HOMEPATH / "players"

BlackJackBot = commands.Bot("!")


@BlackJackBot.command()
async def register(ctx):
    userid = ctx.author.id
    player = Player(userid)
    pass

BlackJackBot.run()
