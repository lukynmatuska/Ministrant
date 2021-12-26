#Prvni argument kazde fukce tady musi byt 'self'


import discord
import random
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
        
##EVENTS
##    @commands.Cog.listener()
##    async def on_ready(self):
##        print('Ready!')
##        print('Logged in as ---->', self.client.user)
##        print('ID:', self.client.user.id)
##
##         
##COMMANDDS

    @commands.command(aliases=['8ball', 'test'])
    async def _8ball(self, ctx, *, question):
        responses = ['Zalezi, jak to citis',
                     'Rozhodne ano',
                     'Naser si',
                     'Neznám nic lepšího',
                     'Tvoje zvědavost hraničí s drzostí!',
                     'To je ve hvězdách',
                     'To je ale hloupá otázka',
                     'O tom se nemluví',
                     'Ses zbláznil?!',
                     'Zeptej se Jardy',
                     'Ty o tom pochybuješ?',
                     'Co není, může být',
                     'Neprovokuj!',
                     'Budu o tom přemýšlet',
                     'Já ne, ale ty?',
                     'Na to jsem málo opilý',
                     'Nemohu odpovědět přede všemi',
                     'Ano',
                     'Ne',
                     'Nelze',
                     'Není ve smlouvě',
                     'Zrovna tohle ve smlouvě mám, takže lze :)',
                     'Jsem super.',
                     'Jarda je nejlepší.',
                     'A?',
                     'Tvoje máma',
                     'Nepřej si mně, pokud si myslíš, že ano',
                     'Půjdu snad offline, tady nemám co dělat *sigh*']
        await ctx.send(f'Otazka: {question}\nOdpoved: {random.choice(responses)} ')

    @commands.command()
    async def stouch(self, ctx):
        await ctx.send(f'Nestouchej me pls :(')
        

def setup(client):
    client.add_cog(Example(client))
