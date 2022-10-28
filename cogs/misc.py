import random
import discord
from discord.ext import commands
from .utils.config import *
from discord.ui import Button, View
from discord.enums import ButtonStyle
import time 
import datetime
from utilities.Tools import*

class Buttons(View):
    def __init__(self):
        super().__init__(timeout=100)

        button1 = Button(label=f'Get Soward', style=ButtonStyle.url, url='https://discord.com/oauth2/authorize?client_id=1004248513435152484&permissions=8&scope=bot%20applications.commands', emoji='<:zenox:1006479948988567583>')
        button2 = Button(label=f'Support Server', style=ButtonStyle.url, url='https://discord.gg/z5F5YBgwX', emoji='<:zenox:1006479948988567583>')
        button3 = Button(label=f'Vote me!', style=ButtonStyle.url, url='https://top.gg/bot/1004248513435152484/vote', emoji='<:spy_icons_Discord:1005805306682560612>')
      #  button4 = Button(label=f'support', style=ButtonStyle.url, url='https://discord.gg/z5F5YBgwXH', emoji='<:support:1003339134582128771>')

        self.add_item(button1)
        self.add_item(button2)
        self.add_item(button3)
        self.add_item(button4)
        self.items = [button1, button2, button3, button4]
    
    async def on_timeout(self):
        self.items[0].disabled = True
        self.items[1].disabled = True
        self.items[2].disabled = True
        self.items[3].disabled = True

class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['nick'])
    @blacklist_check()
    @commands.has_permissions(manage_nicknames=True)
    async def changenickname(self, ctx, member: discord.Member, * , nick):
        await member.edit(nick=nick)
        await ctx.send(embed=discord.Embed(title="<:tick_right:1003345911067443241> | Successfully changed nickname", color=0x2f3136))

    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_nicknames=True)
    async def clearnick(self, ctx, member: discord.Member):
        await member.edit(nick="")
        await ctx.send(embed=discord.Embed(title="<:tick_right:1003345911067443241> | Successfully reset nickname", color=0x2f3136))

        
    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | This channel's slowmode has been set to {seconds}", color=0x2f3136))

    @commands.command(aliases=['l'])
    @blacklist_check()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(embed=discord.Embed(title=f"<:eg_lock:1018057640724660226> | {ctx.channel.mention} has been locked!", color=0x2f3136))
       # if ctx.channel.permissions_for(ctx.guild.default_role).send_messages == False:
        #    await ctx.send("This chnanel is already locked.")

    @commands.command(aliases=['unl'])
    @blacklist_check()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx: commands.Context):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(embed=discord.Embed(title=f"<:eg_unlock:1018057690154537051> | {ctx.channel.mention} has been unlocked!", color=0x2f3136))
      #  if ctx.channel.permissions_for(ctx.guild.default_role).send_messages == True:
      #      await ctx.send("This channel is already unlocked.")
      
            
    @commands.command(name="serv", aliases=["serversts", "guio", "guildss", "so"])
    @commands.guild_only()
    async def servjheinfo(self, ctx):
        "Displays server information and statistics."
     #   region = self.parseServerRegion(str(ctx.guild.region))
        info = f"""**Owner:** {ctx.guild.owner.name}
**Owner ID:** `{ctx.guild.owner.id}`
**Server ID:** `{ctx.guild.id}`
**Created At:** {ctx.guild.created_at.strftime("%A, %B %d, %Y.")}
**Roles:** {len(ctx.guild.roles)}
**Member Count:** {len([x for x in ctx.guild.members if not x.bot])} ({len([x for x in ctx.guild.members if x.bot])} bots)
**Members Online:** {len([x for x in ctx.guild.members if not str(x.status) == "offline"])}"""
        embed = discord.Embed(description=info, color=0x2f3136)
        embed.set_author(name=ctx.guild.name)
        if ctx.guild.icon.url:
            embed.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(utils(bot))