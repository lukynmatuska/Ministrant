from disnake import ApplicationCommandInteraction
from disnake.ext import commands
from config.messages import Messages



class Praying(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # When somebody use /pray command, run this code.
    @commands.slash_command(description="Ministrant se pomodlí.")
    async def pray(self, inter: ApplicationCommandInteraction):
        await inter.response.defer()
        await inter.followup.send(Messages.pray_string)


def setup(bot: commands.Bot):
    bot.add_cog(Praying(bot))
