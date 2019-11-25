import discord
from discord.ext import commands
import random

def get_prefix(client,message):
    prefixes=['polly ','Polly ','p ','P ']
    return prefixes
bot = commands.Bot(command_prefix=get_prefix,case_insensitive=True)
bot.remove_command('help')

def randomNo(rangeOne,rangeTwo):
  for x in range(1):
    x = random.randint(rangeOne,rangeTwo)
  return x
