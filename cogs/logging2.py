import discord
from discord.ext import commands
import json

class logging67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Logging commands"""  

    def help_custom(self):
		      emoji = '<a:Loading:1017405092321824799>'
		      label = "Logging"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def Logs(self, ctx: commands.Context):
        """``` audit <parameter> ・ logging channel ・ logging config ・ logging delete```"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(logging67(bot))