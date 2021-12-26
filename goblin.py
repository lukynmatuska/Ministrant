import discord
import random
import os

from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Watching porn'))
    print('Bot je online.')
    
#kdyz napisu .ping, tak to napise pong
@client.command()
async def ping(ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

    
#clear funkce
@client.command(aliases=['smaz'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member: discord.Member, *, reason='Proste jsi nas nasral'):
    await member.kick(reason=reason)

#ban/unban
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Byl popraven {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator)==(member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanovan {user.mention}')
            return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    
#load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

##@client.event
##async def on_message(message):
##    if message.content == "ping":
##        await message.reply('pong', mention_author=True)
        
##@client.event
##async def on_message(message):
##        if message.content == ("Je čerstvá" or "čerstvá"):
##            await message.reply('Není čerstvá', mention_author=True)


client.run('OTA3MzkyMTc4MjkxMTEwMDE5.YYmg0Q.52bnoc0hAOQ1lkqicwGqssMT0HI')


