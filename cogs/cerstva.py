import discord
from discord.ext import commands


class cerstva(commands.Cog):

    def __init__(self, client):
        self.client = client
####    async def on_ready(self):
####        print(f'Logged in as {self.user} (ID: {self.user.id})')
####        print('------')
##    @commands.Cog.listener()
        
##    async def on_Message(self, message):
##        # we do not want the bot to reply to itself
##        if message.author.id == self.user.id:
##            return
##
##        if message.content.startswith('hello'):
##            await message.reply('Hello!', mention_author=True)
        
##    quest = ['Čerstvá',
##           'cerstva',
##           'je čerstvá',
##           'čerstvá']
##    @commands.Cog.listener()
##    async def on_message(self, message):
##        for i in quest:
##            if i in message.content:
##                await message.reply('Není čerstvá', mention_author=True)
##        
    @commands.Cog.listener()
    async def on_message(self, msg):
            if msg.content == ("Je čerstvá"):
                await msg.reply('Není čerstvá!', mention_author=True)
##            if Message.content == ("Není čerstvá"):
##                await Message.reply('Je čerstvá!', mention_author=True)

##    @commands.Cog.listener()
##    async def on_message(self, message):
##        if message.content ==('Je čerstvá'):
##            channel = message.channel
##            await channel.send('Není čerstvá!')
##
##            def check(self, message1):
##                return message1.content == 'Není čerstvá' and message1.channel == channel
##
##            msg = await client.wait_for('message', check=check)
##            await channel.send("Je čerstvá!".format(msg))
##        
def setup(client):
    client.add_cog(cerstva(client))
