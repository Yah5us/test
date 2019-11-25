import discord
from discord.ext import commands
import random
import keep_alive
import custom_commands
import os
from datetime import datetime

def get_prefix(client,message):
    prefixes=['polly ','Polly ','p ','P ']
    return prefixes
bot = commands.Bot(command_prefix=get_prefix,case_insensitive=True)
bot.remove_command('help')

@bot.event #Defines aspect of bot when ready, also sends ready message to dev
async def on_ready():
  await bot.change_presence(activity=discord.Game('#BirbdGang'), status = None, afk=False)
  print('Bot is ready')

@bot.command() #HELP
async def help(ctx):
  embed=discord.Embed(
    title="**Polly Help**",
    description=
    """
    p help - show this message
    p info - show bot info
    p pp <@user> - find pp length of any user (100% accurate)
    p quack <@user> - quack at user (kick perm only)
    p quote <message id> - quote a message (from same channel)
    """,
    colour=discord.Colour.teal()
  )
  await ctx.send(embed=embed)

@bot.command() #INFO
async def info(ctx):
  pfp=bot.user.avatar_url
  embed=discord.Embed(
   title="**Polly Info**",
   description=None,
   colour=discord.Colour.teal()
  )
  embed.add_field(name="\U0001F539"+"What is Polly?"+"\U0001F539",value="Polly is a fun bot that was made for the birbd gang.",inline=False)
  embed.set_footer(text="Created by Yah5us#5704 using Python 3.7 and discord.py")
  await ctx.send(embed=embed)

@bot.command() #PP
async def pp(ctx,user:discord.Member=None):
  if user==None:
    user=ctx.message.author
  x=custom_commands.randomNo(1,5)
  if x==1:
    embed=discord.Embed(
      title="{}'s pp:".format(user.name),
      description="8D",
      colour=discord.Colour.red()
    )
    embed.sest_footer(text="'It'll get bigger' 'No it won't'")
    await ctx.send(embed=embed)
  if x==2:
    embed=discord.Embed(
      title="{}'s pp:".format(user.name),
      description="8=D",
      colour=discord.Colour.red()
    )
    embed.sest_footer(text="Hung like a baby")
    await ctx.send(embed=embed)
  if x==3:
    embed=discord.Embed(
      title="{}'s pp:".format(user.name),
      description="8==D",
      colour=discord.Colour.gold()
    )
    await ctx.send(embed=embed)
    embed.sest_footer(text="smoll boi")
  if x==4:
    embed=discord.Embed(
      title="{}'s pp:".format(user.name),
      description="8===D",
      colour=discord.Colour.teal()
    )
    await ctx.send(embed=embed)
    embed.sest_footer(text="Is there a banana in your pants or are you just happy to see me?")
  if x==5:
    embed=discord.Embed(
      title="{}'s pp:".format(user.name),
      description="8====D",
      colour=discord.Colour.teal()
    )
    embed.sest_footer(text="It's soooooo big!")
    await ctx.send(embed=embed)

@bot.command() #QUACK!
@commands.has_permissions(kick_members=True)
async def quack(ctx, user:discord.Member=None):
  if user==None:
    user=ctx.message.author
  await ctx.channel.purge(limit=1)
  await ctx.send("Quack, "+user.mention+"!")

@bot.command() #QUOTE
async def quote(ctx,ID):
    msg=await ctx.fetch_message(ID)
    pfp=msg.author.avatar_url
    if msg.author.nick==None:
      name=msg.author.name+"#"+msg.author.discriminator
    else:
      name=msg.author.nick
    embed=discord.Embed(
      description=
      """
      **"**{}**"**
      """.format(msg.content),
      colour=discord.Colour.teal()
      )
    embed.set_author(name=name,icon_url=pfp)
    embed.set_footer(text="-{}, ".format(name)+msg.created_at.strftime("%b %d, %Y"))
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)

keep_alive.keep_alive()
token=os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
