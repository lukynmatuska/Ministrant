# Import the necessary libraries.
from disnake import Message, ApplicationCommandInteraction
from disnake.ext import commands

# Setup global variables
PRAY_STRING = "Yeete náš, jenž jsi na nebesích,\ngde body tvé.\ngde opravené písemky tvé.\n\nBuď body tvé jako v nebi, tak i na zemi.\nŘešení naše vzorové dej nám dnes.\n\nA odpusť nám naše chyby,\njako i my odpouštíme tvoje na cviku.\nA neuveď nás v opakování,\nale zbav nás od Fka.\nAmen RNGesus"

class Praying(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
 
    # When somebody use /pray command, run this code.
    @commands.slash_command(
            description = f"Ministrant se pomodlí."
    )
    async def pray(self, inter: ApplicationCommandInteraction):
        await inter.response.defer()
        await inter.followup.send(PRAY_STRING)

def setup(bot: commands.Bot):
    bot.add_cog(Praying(bot))
