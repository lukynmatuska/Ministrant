from disnake import ApplicationCommandInteraction, File, Message
from disnake.ext import commands
from config.messages import Messages

fest_counter = 0
ARII_DISCORD_ID = 282207827332694017
ARII_SLEEPING_IMAGE = "./assets/sleepingAri.png"


class Arii(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # When the bot receive some message, run this code.
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        # Use global variables
        global fest_counter

        # Send notification when oversleep
        if message.author.id == ARII_DISCORD_ID and Messages.oversleep_word in message.content.lower():
            with open(ARII_SLEEPING_IMAGE, "rb") as f:
                await message.reply(
                    file=File(
                        fp=f,
                        # filename = "Sleeping Arii.png",
                    )
                )

        # Count in fest word
        if (
            Messages.fest_string in message.content.lower()
            and message.author.id != self.bot.user.id
            and not message.author.bot
        ):
            await message.reply(Messages.fest_string)
            fest_counter += 1

    # When somebody use /fest command, run this code.
    @commands.slash_command(
            description=Messages.fest_brief
    )
    async def fest(self, inter: ApplicationCommandInteraction):
        global fest_counter
        await inter.send(Messages.fest_count.format(fest_counter=fest_counter))


def setup(bot: commands.Bot):
    bot.add_cog(Arii(bot))
