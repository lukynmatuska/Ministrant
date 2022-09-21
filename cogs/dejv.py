from random import randint
from disnake import File, Message
from disnake.ext import commands
from config.messages import Messages

DEJV_IMAGE_ROUTE = "./assets/dejvOpravar.png"


class Dejv(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        """
        When message with specific content from activation_strings
        is detected the bot sends response.
        """

        for string in Messages.activation_strings:
            if string in message.content.lower():
                with open(DEJV_IMAGE_ROUTE, "rb") as f:
                    await message.reply(
                        Messages.dejv_repair_strings[randint(0, len(Messages.dejv_repair_strings)-1)],
                        file=File(fp=f,)
                    )


def setup(bot: commands.Bot):
    bot.add_cog(Dejv(bot))
