from disnake import ApplicationCommandInteraction
from disnake.ext import commands, tasks
from config.messages import Messages
from datetime import time, datetime
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./config/.env")


class Praying(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.send_pray.start()

    local_tz = datetime.now().astimezone().tzinfo

    @commands.slash_command(description=Messages.pray_brief)
    async def pray(self, inter: ApplicationCommandInteraction):
        await inter.send(Messages.pray_string)

    @tasks.loop(time=time(int(os.getenv("PRAYING_HOUR")), int(os.getenv("PRAYING_MINUTE")), tzinfo=local_tz))
    async def send_pray(self):
        modlitebna = self.bot.get_channel(int(os.getenv("MODLITEBNA_ROOM")))
        await modlitebna.send(Messages.pray_string)


def setup(bot: commands.Bot):
    bot.add_cog(Praying(bot))
