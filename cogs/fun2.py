import discord
from discord.ext import commands
import json

class fun67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Fun commands"""
  
    def help_custom(self):
		      emoji = '<a:ch_music:1017402433267322910>'
		      label = "Fun"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def Fun(self, ctx: commands.Context):
        """``` profile ・ source ・ coinflip [1/2] ・ blue ・ red ・ green ・ grey ・ glass ・ wasted ・ igs ・ invert ・ threshold ・ blurple ・ blur ・ sepia ・ pixelate ・ facepalm ・ simp ・ lesbo ・ emojify ・ post ・ slotmachine ・ fact ・ image ・ wink ・ pfps ・ Hug ・ Meme ・ Kiss ・ Aw ・ Avatar ・ userbanner ・ Servericon ・ Invite ・ Membercount ・ Slap ・ Pet ・ Cat ・ Advice ・ Bored ・ Inspire ・ Dance ・ Poll ・ Hack ・ Kill ・ Gay ・ Quack ・ Hack ・ Roast ・ Codestats ・ Age ・ Marry ・ Cry ・ Pokemon ・ Pikachu ・ 8ball ・ asktrump```"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(fun67(bot))