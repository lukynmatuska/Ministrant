from random import randint, random
from disnake import ApplicationCommandInteraction, File, Message
from disnake.ext import commands

#will maybe be seperated into a file later when i feel like it
ACTIVATION_STRINGS = ["zavoláme dejva","zavolame dejva","zavoláme na to dejva","zavolame na to dejva","na to zavolame dejva","hej, dejve!","dejve, pojd to opravit"]
DEJV_IMAGE_ROUTE = "./assets/dejvOpravar.png"
DEJV_REPAIR_STRINGS = ["Přicházá Dejv a jde to opravit", "Zde jde Dave, naše spása", "Uhněte z cesty, přichází Dejv","Znáte Dejva, všechno spraví!"]
VUTIS_STRINGS = ["vutis","vut is","studis"]
SADVID_EMOTE_ID_STRING = "<:sadvid:976410247105241098>"

#class definition
class Dejv(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

     # When the bot receive some message, run this code.
    @commands.Cog.listener()
    async def on_message(self, message: Message):

        nalezeno = False

        for string in ACTIVATION_STRINGS:
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
                    await message.reply(DEJV_REPAIR_STRINGS[randint(0,len(DEJV_REPAIR_STRINGS)-1)],
                        file = File(
                            fp = f,
                        )
                    )


def setup(bot: commands.Bot):
    bot.add_cog(Dejv(bot))