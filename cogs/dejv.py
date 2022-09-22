from random import randint
from disnake import File, Message
from disnake.ext import commands
from config.messages import Messages

DEJV_IMAGE_ROUTE = "./assets/dejvOpravar.png"
VUTIS_STRINGS = ["vutis","vut is","studis"]
SADVID_EMOTE_ID_STRING = "<:sadvid:976410247105241098>"

#class definition

class Dejv(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):

        nalezeno = False
        
        """
        When message with specific content from activation_strings
        is detected the bot sends response.
        """

        for string in Messages.activation_strings:
            if string in message.content.lower():
                nalezeno = True
                break;

        if nalezeno:

            nalezeno = False

            for string in VUTIS_STRINGS:
                if string in message.content.lower():
                    nalezeno = True
                    break;
            
            if nalezeno:
                await message.reply("VUT IS ani Dejv nespraví " + SADVID_EMOTE_ID_STRING)
                    
            else:
                with open(DEJV_IMAGE_ROUTE, "rb") as f:
                    await message.reply(
                        Messages.dejv_repair_strings[randint(0, len(Messages.dejv_repair_strings)-1)],
                        file=File(fp=f,)
                    )


def setup(bot: commands.Bot):
    bot.add_cog(Dejv(bot))
