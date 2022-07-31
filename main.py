#!/usr/bin/python3
# Import the necessary libraries.
import logging
#import disnake
from disnake import Embed, TextChannel, AllowedMentions, Intents, Game, Member
from disnake.ext import commands
import os
from dotenv import load_dotenv

# Setup logging
logger = logging.getLogger('disnake')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# Getting .env value.
load_dotenv()

# Creating a commands.Bot() instance, and assigning it to "bot"
bot = commands.Bot(
    command_prefix = ";",
    #help_command=None,
    #allowed_mentions=AllowedMentions(roles=False, everyone=False, users=True),
    intents = Intents.all(),
    activity = Game(name="Arii tagging"),
)


# When the bot is ready, run this code.
@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.event
async def on_message(message):
    print(f"message: {message}")
    if "Ari" in message.author.name or "ari" in message.content.lower():
        await message.reply("<@282207827332694017> ty jsi vůl!")

@bot.command(description="Unmutes a specified user.")
# @commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: Member):
    # mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    # await member.remove_roles(mutedRole)
    await member.send(f" you have unmutedd from: - {ctx.guild.name}")
    embed = Embed(
           title = "unmute",
           description = f" unmuted-{member.mention}",
           colour = Colour.light_gray()
    )
    await ctx.send(embed=embed)

bot.load_extension("cogs.ping")  # Note: We did not append the .py extension.

# Login to Discord with the bot's token.
#bot.run(DISCORD_BOT_TOKEN)
# bot.run("Nzg2ODgxNDY1MjQ5NTYyNjc1.GEJHD5.QCRh_sZ_RNfTc8djwHumIAepV-VyKJ_3hTOU-Q")
bot.run("OTc4OTIyMTA0NjYzNzExNzg0.GFvxNv.LvHI4vpGWG3DhiCVzo43pn97iQhpj8lYcnny5g")

