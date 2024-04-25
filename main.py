import discord
from discord.ext import commands
from discord.ext.commands import CommandInvokeError
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("TOKEN")

THE_GUILD = discord.Object(id=858764161705443348)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
  print("hello there")
  activity = discord.Activity(name="over you, Austrian Empire..",
                              type=discord.ActivityType.watching)
  await bot.change_presence(activity=activity)
  synced = await bot.tree.sync()

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content.startswith("austria"):
    await message.reply("austrian empire!!!")
  if message.content.startswith("who is MoB"):
    await message.reply(f"Hey look, buddy. I'm an engineer, that means I solve problems. Not problems like (What is beauty?), 'cause that would fall within the purview of your conundrums of philosophy. I solve practical problems! For instance, how am I gonna stop some big mean Mother-Hubbard from tearin' me a structurally superfluous new behind? The answer? Use a gun. And if that don't work, use more gun. Like this heavy-caliber tripod-mounted little-old-number designed by me. Built, by me. And you best hope... It's not pointed at you.- engineer tf2")
  if message.content.startswith("what is this group") or message.content.startswith('what is this server'):
    await message.reply("Hey, assuming that you dont know what this server is, you can **execute the command $serverinfo** or use the slash command!")



@bot.hybrid_command(name="serverinfo", description="get all server info here")
async def serverinfo(ctx):
  embedVar2 = discord.Embed(
      title="The Austrian Empire",
      description="  quick info about what this server is",
      color=0x00ff00)
  embedVar2.add_field(
      name="What to do here?",
      value=
      "You can chat here, talk while your friends are offline, play with our awesome bots, join our allies and all of that cool and amazing stuff!",
      inline=True)
  embedVar2.add_field(
      name="What is this place?",
      value=
      f"The Austrian Empire is a community server and we do some roblox things here! **Roblox is recommended!!**",
      inline=True)
  embedVar2.add_field(
      name="Problems and Feedback?",
      value=
      f"If you have any problems, feel free to ping any of our mods. If you have any feedback, go to the suggestions category and give us some suggestions!",
      inline=False)
  embedVar2.add_field(
      name="Roblox Groups!",
      value=
      f"You can also find us on Roblox! Do note, that these roblox groups are not really used anymore. https://www.roblox.com/groups/17139488/TCA-The-Chicken-Army#!/about https://www.roblox.com/groups/10646029/OTS-Organization-of-Turkic-States#!/about",
      inline=False)
  embedVar2.set_author(name="Welcome to:")
  embedVar2.set_footer(text=" - The Austrian Empire")
  await ctx.send(embed=embedVar2)


@bot.command()
async def send_message(ctx, *args):
  arguments = " ".join(args)
  if arguments == "@everyone" or arguments == "@here" or "@" in arguments:
    await ctx.send(
        f"Stop. Do not try that again. Do not attempt to ping everyone again. @ is not allowed."
    )
  else:
    await ctx.message.delete()
    await ctx.send(arguments)


@bot.tree.command(name="send_message",
                  description="send a message using slash commands")
@app_commands.describe(messagetosend="what should MoB send?")
async def send_message(ctx, messagetosend: str):
  if messagetosend == "@everyone" or messagetosend == "@here" or "@" in messagetosend:
    await ctx.response.send_message(
        f"Stop. Do not try that again. Do not attempt to ping everyone again. @ is not allowed."
    )
  else:
    await ctx.response.send_message(messagetosend)


@bot.command(name="eightball")
async def eightball(ctx, question):
  try:
    possibly = [
        "yes", "no", "strong maybe", "ask again", "maybe in the future",
        "absolutely not", "sure i guess"
    ]
    randomchoice = random.choice(possibly)
    await ctx.send("hmm lemme think...")
    time.sleep(2)
    await ctx.send(randomchoice)

  except MissingRequiredArgument:
    await ctx.send("{message.author.mention}, $eightball <your question here>")


@bot.tree.command(name="eightball",
                  description="ask the eight ball a question...")
@app_commands.describe(eightball_question="ask em a question")
async def eightball(ctx, eightball_question: str):
  try:
    possibly = [
        "yes", "no", "strong maybe", "ask again", "maybe in the future",
        "absolutely not", "sure i guess"
    ]
    randomchoice = random.choice(possibly)
    await ctx.response.send_message(randomchoice)
  except:
    await ctx.response.send_message("nah it didn't work idk why lol")


@bot.hybrid_command(name="serverstats",
                    description="get the server stats for the Austrian Empire")
async def serverstats(ctx):
  await ctx.send(f"Austrian Empire stats: ")
  guild = ctx.guild
  if guild:
    roles = len(guild.roles)
    channels = len(guild.channels)
    emojis = len(guild.emojis)
    stickers = len(guild.stickers)
    threads = len(guild.threads)
    voice = len(guild.voice_channels)
    members = len(guild.members)
  embedVar = discord.Embed(
      title="Server Stats",
      description="Displaying all statistics for the Austrian Empire",
      color=0x00ff00)
  embedVar.add_field(name="Roles", value=f"Roles: {roles}", inline=True)
  embedVar.add_field(name="Channels",
                     value=f"Channels: {channels}",
                     inline=True)
  embedVar.add_field(name="Emojis", value=f"Emojis: {channels}", inline=True)
  embedVar.add_field(name="Stickers",
                     value=f"Stickers: {stickers}",
                     inline=True)
  embedVar.add_field(name="Threads", value=f"Threads: {threads}", inline=True)
  embedVar.add_field(name="Voice",
                     value=f"Voice Channels: {voice}",
                     inline=True)
  embedVar.add_field(name="Members",
   value=f"Members: {ctx.guild.member_count}",
   inline=True)
  embedVar.set_footer(text="- The Austrian Empire")
  await ctx.send(embed=embedVar)
  #await ctx.send(f"Roles: {roles}, Channels: {channels}, Emojis: {emojis}, Stickers: {stickers}, Threads: {threads}, Voice Channels = {voice}")


@bot.hybrid_command(name="commands",
                    description="get all commands for this bot")
async def cmds(ctx):
  cmdsembed = discord.Embed(
      title="commands",
      description="Displaying all commands for Austrian Empire's bot",
      color=0x00ff00)

  cmdsembed.add_field(
      name=f"Server Stats ($serverstats)",
      value=
      "Displays stats for Austrian Empire such as emojis, stickers, etc. Can use with slash commands",
      inline=False)
  cmdsembed.add_field(
      name=f"Server Info ($serverinfo)",
      value="Displays info about this server. Can use with slash commands",
      inline=False)
  cmdsembed.add_field(name=f"Send Message ($send_message)",
                      value="Makes the bot send a message.",
                      inline=False)
  cmdsembed.add_field(
      name=f"Eightball ($eightball (question))",
      value="Answers your questions, with a randomized answer..",
      inline=False)
  cmdsembed.add_field(name=f"Commands ($commands)",
                      value="This!",
                      inline=False)
  cmdsembed.set_footer(text="- The Austrian Empire")
  await ctx.send(embed=cmdsembed)


bot.run(DISCORD_TOKEN)
