import discord
from discord.ext import commands
import json

class Moderation2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Moderation commands"""
  
    def help_custom(self):
		      emoji = '<a:moderation_animated:1017402486258151534>'
		      label  = "Moderation"
		      description = ""
		      return emoji, label, description  

#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def Moderation(self, ctx: commands.Context):
        """``` antispam enable/disable ・ hide ・ unhide ・ nuke ・ createchannel ・ deletechannel ・ lockserver ・ ban ・ unban ・unbanall ・ warn ・ timeout ・ mute ・ unmute ・ clear ・ lockall ・ unlockall ・ lock ・ unlock ・ hideall ・ unhideall ・ purge ・ purge contains ・ purge startswith ・ purge endswith ・ purge user ・ purge invites ・ clone ・ slowmode ・ snipe ・ nick ・ enlarge ・ giveallhumans ・ giveallbots ・ removeallhumans ・ removeallbots ・ jail ・ unjail ・ boosts ・ cleanup (Clears Bot Messages) ・ vcroles New ・ vcrole Config ・ Vcrole Delete ・ vcdeafen ・ vcundeafen ・ vcmute ・ vcunmute```"""


def setup(bot):
    bot.add_cog(Moderation2(bot))