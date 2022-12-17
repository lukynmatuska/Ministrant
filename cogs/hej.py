from disnake import Message
from disnake.ext import commands
from config.messages import Messages

hej_counter = 0
hou_counter = 0


class HejHou(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        """
        Send "hou" when someone sends message containing "hej" and vice versa
        """

        global hej_counter
        global hou_counter

        if message.author.bot:
            return

        if message.author.id != self.bot.user.id and "hej" in message.content.lower():
            await message.reply("hou")
            hej_counter += 1

        if message.author.id != self.bot.user.id and "hou" in message.content.lower():
            await message.reply("hej")
            hou_counter += 1

    @commands.command(description=Messages.hej_brief)
    async def hej(self, ctx):
        global hej_counter
        await ctx.reply(f"Pocet hej od spusteni je {hej_counter}")

    @commands.command(description=Messages.hou_brief)
    async def hou(self, ctx):
        global hou_counter
        await ctx.reply(f"Pocet hou od spusteni je {hou_counter}")


def setup(bot: commands.Bot):
    bot.add_cog(HejHou(bot))
