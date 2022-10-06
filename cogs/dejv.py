import random
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

        message_content = message.content.lower()

        for string in Messages.activation_strings:
            if string in message_content:
                for string in Messages.vutis_strings:
                    if string in message_content:
                        await message.reply(Messages.dejv_vut_is)
                        return
                with open(DEJV_IMAGE_ROUTE, "rb") as f:
                    await message.reply(random.choice(Messages.dejv_repair_strings), file=File(f))


def setup(bot: commands.Bot):
    bot.add_cog(Dejv(bot))
