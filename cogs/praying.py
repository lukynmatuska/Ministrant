from disnake import ApplicationCommandInteraction
from disnake.ext import commands
from config.messages import Messages


class Praying(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description=Messages.pray_brief)
    async def pray(self, inter: ApplicationCommandInteraction):
        await inter.send(Messages.pray_string)


def setup(bot: commands.Bot):
    bot.add_cog(Praying(bot))
