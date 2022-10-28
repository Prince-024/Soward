import discord
from discord.ext import commands
import json

class general67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<:icons8discorde64:1017404784900325406>'
		      label = "General"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def General(self, ctx: commands.Context):
       """```steal ・ afk ・ nick ・ clearnick ・ crembed ・ colors ・ vote ・ invite ・ embed ・ botlst  ・ userinfo ・ serverinfo ・ role ・ channel ・ stats ・ emoji-add ・ emoji-delete ・ enlarge ・ boosts ・ give <user> <role> ・ temp <role> <time> <user> ・ remove <user> <role> ・ deleterole <role> ・ createrole <name> ・ rename <role> <new name> ・ color <role> <color> ・ roleinfo <role> ・ revokeall ・ revokeinvites```"""
       

def setup(bot):
    bot.add_cog(general67(bot))