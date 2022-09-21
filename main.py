#!/usr/bin/python3
# Import the necessary libraries.
import logging
from disnake import Embed, TextChannel, AllowedMentions, Intents, Game, Member, File, Message, TextInputStyle, ui, ModalInteraction, AppCmdInter
from disnake.ext import commands
import os
from os.path import isfile
from dotenv import load_dotenv

# Setup logging
logger = logging.getLogger('disnake')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# Getting .env values
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Creating a commands.Bot() instance, and assigning it to "bot"
bot = commands.Bot(
    command_prefix = ";",
    # help_command = None,
    # allowed_mentions = AllowedMentions(roles = False, everyone = False, users = True),
    intents = Intents.all(),
    activity = Game(name="Modlení"),
    sync_commands_debug = True,
    test_guilds = [828675132365078618],
)


# When the bot is ready, run this code.
@bot.event
async def on_ready():
    print("The bot is ready!")

# Load extenesions
for name in os.listdir("./cogs"):
    filename = f"./cogs/{name}"
    modulename = f"cogs.{name}"

    if isfile(filename) and filename.endswith(".py"):
        bot.load_extension(modulename[:-3])

# Login to Discord with the bot's token.
bot.run(DISCORD_BOT_TOKEN)
