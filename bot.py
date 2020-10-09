import sys
import discord
import time
import datetime
from discord.ext import commands
import game
from game import *
import pathlib
from functools import wraps

path = pathlib.Path()

TOKEN_FILE = path.cwd() / "token.txt"

with open(TOKEN_FILE, "r") as t:
    token = t.read()
