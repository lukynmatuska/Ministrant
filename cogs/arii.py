# Import the necessary libraries.
from disnake import ApplicationCommandInteraction, File, Message
from disnake.ext import commands

# Setup global variables
fest_counter = 0
FEST_STRING = "fest"
# FEST_COUNTED_STRING = f"Pocet pouziti \"{FEST_STRING}\" od meho spusteni je {fest_counter}."
ARII_DISCORD_ID = 282207827332694017
ARII_SLEEPING_IMAGE = "./assets/sleepingAri.png"
OVERSLEEP_WORD = "zaspal"

class Arii(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # When the bot receive some message, run this code.
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        # Use global variables
        global fest_counter

        # Send notification when oversleep
        if message.author.id == ARII_DISCORD_ID and OVERSLEEP_WORD in message.content.lower():
            with open(ARII_SLEEPING_IMAGE, "rb") as f:
                await message.reply(
                    file = File(
                        fp = f,
                        # filename = "Sleeping Arii.png",
                    )
                )

        # Count in fest word
        if FEST_STRING in message.content.lower() and message.author.id != self.bot.user.id and not message.author.bot:
            await message.reply(FEST_STRING)
            fest_counter += 1
    
    # When somebody use /fest command, run this code.
    @commands.slash_command(
            description = f"Vraci pocet pouziti \"{FEST_STRING}\" od spusteni."
    )
    async def fest(self, inter: ApplicationCommandInteraction):
        # Use global variables
        global fest_counter
        await inter.response.defer()
        await inter.followup.send(f"Pocet pouziti \"{FEST_STRING}\" od meho spusteni je {fest_counter}.")

def setup(bot: commands.Bot):
    bot.add_cog(Arii(bot))
