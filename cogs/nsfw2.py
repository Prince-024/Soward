import discord
from discord.ext import commands
import json

class nsfw2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """nsfw commands"""  

    def help_custom(self):
		      emoji = '<:nsfw:1017402520013897810>'
		      label = "NSFW"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def nsfw(self, ctx: commands.Context):
        """```n4k ・ pussy ・ boobs ・ lewd ・ lesbian ・ blowjob ・ cum ・ gasm ・ hentai```"""


def setup(bot):
    bot.add_cog(nsfw2(bot))