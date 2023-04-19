from disnake import ApplicationCommandInteraction, Embed
from disnake.ext import commands
from config.messages import Messages
from datetime import datetime
from dotenv import load_dotenv
import sys
import requests

load_dotenv(dotenv_path="./config/.env")


class Nepal(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.refresh_cucin_api_response()

    local_tz = datetime.now().astimezone().tzinfo

    def refresh_cucin_api_response(self):
        self.cucin_api_response = requests.get('https://obed.cucin.eu/fit/?json').json()

    def get_today_nepal_menu(self):
        self.refresh_cucin_api_response()
        if not isinstance(self.cucin_api_response, dict):
            print("Response from API is not a JSON, ending.", file=sys.stderr)
            exit(1)

        if "nepal" not in self.cucin_api_response["restaurants"].keys():
            print("There is not 'nepal' restaurant JSON response from API, ending.", file=sys.stderr)
            exit(1)

        if "dishes" not in self.cucin_api_response["restaurants"]["nepal"].keys():
            print(
                "There are not 'dishes' in nepal restaurant JSON response from API, ending.",
                file=sys.stderr
            )
            exit(1)

        return self.cucin_api_response["restaurants"]["nepal"]["dishes"]

    def format_today_nepal_menu(self):
        meals = self.get_today_nepal_menu()
        s = ""
        for meal in meals:
            if meal["number"] != "":
                s += f"**{meal['number']}.** "
            s += f"{meal['name']} *Cena:* **{meal['price']}**\n"
        return s

    @commands.slash_command(description=Messages.today_nepal_brief)
    async def today_nepal_menu(self, inter: ApplicationCommandInteraction):
        await inter.response.defer()
        nepal_menu_text = self.format_today_nepal_menu()
        nepal_embed = Embed(
            title="Dnešní meníčko v Nepal Brno",
            description=nepal_menu_text,
        )
        await inter.followup.send(
            # content=nepal_menu_text,
            embed=nepal_embed
        )


def setup(bot: commands.Bot):
    bot.add_cog(Nepal(bot))
