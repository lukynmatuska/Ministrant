from disnake import ApplicationCommandInteraction
from disnake.ext import commands, tasks
from config.messages import Messages
from datetime import time, datetime

modlitebna_room = 961304110274056212


class Praying(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.send_pray.start()

    local_tz = datetime.now().astimezone().tzinfo

    @commands.slash_command(description=Messages.pray_brief)
    async def pray(self, inter: ApplicationCommandInteraction):
        await inter.send(Messages.pray_string)

    @tasks.loop(time=time(7, 0, tzinfo=local_tz))
    async def send_pray(self):
        modlitebna = self.bot.get_channel(modlitebna_room)
        await modlitebna.send(Messages.pray_string)


def setup(bot: commands.Bot):
    bot.add_cog(Praying(bot))
