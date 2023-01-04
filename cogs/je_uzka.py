from disnake import Message
from disnake.ext import commands
import re


class JeUzka(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_message_author = ""

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        """
        Send "hou" when someone sends message containing "hej" and vice versa
        """

        if message.author.bot:
            return

        message_lower = message.content.lower()

        if re.search(r"nen(i|í) (ú|u)zk(á|a)", message_lower):
            self.last_message_author = message.author
            return await message.reply("JE ÚZKÁ <:blazaGasm:1059467411444727848>")

        if re.search(r"je (ú|u)zk(á|a)", message_lower) and message.author == self.last_message_author:
            return await message.reply("<:ano:977641577604333630> JE ÚZKÁ <:blazaGasm:1059467411444727848>")


def setup(bot: commands.Bot):
    bot.add_cog(JeUzka(bot))
