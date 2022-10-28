import discord
from discord.ext import commands
import json

class selfrole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Game commands"""

  
    def help_custom(self):
		      emoji = '<a:bolt:1018057711251902494>'
		      label = "Autoroles"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def Autorole(self, ctx: commands.Context):
        """``` autorole-human-add ・ autorole-human-remove ・ autorole-bot-add ・ autorole-bot-remove ・ autoroles-config ・ selfrole <channel> <role> ・ verification <channel> <role>```"""
       

def setup(bot):
    bot.add_cog(selfrole(bot))