import discord
from discord.ext import commands
import json

class j2c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<a:voice:1017402454159147039>'
		      label = "Join to create"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def Join2create(self, ctx: commands.Context):
       """``` voice setupj2c ・ voice claim ・ voice lock ・ voice unlock ・ voice permit <user> ・ voice reject <user> ・ voice name <name> ・ voice limit ( ex. 1-2-3)```"""
  

def setup(bot):
    bot.add_cog(j2c(bot))