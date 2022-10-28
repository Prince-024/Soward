import discord
from discord.ext import commands
import json
from utilities.Tools import *
class antinuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<:security:1017403300972331108>'
		      label = "Antinuke"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    @blacklist_check()
    async def antnuke(self, ctx: commands.Context):
       """``` Antinuke enable/disable ・ Antinuke config ・ features ・ whitelist add・ whitelist remove・ whitelist show ・ whitelist reset ・ channelclean ・ roleclean ・ recover ・ punishment set ・ punishment show  ```"""
  

def setup(bot):
    bot.add_cog(antinuke(bot))