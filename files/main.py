import discord
from discord.ext import commands
from discord.ext.commands import CommandInvokeError
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
  activity = discord.Game(name="bot goes offline when notacupofmilk does")
  await bot.change_presence(activity=activity)

@bot.command()
async def serverinfo(ctx):
  embedVar2 = discord.Embed(title="The Chicken Community", description = "Description about the chicken community and info", color = 0x00ff00)
  embedVar2.add_field(name = "What to do here?", value = "You can chat here, talk while your friends are offline, play with our awesome bots, join our allies and all of that cool and amazing stuff!", inline = False)
  embedVar2.add_field(name = "What is this place?", value = f"The Chicken Community is a community server (obviously) and we do some roblox things here! Roblox is recommended!!", inline = False)
  embedVar2.add_field(name = "Problems and Feedback?", value = f"If you have any problems, feel free to ping any of our mods. If you have any feedback, go to the suggestions category and give us some suggestions!", inline = False)
  await ctx.send(embed=embedVar2)


@bot.command()
async def send_message(ctx, *args):
    try:
        arguments = " ".join(args)
        await ctx.send(arguments)
    except CommandInvokeError:
        await ctx.send("Type a real message, not empty ones!")



@bot.command()
async def serverstats(ctx):
  await ctx.send(f"Chicken army stats: ")
  guild = ctx.guild
  if guild:
    roles = len(guild.roles)
    channels = len(guild.channels)
    emojis = len(guild.emojis)
    stickers = len(guild.stickers)
    threads = len(guild.threads)
    voice = len(guild.voice_channels)
  embedVar = discord.Embed(title = "Server Stats", description = "server stats here", color = 0x00ff00)
  embedVar.add_field(name = "Server Stuff", value = f"Roles: {roles}, Channels: {channels}, Emojis: {emojis}, Stickers: {stickers}, Threads: {threads}, Voice Channels = {voice}", inline = True)
  await ctx.send(embed=embedVar)
    #await ctx.send(f"Roles: {roles}, Channels: {channels}, Emojis: {emojis}, Stickers: {stickers}, Threads: {threads}, Voice Channels = {voice}")


@bot.command()
async def cmds(ctx):
  await ctx.send("serverinfo for vague info about server, send_message for making bot send messages, serverstats to find out about server stats")


bot.run(DISCORD_TOKEN)