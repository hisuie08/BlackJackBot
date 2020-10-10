import sys
import discord
import time
import datetime
import game
from game import *
import pathlib
from functools import wraps
from asyncio.exceptions import TimeoutError

path = pathlib.Path()

TOKEN_FILE = path.cwd() / "token.txt"

with open(TOKEN_FILE, "r") as t:
    token = t.read()

client = discord.Client()


@client.event
async def on_ready():
    print("run!")


@client.event
async def on_message(message):
    userid = message.author.id
    player = Player(userid)
    if message.content == "!register":
        if not player.registered:
            await message.channel.send(message.author.mention + "登録されていません。登録しますか？")

            def yes_or_no(m):
                return m.content == "y" and m.channel == message.channel and m.author == message.author
            try:
                msg = await client.wait_for("message", check=yes_or_no, timeout=20)
                player.register()
                await message.channel.send(f'{msg.author.mention}、登録しました\nチップ: {player.load_data()["chip"]}')
            except TimeoutError:
                await message.channel.send(f"{message.author.mention} タイムアウトしました")
        else:
            await message.channel.send(f"{message.author.mention} すでに登録済です")

    if message.content == "!bjstart":
        if player.registered:
            player.on_game = True
            print("start")
            game = Game(client.user.id, player.userid)
            game.start()
            for p in [game.dealer, game.player]:
                for c in p.hands:
                    print(c.symbol, c.num)
                print(str(p.calc_sum()))

            def action(m):
                return message.channel and m.author == message.author
            while player.on_game:
                try:
                    actionmsg = await client.wait_for("message", check=action, timeout=20)
                    if actionmsg.content == "h":
                        print("bet", player.on_game)
                    elif actionmsg.content == "s":
                        print("stand", player.on_game)
                except TimeoutError:
                    break

client.run(token)
