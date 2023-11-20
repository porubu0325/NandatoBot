import discord
from discord.ext import commands
import os
import random
import datetime
import time

PREFIX='/'
bot = commands.Bot(command_prefix=PREFIX)
token = 'DISCORD_BOT_TOKEN'

#終了コマンド
@bot.command()
async def end(ctx):
    if ctx.message.author.id YOURID:
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="終了中",description=f"終了中", color=color))
        await ctx.message.delete()
        await bot.close()
    else:
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="XXXXX", description="お前......", color=color))
        await ctx.message.delete()

# pong
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Hello World
@bot.command()
async def Hello(ctx):
    await ctx.send('Hello World')

# Fizz Buzz
@bot.command(name='fizzbuzz')
async def fizzbuzz(ctx, number: int):
    response = ""
    if number % 3 == 0:
        response += "Fizz"
    if number % 5 == 0:
        response += "Buzz"
    if not response:
        response = str(number)

    await ctx.send(response)

@bot.event #メインチャンネル
async def on_message(message):
    print("It's me, Mario....")
    if message.author == bot.user:
        return
        
bot.run(token)
