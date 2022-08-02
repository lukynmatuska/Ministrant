# Import the necessary libraries.
from disnake import Message
from disnake.ext import commands

# Setup global variables
uhoh_counter = 0

class UhOh(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # When the bot receive some message, run this code.
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        global uhoh_counter

        if message.author.id != self.bot.user.id and "uh oh" in message.content.lower() and not message.author.bot:
            await message.reply("uh oh")
        #elif config.uhoh_string in message.content.lower():
        #    await message.channel.send("uh oh")
            uhoh_counter += 1
    
    # When somebody use /uhoh command, run this code.
    @commands.command(brief="Messages.uhoh_brief")
    async def uhoh(self, ctx):
        global uhoh_counter
        await ctx.reply(f"Pocet uh oh od spusteni je {uhoh_counter}")

def setup(bot: commands.Bot):
    bot.add_cog(UhOh(bot))
