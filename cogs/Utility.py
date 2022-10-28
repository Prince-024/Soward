import discord
from discord.ext import commands
import json

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<:utility:1017405604987404408>'
		      label = "utility"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def Utility(self, ctx: commands.Context):
       """```calculate ・ Suggestions<sg> ・ report ・ vcdeafen ・ vcundeafen ・ vcmute ・ vcunmute ・ emoji-add ・ emoji-delete ・ createrole<name> ・ deleterole <name> ・ rename <role> <new name> ・ color <role> <color> ・ cnuke ・ hackban ・ timer```"""
  

def setup(bot):
    bot.add_cog(Utility(bot))