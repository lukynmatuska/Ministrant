# Import the necessary libraries.
from disnake import ApplicationCommandInteraction, Embed, Colour, Message, FFmpegPCMAudio, PCMVolumeTransformer, VoiceChannel
from disnake.ext import commands

VOICE_CHANNEL_DISCORD = 1001526114793046147
VOICE_CHANNEL_SOUND = "./assets/m.mp3"

# Setup global variables
PRAY_STRING = "Yeete náš, jenž jsi na nebesích,\ngde body tvé.\ngde opravené písemky tvé.\n\nBuď body tvé jako v nebi, tak i na zemi.\nŘešení naše vzorové dej nám dnes.\n\nA odpusť nám naše chyby,\njako i my odpouštíme tvoje na cviku.\nA neuveď nás v opakování,\nale zbav nás od Fka.\nAmen RNGesus"

import asyncio
import youtube_dl

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ""


ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    "options": "-vn"
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        assert data

        if "entries" in data:
            # take first item from a playlist
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        assert filename

        return cls(FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Praying(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        # connect to channel
        channel: VoiceChannel = self.bot.get_channel(1001526114793046147) # VOICE_CHANNEL_DISCORD)
        print(f"channel: {channel}")
        if channel is None:
            return
        channel.connect()

        # play sound
        # source = PCMVolumeTransformer(FFmpegPCMAudio(VOICE_CHANNEL_SOUND))
        # ctx.voice_client.play(source, after=lambda e: print(f"Player error: {e}") if e else None)

    # When somebody use /pray command, run this code.
    @commands.slash_command(
        description = f"Ministrant se pomodlí."
    )
    async def pray(
        self,
        inter: ApplicationCommandInteraction
        ):
        await inter.response.defer()
        await inter.followup.send(PRAY_STRING)

    @commands.slash_command(
        description = "Ministrant se připojí do hlasového kanálu"
    )
    async def join(
        self,
        inter: ApplicationCommandInteraction,
        channel: VoiceChannel = commands.Param(name = "channel")
        ):
        """
        Parameters
        ----------
        channel: Kanál, kam se má Ministrant připojit.
        """
        await inter.response.defer()

        # Prepare embed for response
        embed = Embed(
            colour = Colour.green()
        )
        embed.set_footer(
            text = f"Může za to {inter.author.name}"
        )


        if inter.bot.voice_clients is not None:
            for voice_client in inter.bot.voice_clients:
                await voice_client.move_to(channel)

                # Message reply
                embed.title = f"Přepojil jsem se do kanálu `{channel}`."
                embed.description = "Bo si se mnou chcó zabžondat i někde jinde."
                return await inter.followup.send(
                    embed = embed
                )
        
        await channel.connect()
        
        # Message reply
        embed.title = f"Připojil jsem se do kanálu `{channel}`."
        embed.description = "Bo si se mnou někdo chce zabžondat."
        await inter.followup.send(
            embed = embed
        )

    @commands.slash_command(
        description = "Ministrant zaspívá písničku ze své paměti."
    )
    async def play(
        self,
        inter: ApplicationCommandInteraction,
        file: str = commands.Param(name = "file")
        ):
        """
        Parameters
        ----------
        file = Soubor písničky, co má Ministrant zazpívat.
        """
        await inter.response.defer()

        # Prepare embed for response
        embed = Embed(
            color = Colour.blue()
        )
        embed.set_footer(
            text = f"Může za to {inter.author.name}"
        )

        await self.ensure_voice(inter)
        source = PCMVolumeTransformer(FFmpegPCMAudio(file))
        if inter.bot.voice_clients is not None:
            for voice_client in inter.bot.voice_clients:
                voice_client.play(source, after=lambda e: print(f"Player error: {e}") if e else None)
                embed.title = f"Právě zpívám `{file}`."
                embed.description = "Bo si rád békám s ostatníma."
                return await inter.followup.send(
                    embed = embed
                )
        embed.title = "Tož keď niesom v roomke, tak nemožu békat."
        embed.description = "Aj, aj, ty jsi ale nešika."
        await inter.followup.send(
            embed = embed
        )

    # @commands.command()
    # async def yt(self, ctx, *, url):
    #     """Plays from a url (almost anything youtube_dl supports)"""
    #     await self.ensure_voice(ctx)
    #     async with ctx.typing():
    #         player = await YTDLSource.from_url(url, loop=self.bot.loop)
    #         ctx.voice_client.play(
    #             player, after=lambda e: print(f"Player error: {e}") if e else None
    #         )

    #     await ctx.send(f"Now playing: {player.title}")

    # @commands.command()
    # async def stream(self, ctx, *, url):
    #     """Streams from a url (same as yt, but doesn't predownload)"""
    #     await self.ensure_voice(ctx)
    #     async with ctx.typing():
    #         player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
    #         ctx.voice_client.play(
    #             player, after=lambda e: print(f"Player error: {e}") if e else None
    #         )

    #     await ctx.send(f"Now playing: {player.title}")

    # @commands.slash_command(
    #     description = "Změna hlasitosti"
    # )
    # async def volume(
    #     self,
    #     inter: ApplicationCommandInteraction,
    #     volume: int = commands.Param(name = "volume")
    # ):
    #     """
    #     Parameters
    #     ----------
    #     volume: Hlasitost, kterou má Ministrant nastavit.
    #     """

    #     if ctx.voice_client is None:
    #         return await ctx.send("Not connected to a voice channel.")

    #     ctx.voice_client.source.volume = volume / 100
    #     await ctx.send(f"Changed volume to {volume}%")

    @commands.slash_command(
        description = "Ministrant se připojí do hlasového kanálu"
    )
    async def stop(
        self,
        inter: ApplicationCommandInteraction
        ):
        await inter.response.defer()

        embed = Embed(
            color = Colour.red()
        )
        embed.set_footer(
            text = f"Může za to {inter.author.name}"
        )

        if inter.bot.voice_clients is not None:
            for voice_client in inter.bot.voice_clients:
                await voice_client.disconnect()

                # Message reply
                embed.title = "Tož sem se odpojil."
                embed.description = "Bo mňa to prý nebavilo."
                return await inter.followup.send(
                    embed = embed
                )
        
        # Message reply
        embed.title = "Asi jsem se neodpojil."
        embed.description = "Bo sa něco dojebalo."
        await inter.followup.send(
            embed = embed
        )

    async def ensure_voice(
        self,
        inter: ApplicationCommandInteraction
        ):
        if inter.bot.voice_clients is None:
            if inter.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Nemůžu ti poslóžit, bo néseš ve zvukové místnosti.")
                raise commands.CommandError("Author not connected to a voice channel.")

def setup(bot: commands.Bot):
    bot.add_cog(Praying(bot))
