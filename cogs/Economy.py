import discord
from discord.ext import commands
import json

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<a:cash:1017403803726778409>'
		      label = "Economy"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def eco(self, ctx: commands.Context):
       """```Bal ・ dep ・ with ・ Rob ・ Slots ・ Shop ・ Buy ・ Sell ・ Beg ・ Work ・ Rich ・ Send ```"""
  

def setup(bot):
    bot.add_cog(economy(bot))