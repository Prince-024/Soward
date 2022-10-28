import discord
from discord.ext import commands
import json

class automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<:automod:1029505440054259784>'
		      label = "Automod"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def Automod(self, ctx: commands.Context):
       """``` Antispam enable/disable ・ Antilink enable/disable  ```"""
  

def setup(bot):
    bot.add_cog(automod(bot))