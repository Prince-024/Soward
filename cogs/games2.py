import discord
from discord.ext import commands
import json

class games67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Game commands"""

  
    def help_custom(self):
		      emoji = '<a:sgames:1017404466833657918>'
		      label = "Games"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def Games(self, ctx: commands.Context):
        """``` fight ・ Findimposter ・ Rps ・ Hangman ・ TicTacToe ・ blackjack ・ truth ・ dare ・ typerace```"""
       

def setup(bot):
    bot.add_cog(games67(bot))