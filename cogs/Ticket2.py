import discord
from discord.ext import commands
import json

class invtracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<a:tic:1017405527183065158>'
		      label = "Tickets"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def TicketTool(self, ctx: commands.Context):
       """``` sendpanel ・ adduser ・ delete ・ close```"""
  

def setup(bot):
    bot.add_cog(invtracker(bot))