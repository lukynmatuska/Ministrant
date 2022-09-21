from disnake import Message
from disnake.ext import commands
from config.messages import Messages

uhoh_counter = 0


class UhOh(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        """
        Send "uh oh" when someone sends message containing "uh oh"
        """

        global uhoh_counter

        if message.author.bot:
            return

        if message.author.id != self.bot.user.id and "uh oh" in message.content.lower():
            await message.reply("uh oh")
            uhoh_counter += 1

    @commands.command(description=Messages.uhoh_brief)
    async def uhoh(self, ctx):
        global uhoh_counter
        await ctx.reply(f"Pocet uh oh od spusteni je {uhoh_counter}")


def setup(bot: commands.Bot):
    bot.add_cog(UhOh(bot))
