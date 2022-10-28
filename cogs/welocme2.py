import discord
from discord.ext import commands
import json

class welcome2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<a:welcome:1017405722226610247>'
		      label = "Welcome"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def welcomes(self, ctx: commands.Context):
               """``` greet <msg> (use $$MM$$ in greet msg for member mention) ・ stopgreet ・ welcome enable ・ welcome disable ・ welcome channel ・ welcome test ・ welcome message\n\n Welcome variables ・ ++user.name++ ・ ++user.mention++ ・ ++user.id++ ・ ++user.tag++ ・ ++server.name++ ・ ++server.membercount++```"""

  

def setup(bot):
    bot.add_cog(welcome2(bot))