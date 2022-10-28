#from core.Soward import Soward
import colorama
from colorama import Fore
print(Fore.CYAN + "=======================" + Fore.RESET)
import ast
import inspect
from lib2to3.pgen2 import token
import re
from click import command
import discord, datetime
from discord.ext import commands
import os
os.system("pip install httpx")
os.system("pip install aiohttp")
#os.system("pip install wavelink")
import json
import subprocess
import asyncio
import traceback
import sys
import ast
from Errorembed import ErrorEmbed
from otherscipts.data import Data
import headers
from discord.utils import get
import os
import re
import json
from core import Context
import requests
from click import command
import discord, datetime
import pymongo
import httpx
import random
import asyncio
from utilities.Tools import* 
from discord.ext import commands, tasks
import webserver
from discord.ui import Button, View
from webserver import keep_alive
from discord.ext.commands import cooldown, BucketType
import time
from cogs.ticket import createTicket, closeTicket
#import jishaku
#bot = Soward()

#intents = discord.Intents.all()
intents = discord.Intents.all()
#intents.presences = False

default_prefix = "$"

def get_prefix(client, message):
  with open("prefixes.json", "r") as f:
    idk = json.load(f)
  with open ("nonprefix.json","r") as f:
    member = json.load(f)
  if str(message.author.id) in member["access"]:
        return ""
  elif str(message.guild.id) not in idk:
       return f"{default_prefix}"
  elif str(message.guild.id) in idk:
       idkprefix = idk[str(message.guild.id)]
       return f"{idkprefix}"

from discord.ext.commands import AutoShardedBot
OWNER_IDS = [1018139793789563000]

bot = AutoShardedBot(command_prefix=get_prefix, case_insensitive = True, intents=intents, owner_ids=OWNER_IDS, shard_count=3, allowed_mentions=discord.AllowedMentions(everyone=False, replied_user=False, roles=False), strip_after_prefix=True)
headers = {'Authorization': f'MTAwNDI0ODUxMzQzNTE1MjQ4NA.Gn9shC.zvlZHy1KrvCKB0m4WXjBBB9XvGmBzHBN3Tvcy4'}

for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')


def is_allowed(ctx):
    return ctx.message.author.id == 1018139793789563000

async def antilinks_event(message):
  duration = datetime.timedelta(minutes=5)
  with open("antilinkconf.json", "r") as f:
    conf = json.load(f)
  if str(message.guild.id) not in conf or conf[str(message.guild.id)] == "disable":
    return
  elif str(message.guild.id) in conf and conf[str(message.guild.id)] == "enable":
    if message.author.guild_permissions.manage_messages:
      return
    else:
      if "https://discord.gg/" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending server invite")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
        return
      if "discord.gg" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending server invite")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
      if "https://" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending links")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
      if "http://" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending links")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
      if "Discord.gg" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending server invite")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
        if "discord.com/invite" in message.content:
          httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
          await message.author.timeout_for(duration, reason="Sending server invite")
          await message.channel.send(f'Muted {message.author.mention} for advertising.')
          


 
@bot.command()
@commands.has_permissions(administrator=True)
async def antilink(ctx, toggle):
  with open("antilinkconf.json", "r") as f:
    idk = json.load(f)
  if toggle == "enable":
      idk[str(ctx.guild.id)] = "enable"
      await ctx.reply(embed=discord.Embed(title=f" enabled antilink ", color=0x2f3136))
  elif toggle == "disable":
      idk[str(ctx.guild.id)] = "disable"
      await ctx.reply(embed= discord.Embed(title=" Disabled antilink ", color=0x2f3136))
  else:
    await ctx.reply(embed=discord.Embed(title= f"Wrong ❌ Invalid argument, it should be enable or disable.", color=0x2f3136))
  with open('antilinkconf.json', 'w') as f:
    json.dump(idk, f, indent=4)

bot.add_listener(antilinks_event, 'on_message')
    
#@bot.event
#async def on_ready():
   ## if not bot.persistent_views_added:
    #    bot.add_view(createTicket())
  #      bot.add_view(closeTicket())
   #     bot.persistent_views_added = True
@bot.event
async def on_ready():
        bot.add_view(createTicket())
        bot.add_view(closeTicket())
        bot.add_view(selfrole2())
        bot.add_view(verificationb())
#@bot.event
#async def on_ready():
  #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.Game, name=f'{len(bot.guilds)} Guilds!'))

    

@bot.event
async def on_command_error(ctx, error):
    if type(error) == commands.MissingRequiredArgument:
        return await ctx.send(embed=discord.Embed(
                title="Error",
                description=f"You forgot to provide an argument, please do it like: `{ctx.command.name} {ctx.command.usage}`",
                color=0x2f3136))
    elif type(error) == commands.BotMissingPermissions:
        return await ctx.send(embed=discord.Embed(title=f"The bot is missing Permissions:", description=f" {', '.join(error.missing_perms)}", color=0x2f3136))
    elif type(error) == commands.MissingRole:
        return await ctx.reply(
            f"**You are missing the role: {error.missing_role}")
    elif type(error) == commands.BotMissingRole:
        return await ctx.reply(
            f"The bot is lacking the role: {error.missing_role}")
    elif type(error) == commands.CommandNotFound:
        pass  #return await ctx. rep ly("That command does not exist.")
    elif type(error) == commands.CheckFailure:
        pass #await ctx.reply("only developers use this commnd")
    elif type(error) == commands.BadArgument:
        return await ctx.reply(embed=discord.Embed(title=error, color=0x2f3136))
    else:
        await ctx.reply(embed=discord.Embed(title=error, color=0x2f3136))
        raise error


@bot.command(alasies=["antinuke-features"])
@blacklist_check()
async def features(ctx):
  em = discord.Embed(description=f"**Antinuke Events** <:eg_shield:1018057685637275670>\nMove my role above for more protection.\n\nAnti Ban\nAnti Bot \nAnti Channel create  \nAnti Channel delete: \nAnti Channel update: \nAnti Guild update \nAnti Kick \nAnti Member update \nAnti Role create \nAnti Role delete \nAnti Role update: \nAnti Webhook: \nAnti prune \nAnti integration create \nAnti Emoji create \nAnti emoji update \nAnti emoji delete \nAnti community spam \nAnti guild update ", color=0x2f3136, timestamp=ctx.message.created_at)
 
  em.set_thumbnail(url=bot.user.display_avatar.url)
  em.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
  em.set_footer(text="Made By Prince", icon_url="https://images-ext-2.discordapp.net/external/XpYSeN_4K1TG8OtzI3R3LE3zXbhvqB1rwgQkKRSs-Ww/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/980361546918162482/aa3b4e68dd27540854c0e0e3f374fe32.png")
  await ctx.send(embed=em)


@bot.event
async def on_message(message):
    
    msg = message
    prince = str("<@1018139793789563000>")
    if message.author == bot.user or message.author.bot:
    	return
    if prince in message.content:
             	await msg.add_reaction("<a:azZ_kiddosleep:934674720782159932>")
             	await msg.add_reaction("<a:azzzzzzz_thory_kiddo_heart:934674783180828682>")
             	await msg.add_reaction("<a:paisa:934531098849968138>")
#    await blacklist(message)
    await bot.process_commands(message)

         
@bot.command()
@blacklist_check()
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, member: discord.Member, reason=None):
    author = ctx.message.author
    if reason is None:
       reason = f"action done by {ctx.author.name}"
    await member.remove_timeout()
    await member.send(f":exclamation: | You are have been unmuted from: {ctx.guild.name} by {ctx.author.name}")
    await ctx.send(f"{member.name} successfully unmuted")
    
    

@bot.command()
@commands.is_owner()
async def guild(ctx, id: int):
  guild = bot.get_guild(id)
  guildname = guild.name
  guildid = guild.id
  guildowner = guild.owner.name
  guildmembers = guild.member_count
  embed = discord.Embed(title=f"guild info",description=f"```guild =  {guild.name}\n guild id = {guildid}\n Owner =  {guildowner}\n members =  {guildmembers}```",color=ctx.author.color)
  await ctx.reply(embed=embed,mention_author=False)


@bot.command()
@blacklist_check()
async def n4k(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/4k")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed()
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
@blacklist_check()
async def pussy(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/pussy")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
@blacklist_check()
async def boobs(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/boobs")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
@blacklist_check()
async def lewd(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/lewd")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
@blacklist_check()
async def lesbian(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/lesbian")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
@blacklist_check()
async def blowjob(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/blowjob")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
@blacklist_check()
async def cum(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/cum")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
@blacklist_check()
async def gasm(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/gasm")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
@blacklist_check()
async def hentai(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/hentai")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)


def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 1018139793789563000 or ctx.message.author.id == 980361546918162482










intents = discord.Intents.default()
intents.members = True
with open('badges.json') as f:
  
 owner = [980361546918162482,1018139793789563000]


badgesgiver = [980361546918162482,925246550018519040,940973004647718912,971301161678290964,969991261048164352,1018139793789563000,984815117730480228,990643162928279592]

@bot.command(aliases=["addb"])
#@commands.is_owner()
async def addbadge(ctx, user: discord.Member, *, badge):
  if ctx.author.id in badgesgiver:
    with open("badges.json", "r") as f:
      idk = json.load(f)
    if str(user.id) not in idk:
      idk[str(user.id)] = []
      idk[str(user.id)].append(f"{badge}")
      await ctx.reply(embed=discord.Embed(title=f" Added badge {badge} to {user}.",  color=0x2f3136))
    elif str(user.id) in idk:
      idk[str(user.id)].append(f"{badge}")
      await ctx.reply(embed=discord.Embed(title=f" Added badge {badge} to {user}.",color=0x2f3136))
    with open("badges.json", "w") as f:
      json.dump(idk, f, indent=4)


@bot.command(aliases=["profile"])
@blacklist_check()
async def badges(ctx, user: discord.Member=None):
  user = user or ctx.author
  with open("badges.json", "r") as f:
    idk = json.load(f)
  if str(user.id) not in idk:
    await ctx.reply(embed=discord.Embed(description=f"{user} Have no badges join [support server](https://discord.gg/k6YNHy36JJ) to get some badges.",color=0x2f3136), mention_author=False)
  elif str(user.id) in idk:
    embed = discord.Embed(color=discord.Colour(0x2f3136),title="<a:hypesquad:1017430505353904128> Soward Achivement <a:hypesquad:1017430505353904128> ",description=f"{user.mention} badges\n\n"   
 )
    for bd in idk[str(user.id)]:
      embed.description += f"{bd}\n"
    embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
    embed.set_thumbnail(url=user.display_avatar.url)
    await ctx.reply(embed=embed, mention_author=False)

#@badges.error
#async def badges_error(ctx, error):
    #    if isinstance(error, commands.CommandInvokeError):
   #             await ctx.send(embed=discord.Embed(title='put pfp and try again later', color=0xab280e))

@bot.command(aliases=['rb'])
#@commands.is_owner()
async def removebadge(ctx, user: discord.User = None):       
  if ctx.author.id in badgesgiver:
    if user is None:
        await ctx.reply(embed=discord.Embed(title="You must specify a user to remove badge.", color=0x2f3136))
        return
    with open('badges.json', 'r') as f:
        badges = json.load(f)
    try:
        if str(user.id) in badges:
            badges.pop(str(user.id))

            with open('badges.json', 'w') as f:
                json.dump(badges, f, indent=4)

            await ctx.reply(embed=discord.Embed(title=f"Removed badge of {user}", color=0x2f3136))
    except KeyError:
        await ctx.reply("This user has no badge.")

class verificationb(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Verify',
                       style=discord.ButtonStyle.green,
                       custom_id=f'verifybutton')
    async def button_callback(self, button, interaction: discord.Interaction):
        with open("verification.json", "r") as f:
            idk = json.load(f)
        role_id = idk[str(interaction.guild.id)]["role"]
        role = interaction.guild.get_role(role_id)
        try:
            await interaction.user.add_roles(role, reason="Verification")
            await interaction.response.send_message(f" successfully verified",
                                                    ephemeral=True)
        except:
            await interaction.response.send_message(f"failed to verify",
                                                    ephemeral=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def verification(ctx, verification_channel: discord.TextChannel,
                       verified_role: discord.Role):
    with open("verification.json", "r") as f:
        idk = json.load(f)
    mm = {"channel": verification_channel.id, "role": verified_role.id}
    idk[str(ctx.guild.id)] = mm
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136),
                                        description=f"successfully setuped"))
    embed=discord.Embed(title="<a:Error:1018257469274861688> Verification Required <a:Error:1018257469274861688>", description=f"<a:verify:1033811571031408732> To access **{ctx.guild.name}**\n     <a:verify:1033811571031408732> you need to pass the verification first\n Press the verify button below.", timestamp=ctx.message.created_at, color=0x2f3136)
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
    await verification_channel.send(embed=embed, view=verificationb())
   # await verification_channel.send(embed=discord.Embed(
    #    color=discord.Colour(0x2f3136),
   #     description=
 #       f"To access {ctx.guild.name}, you need to pass the verification first, Press the verify button below.",
   #     title=f"Verification").set_footer(text=bot.user.name,
   #                                       icon_url=bot.user.avatar),
   #                                 view=verificationb())
    with open('verification.json', 'w') as f:
        json.dump(idk, f, indent=4)
      
class selfrole2(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(label='GetRole', style=discord.ButtonStyle.green, custom_id=f'ReactionRole')
  async def button_callback(self, button, interaction: discord.Interaction):
   with open("randx.json", "r") as f:
    idk = json.load(f)
   role_id = idk[str(interaction.guild.id)]["role"]
   role = interaction.guild.get_role(role_id)
   try:
      await interaction.user.add_roles(role, reason="ReactionRole")
      await interaction.response.send_message(f" Successfully Added", ephemeral=True)
   except:
       await interaction.response.send_message(f"Failed to Add", ephemeral=True)


@bot.command()
@commands.has_permissions(administrator=True)
async def selfrole(ctx, selfrole_channel:discord.TextChannel, self_role:discord.Role):
    with open("randx.json", "r") as f:
          idk = json.load(f)
    mm = {"channel": selfrole_channel.id, "role": self_role.id}
    idk[str(ctx.guild.id)] = mm
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"successfully setuped"))
    embed=discord.Embed(title="Self Role!", description=f"To get the roles,Click on button below \n\n<a:bolt:1018057711251902494> - {self_role.mention}", timestamp=ctx.message.created_at, color=0x2f3136)
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
    await selfrole_channel.send(embed=embed, view=selfrole2())
  #  await selfrole_channel.send(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"To get the roles,Click on button below \n\n<a:bolt:1018057711251902494> - {self_role.mention}\n\nThanku for using me", title=f"Role Menu").set_footer(text=bot.user.name, icon_url=bot.user.avatar), view=selfrole2())
    with open('randx.json', 'w') as f:
      json.dump(idk, f, indent=4)

def json_loda():
  with open('roles.json', 'r') as f:
    pp = json.load(f)
  for guild in client.guilds:
    if not str(guild.id) in pp:
      pp[str(guild.id)] = {"humanautoroles": [], "botautoroles": []}
    with open('roles.json', 'w') as f:
      json.dump(pp, f, indent=4)

@bot.listen("on_guild_join")
async def dexter_balak(guild):
  with open('roles.json', 'r') as f:
    pp = json.load(f)
  if guild:
    if not str(guild.id) in pp:
      pp[str(guild.id)] = {"humanautoroles": [], "botautoroles": []}
    with open('roles.json', 'w') as f:
      json.dump(pp, f, indent=4)

@bot.listen("on_member_join")
async def autorolessacks(member):
  if member.id == bot.user.id:
    return
  else:
    gd = member.guild
    with open('roles.json') as f:
      idk = json.load(f)
    g_ = idk.get(str(member.guild.id))
    human_autoroles = g_['humanautoroles']
    bot_autoroles = g_['botautoroles']
    if human_autoroles == []:
      pass
    else:
      for role in human_autoroles:
        rl = gd.get_role(int(role))
        if not member.bot:
          await member.add_roles(rl, reason="Soward | Autorole")
    if bot_autoroles == []:
      pass
    else:
      for rol in bot_autoroles:
        rml = gd.get_role(int(rol))
        if member.bot:
          await member.add_roles(rml, reason="Soward | Autorole")

@bot.command(name="autorole-bot-add")
@commands.has_permissions(administrator=True)
async def botautoroleidk(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if str(role.id) in omk['botautoroles']:
      await ctx.reply(embed=discord.Embed(title="That role is already set in autoroles.", color=0x2f3136))
      return
    else:
      ff[str(ctx.guild.id)]['botautoroles'].append(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(embed=discord.Embed(title="successfully Added Bot autoroles.",color=0x2f3136))

@bot.command(name="autorole-human-add")
@commands.has_permissions(administrator=True)
async def humanautoroleidk(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
    await ctx.reply(embed=discord.Embed(title="you must have role above me to use this cmd.", color=0x2f3136))
    return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if str(role.id) in omk['humanautoroles']:
      await ctx.reply(embed=discord.Embed(title="That role is already set in autoroles.", color=0x2f3136))
      return
    else:
      ff[str(ctx.guild.id)]['humanautoroles'].append(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(embed=discord.Embed(title="Added that role to autoroles.", color=0x2f3136))

@bot.command(name="autorole-bot-remove")
@commands.has_permissions(administrator=True)
async def botarmutoroleidk(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if not str(role.id) in omk['botautoroles']:
      await ctx.reply(embed=discord.Embed(title="That role is not set in autoroles.", color=0x2f3136))
      return
    else:
      ff[str(ctx.guild.id)]['botautoroles'].remove(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(embed=discord.Embed(title="Removed that role from  autoroles.", color=0x2f3136))

@bot.command(name="autorole-human-remove")
@commands.has_permissions(administrator=True)
async def humanautoroleidkrm(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if not str(role.id) in omk['humanautoroles']:
      await ctx.reply(embed=discord.Embed(title="That role is not set in autoroles.", color=0x2f3136))
      return
    else:
      ff[str(ctx.guild.id)]['humanautoroles'].remove(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(embed=discord.Embed(title="Removed that role from autoroles.", color=0x2f3136))
@bot.command(name="autorole-config")
@commands.has_permissions(administrator=True)
async def auto_rolshow(ctx):
  print("juice")
  with open('roles.json', 'r') as f:
    ok = json.load(f)
  g = ok.get(str(ctx.guild.id))
  human_autoroles = g['humanautoroles']
  bot_at = g['botautoroles']
  if human_autoroles == [] and bot_at == []:
    await ctx.reply("No Autoroles set for this guild.")
    return
  else:
    if human_autoroles == []:
      human_autoroles.append("No Human Auto-Roles.")
    if bot_at == []:
      bot_at.append("No Bot Auto-Roles.")
    embed = discord.Embed(title="Autoroles")
    embed.add_field(name="Human Auto-Roles", value="\n".join(human_autoroles))
    embed.add_field(name="Bot Auto-Roles", value="\n".join(bot_at))
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.reply(embed=embed)
owners =[980361546918162482,925246550018519040,940973004647718912,971301161678290964,969991261048164352,1018139793789563000,984815117730480228,990643162928279592]
  
@bot.command(aliases=["nopre"])
#@commands.is_owner()
async def np(ctx, type=None, mem: discord.Member = None):
  if ctx.author.id not in owners:
    await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You don't have access to this command !", color=0x2f3136),mention_author=False)
    return
  else:
    if type == None:
      await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'Type' argument", color=0x2f3136),mention_author=False)
      return
    if type == "add":
      if mem == None:
        await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'Member' argument", color=0x2f3136),mention_author=False)
        return
      else:
        with open ("nonprefix.json","r") as f:
          member = json.load(f)
          if str(mem.id) in member["access"]:
            await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | The mentioned member is already added!", color=0x2f3136),mention_author=False)
            return
          else:
            member["access"].append(str(mem.id))
            with open ("nonprefix.json","w") as f:
              json.dump(member,f)
            await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> |  successfully added {mem.name} to noprefix !", color=0x2f3136),mention_author=False)
    if type == "remove":
      if mem == None:
        await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'Member' argument", color=0x2f3136),mention_author=False)
        return
      else:
        with open ("nonprefix.json","r") as f:
          member = json.load(f)
          if str(mem.id) not in member["access"]:
            await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | The mentioned member is already absent!", color=0x2f3136),mention_author=False)
            return
          else:
            member["access"].remove(str(mem.id))
            with open ("nonprefix.json","w") as f:
              json.dump(member,f)
            await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | {mem.name} is successfully removed from noprefix!", color=0x2f3136),mention_author=False) 
    if type == "list":
      embed = discord.Embed(title=f"Non Prefix Users", description="")
      with open ('nonprefix.json', 'r') as i:
        mem = json.load(i)
      try:
        for u in mem["access"]:
          user = await bot.fetch_user(u)
          embed.description += f"{user.name}\n"
          embed.title = "Non Prefix Users "
        await ctx.reply(embed = embed,mention_author=False)
      except KeyError:
        await ctx.send("No user is added to Non-Prefix")



  

        


cd = commands.CooldownMapping.from_cooldown(7, 10, commands.BucketType.user)        

@bot.listen("on_message")
async def antispamm_event(message):
  with open("antispamconf.json", "r") as f:
    idk = json.load(f)
  bucket = cd.get_bucket(message)
  retry = bucket.update_rate_limit()
  if retry:
    if str(message.guild.id) not in idk or idk[str(message.guild.id)] == "disable":
      return
    elif str(message.guild.id) in idk and idk[str(message.guild.id)]== "enable":
      if message.author.guild_permissions.manage_messages:
          return
      else:
        if message.author.id != bot.user.id:
          duration = datetime.timedelta(minutes=10)
          await message.author.timeout_for(duration, reason="Soward | antispam")
          await message.channel.send(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f'Muted {message.author.mention} for spamming.'))

@bot.command()
@blacklist_check()
@commands.has_permissions(administrator=True)
async def antispam(ctx, toggle):
  with open("antispamconf.json", "r") as f:
    idk = json.load(f)
  if toggle == "enable":
      idk[str(ctx.guild.id)] = "enable"
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"Enabled anti spam"))
  elif toggle == "disable":
      idk[str(ctx.guild.id)] = "disable"
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"Disabled anti spam"))
  else:
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"Invalid argument, it should be enable / disable."))
  with open('antispamconf.json', 'w') as f:
    json.dump(idk, f, indent=4)



         
@bot.command()
@blacklist_check()
async def enlarge(ctx , emoji: discord.PartialEmoji = None):
  embed = discord.Embed(title = f"Emoji Name | {emoji.name}" , color = 0x2f3136)
  embed.set_image(url=  f'{emoji.url}')
  embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.display_avatar.url}")
  embed.set_footer(text="Made By Prince" , icon_url="https://images-ext-2.discordapp.net/external/XpYSeN_4K1TG8OtzI3R3LE3zXbhvqB1rwgQkKRSs-Ww/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/980361546918162482/aa3b4e68dd27540854c0e0e3f374fe32.png")
  await ctx.send(embed = embed)

@bot.command(aliases=["banned", "bannedusers", "listbans"])
@commands.has_permissions(ban_members=True)
async def banlist(ctx):
    list = ctx.guild.bans()
    banned = ""
    count = 0

    if len(list) > 0:
        for ban in list:
            user = ban.user

            count += 1
            banned += f"\n{count} Banned user(s)\nName(s): {user.name}#{user.discriminator}\nuser id(s){user.id}\n\n"
        embed1 = discord.Embed(title=f'Terminal', url =f"{invitelink}",description =banned, color=0x2f3136)
        embed1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed1) 
    else:
        embed2 = discord.Embed(title=f'Soward', url =f'{invitelink}',description ="There are no banned users for this guild", color=0x2f3136)
        embed2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.display_avatar.url)
    
        await ctx.send(embed = embed2)
      

@bot.command(aliases=["joinpos"])
@blacklist_check()
async def joinposition(ctx, member: discord.Member=None):
        if not member:
                member = ctx.message.author 
        bc = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        mc = str(bc.index(member)+1)
        await ctx.reply(mc)
     #   await ctx.reply(embed=ok)


@bot.command(aliases=['mc'])
@blacklist_check()
async def membercount(ctx):
  user_count = len([x for x in ctx.guild.members if not x.bot])
  online = len(list(filter(lambda m: str(m.status)=="online", ctx.guild.members)))
  idle = len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members)))
  dnd = len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members)))
  offline = len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))
  t_online = [online, idle, dnd]
  Sum = sum(t_online)
  mbed=discord.Embed(title="Membercount", description=f"**Total Members = {ctx.author.guild.member_count} \n Users = {user_count} \n Bots = {ctx.author.guild.member_count - user_count} \n Total Online = {Sum} \n Online status = {online} \n Idle status = {idle} \n Dnd status = {dnd} \n Offline = {offline}**", color=0x2f3136)
  mbed.set_author(name=ctx.guild.name, icon_url=ctx.author.display_avatar.url)
  mbed.set_thumbnail(url=ctx.guild.icon)
  mbed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
  await ctx.send(embed=mbed)










    

    

    
@bot.command(aliases=['fuckoff', 'jana',"getlost","ghumkeaa"])
@commands.has_permissions(ban_members=True)
@blacklist_check()
async def hackban(ctx, userid="Nonexd",reason="None specified"):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    else:
        user = await bot.fetch_user(int(userid))
        await ctx.guild.ban(user,reason=reason)
    embed=discord.Embed(title="Soward", description=f"\n<:Icons_correct:1017402689027592222> | Banned :  {user.name}#{user.discriminator}\n ID -{userid}", color=0x2f3136,timestamp=ctx.message.created_at)
  #          embed.set_thumbnail(url=ctx.aut.display.avatar_url)
    embed.set_footer(text="Soward")
    await ctx.send(embed=embed)


def read_json():
    with open(f"database.json", "r") as file:
        data = json.load(file)
    return data


def write_json(data):
    with open(f"database.json", "w") as file:
        json.dump(data, file, indent=4)
        file.close()

database = {}
database.update(read_json())

welcm = database["welcm"]

@bot.command(aliases=["greet"])
@commands.has_permissions(manage_channels=True)
async def set_greet(ctx,*,msg=None):
	if msg == None:
		await ctx.send(embed=discord.Embed(title="pls provide msg !!", color=0x2f3136))
		return
	if not "$$MM$$" in msg:
		await ctx.reply(f"**use member mention \n example:** \n `greet heyy!! $$MM$$ welcome to {ctx.guild.name} server !!`  ")
	else:
		try:
			
			if not str(ctx.guild.id) in welcm.keys():
				welcm.update({f"{ctx.guild.id}":{f"{ctx.channel.id}":f"{msg}"}})
			db = welcm[str(ctx.guild.id)]
			wlcm = ({f"{ctx.channel.id}":f"{msg}"})
			
			db.update(wlcm)
			write_json(database)
			await ctx.send(embed=discord.Embed(title="successfully set welcome msg !!", color=0x2f3136))
			await ctx.message.delete()
		except:
			pass

@bot.command(aliases=["stopgreet"])
@commands.has_permissions(manage_channels=True)
async def stop_greet(ctx):
	if not str(ctx.guild.id) in welcm.keys():
		await ctx.send(embed=discord.Embed(title="in this server not set welcome message !!", color=0x2f3136))
		return
	elif not str(ctx.channel.id) in welcm[str(ctx.guild.id)].keys():
		await ctx.send(embed=discord.Embed(title="welcome message not set in this channel.", color=0x2f3136))
		return
	else:
		try:
			
			db = welcm[str(ctx.guild.id)]
			db.pop(f"{ctx.channel.id}")
			write_json(database)
			await ctx.send(embed=discord.Embed(title="stop welcome message in this channel.", color=0x2f3136))
			await ctx.message.delete()
		except:
			pass

@bot.event
async def on_member_join(member):
	if str(member.guild.id) in welcm.keys():
		for x in welcm[str(member.guild.id)].keys():
			ch = member.guild.get_channel(int(x))
			msg = welcm[str(member.guild.id)][x]
			m = msg.replace("$$MM$$", f"{member.mention}")
			try:
				await ch.send(m , delete_after=10)
			except:
				pass

start_time = datetime.datetime.utcnow()

import time 
import datetime
start_time = time.time()

@bot.command(aliases=["up"])
@blacklist_check()
async def uptime(ctx):
  current_time = time.time()
  difference = int(round(current_time - start_time))
  uptime = str(datetime.timedelta(seconds=difference))
  await ctx.reply(embed=discord.Embed(title=uptime, color=0x2f3136))


    

@bot.command(aliases=["bld"])
async def blacklisted(ctx, type=None, mem: discord.Member = None):
    embed = discord.Embed(title=f"blacklisted Users", description="")
    with open ('blacklist.json', 'r') as i:
        mem = json.load(i)
        try:
            for u in mem["ids"]:
                user = await bot.fetch_user(u)
                embed.description += f"{user.name}\n"
                embed.title = "blacklisted users "
                await ctx.reply(embed = embed,mention_author=False)
        except KeyError:
            await ctx.send("No blacklisted users found")

@bot.command()
@commands.is_owner()
async def bl(ctx: Context, member: discord.Member):
    try:
      with open('blacklist.json', 'r') as bl:
        blacklist = json.load(bl)
        if str(member.id) in blacklist["ids"]:
          embed = discord.Embed(title="Error!", description=f"{member.name} is already blacklisted", color=discord.Colour(0x2f3136))
          await ctx.reply(embed=embed, mention_author=False)
        else:
          add_user_to_blacklist(member.id)
          embed = discord.Embed(title="Blacklisted", description=f"Successfully Blacklisted {member.name}", color=discord.Colour(0x2f3136))
          with open("blacklist.json") as file:
              blacklist = json.load(file)
              embed.set_footer(
                text=f"There are now {len(blacklist['ids'])} users in the blacklist"
            )
              await ctx.reply(embed=embed, mention_author=False)
    except:
              embed = discord.Embed(
                title="Error!",
                description=f"An Error Occurred",
                color=discord.Colour(0x2f3136)
            )
              await ctx.reply(embed=embed, mention_author=False)

@bot.command()
@commands.is_owner()
async def bremove(ctx: Context, member: discord.Member = None):
    try:
      remove_user_from_blacklist(member.id)
      embed = discord.Embed(
                title="User removed from blacklist",
                description=f"**<:Icons_correct:1017402689027592222> | {member.name}** has been successfully removed from the blacklist",
                color=discord.Colour(0x2f3136)
            )
      with open("blacklist.json") as file:
        blacklist = json.load(file)
        embed.set_footer(
                text=f"There are now {len(blacklist['ids'])} users in the blacklist"
            )
        await ctx.reply(embed=embed, mention_author=False)
    except:
        embed = discord.Embed(
                title="Error!",
                description=f"**{member.name}** is not in the blacklist.",
                color=discord.Colour(0x2f3136)
            )
        await ctx.reply(embed=embed, mention_author=False)






@bot.command()
@blacklist_check()
async def pfps(ctx):
  a = requests.get('https://api.ihatehaters.repl.co/api/gif/pfps?format=text').text
  b = a.replace('"','')
  await ctx.send(b)


            
mainshop = [{"name":"Watch","price":100,"description":"Time <:watchtool:1019456724962385930>"},
            {"name":"Laptop","price":1000,"description":"Work <:Laptop:1019456878650069002>"},
            {"name":"PC","price":10000,"description":"Gaming <:PC:1019456969695838269>"},
            {"name":"Ferrari","price":99999,"description":"Sports Car <:ferrari:1019456103483981865>"}]

@bot.command(aliases=['bal'])
@blacklist_check()
async def balance(ctx):
    author = ctx.message.author
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance',color = discord.Color(0x2f3136))
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name='Bank Balance',value=bank_amt)
    em.set_thumbnail(url=author.display_avatar.url)
    await ctx.send(embed= em)


@bot.command()
@blacklist_check()
@commands.cooldown(1, 600, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(embed=discord.Embed(title="begging!", description=f"{ctx.author.mention} Got {earnings} coins!", color=0x2f3136))

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)

@bot.command()
@blacklist_check()
@commands.cooldown(1, 600, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(embed=discord.Embed(title="Working!", description=f"{ctx.author.mention} earned {earnings} coins!!", color=0x2f3136))

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)

@work.error
async def work_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@beg.error
async def beg_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))                
      

@bot.command(aliases=['with'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send(embed=discord.Embed(title="Please enter the amount", color=0x2f3136))
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send(embed=discord.Embed(title="You do not have sufficient balance", color=0x2f3136))
        return
    if amount < 0:
        await ctx.send(embed=discord.Embed(title="Amount must be positive!", color=0x2f3136))
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(embed=discord.Embed(title="withdraw", description=f"{ctx.author.mention} You withdraw {amount} coins", color=0x2f3136))

@bot.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send(embed=discord.Embed(title="Please enter the amount", color=0x2f3136))
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send(embed=discord.Embed(title="You do not have sufficient balance", color=0x2f3136))
        return
    if amount < 0:
        await ctx.send(embed=discord.Embed(title="Amount must be positive!", color=0x2f3136))
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(embed=discord.Embed(title=f"{ctx.author.mention} You deposited {amount} coins", color=0x2f3136))

@bot.command(aliases=['sn'])
@blacklist_check()
@commands.cooldown(1, 60, commands.BucketType.user)
async def send(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send(embed=discord.Embed(title="Please enter the amount", color=0x2f3136))
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send(embed=discord.Embed(title="You do not have sufficient balance", color=0x2f3136))
        return
    if amount < 0:
        await ctx.send(embed=discord.Embed(title="Amount must be positive!", color=0x2f3136))
        return

    await update_bank(ctx.author,-1*amount,'bank')
    await update_bank(member,amount,'bank')
    await ctx.send(embed=discord.Embed(title=f"{ctx.author.mention} You gave {member} {amount} coins", color=0x2f3136))

@send.error
async def send_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command(aliases=['ro'])
@blacklist_check()
@commands.cooldown(1, 30, commands.BucketType.user)
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send(embed=discord.Embed(title="It is useless to rob him!", color=0x2f3136))
        return

    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    await ctx.send(embed=discord.Embed(title=f'{ctx.author.mention} You robbed {member} and got {earning} coins', color=0x2f3136))

@rob.error
async def rob_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command()
@blacklist_check()
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send(embed=discord.Embed(title="Please enter the amount", color=0x2f3136))
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send(embed=discord.Embed(title="You do not have sufficient balance", color=0x2f3136))
        return
    if amount < 0:
        await ctx.send(embed=discord.Embed(title="Amount'Amount must be positive!", color=0x2f3136))
        return
    final = []
    for i in range(3):
        a = random.choice(['S', 'W', 'R', 'D'])

        final.append(a)

    await ctx.send((final))
    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await ctx.reply(embed=discord.Embed(title=f'You won :) {ctx.author.name}', color=0x2f3136))
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.reply(embed=discord.Embed(title=f'You lose :( {ctx.author.name}', color=0x2f3136))


@bot.command()
@blacklist_check()
async def shop(ctx):
    em = discord.Embed(title = "Shop", color = discord.Colour(0x2f3136))

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)

@bot.command()
@blacklist_check()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send(embed=discord.Embed(title="That Object isn't there!", color=0x2f3136))
            return
        if res[1]==2:
            await ctx.send(embed=discord.Embed(title=f"You don't have enough money in your wallet to buy {amount} {item}", color=0x2f3136))
            return


    await ctx.send(embed=discord.Embed(title=f"You just bought {amount} {item}", color=0x2f3136))


            
@bot.command(aliases=["items"])
@blacklist_check()
async def inventory(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "inventory", color = discord.Colour(0x2f3136))
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)
        em.set_thumbnail(url=user.display_avatar.url)

    await ctx.send(embed = em)


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@bot.command()
@blacklist_check()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send(embed=discord.Embed(title="That Object isn't there!", color=0x2f3136))
            return
        if res[1]==2:
            await ctx.send(embed=discord.Embed(title=f"You don't have {amount} {item} in your bag", color=0x2f3136))
            return
        if res[1]==3:
            await ctx.send(embed=discord.Embed(title=f"You don't have {item} in your inventory", color=0x2f3136))
            return

    await ctx.send(embed=discord.Embed(title=f"You just sold {amount} {item}", color=0x2f3136))

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 1* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]


@bot.command(aliases = ["rich"])
@blacklist_check()
async def richest(ctx,x = 5):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0x2f3136))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member
        em.add_field(name = f"{index}. **{name}**" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)

@bot.command()
@blacklist_check()
async def xdjsjah(ctx):
    author = ctx.message.author
        
    b = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://top.gg/bot/1004248513435152484/vote')
    b2 = Button(label='invite me', style=discord.ButtonStyle.link,url='https://discord.com/oauth2/authorize?client_id=1004248513435152484&permissions=1101052116095&scope=applications.commands%20bot')
    b3 = Button(label='support', style=discord.ButtonStyle.link,url='https://discord.gg/d9XQyHZKBB')
    view = View()
    view.add_item(b)
    view.add_item(b2)
    view.add_item(b3)

    embed=discord.Embed(title="Help", description="The commands you can use are below", color=0x2f3136)
    embed.add_field(name="bal", value="Check your bank balance.", inline=False)
    embed.add_field(name="beg", value="Beg for coins. ", inline=False)
    embed.add_field(name="with <amount>", value="Withdraw money into your wallet.", inline=False)
    embed.add_field(name="dep", value="Deposit money into the bank.", inline=False)
    embed.add_field(name="send <@member> <amount>", value="Send someone money.", inline=False)
    embed.add_field(name="rob <@member>", value="Rob some dude.", inline=False)
    embed.add_field(name="slots <amount>", value="Slots.", inline=False)
    embed.add_field(name="`shop", value="Buy some stuff", inline=False)
    embed.add_field(name="buy <item>", value="Buy something from the shop. for now, you can only buy 1 item at a time.", inline=False)
    embed.add_field(name="bag", value="Check your inventory.", inline=False)
    embed.add_field(name="sell <item>", value="Sell any item you own. for now, you can only sell 1 item at once", inline=False)
    embed.add_field(name="rich", value="View the richest users.", inline=False)


    embed.set_footer(text="hope you enjoy ")
    embed.set_thumbnail(url=author.display_avatar.url)
    await ctx.send(embed=embed, view=view)

#----------------------------------------------------

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def ticdelete(ctx):
  await ctx.send(f" | deleting {ctx.channel.mention} in 1sec.")
  await asyncio.sleep(1)
  await ctx.channel.delete()

@ticdelete.error
async def delete_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply("<:Wrong:1017402708703064144> | You are missing Administrator permission(s) to run this command.", mention_author=False)

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def adduser(ctx, member: discord.Member, channel=None):
  channel = channel or ctx.channel
  guild = ctx.guild
  overwrite = channel.overwrites_for(member)
  overwrite.view_channel = True
  await ctx.channel.set_permissions(member, overwrite=overwrite)
  await ctx.reply(f"Successfully added {member.mention} to {channel}", mention_author=False)
  
@adduser.error
async def adduser_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"Uses | `adduser <member id>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("<:Wrong:1017402708703064144> | You are missing Administrator permission(s) to run this command.", mention_author=False)
    
@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def close(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(
        f'<:Icons_correct:1017402689027592222> | Successfully closed {ctx.channel.mention}', mention_author=False
    )
@close.error
async def close_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
        await ctx.reply("<:Wrong:1017402708703064144> | You are missing Administrator permission(s) to run this command.", mention_author=False)

@bot.command()
@blacklist_check()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send('joined')
@bot.command()
@blacklist_check()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send('leaved')
@bot.command()
@commands.has_permissions(administrator = True)
@blacklist_check()
async def voicemove(ctx, channel : discord.VoiceChannel = None):
  if channel == None:
    await ctx.reply('Mention a channel to move users to!')
  if ctx.author.voice:    
    channell = ctx.author.voice.channel
    members = channell.members
    for m in members:
      await m.move_to(channel)
    await ctx.reply(f"Moved all users to {channel.mention}")
  if ctx.author.voice is None:
    await ctx.reply('You need to be connected to the channel from where you want to move everyone.')


@commands.cooldown(1, 30, commands.BucketType.user)
@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
@bot.command()
@blacklist_check()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def unbanall(ctx):
      button = Button(label="Yes", style=discord.ButtonStyle.green, emoji="<:Icons_correct:1017402689027592222>")
      button1 = Button(label="No", style=discord.ButtonStyle.red, emoji="<:Wrong:1017402708703064144>")
      async def button_callback(interaction: discord.Interaction):
        a = 0
        if interaction.user == ctx.author:
          if interaction.guild.me.guild_permissions.ban_members:
            await interaction.response.edit_message(content=f"Unbanning All Banned Member(s)", embed=None, view=None)
            async for idk in interaction.guild.bans(limit=None):
              await interaction.guild.unban(user=idk.user, reason="Unbanall Command Executed By: {}".format(ctx.author))
              a += 1

            
            await interaction.channel.send(content=f"<:Icons_correct:1017402689027592222> | Successfully Unbanned {a} Member(s)")
          else:
            await interaction.response.edit_message(content="I am missing ban members permission.\ntry giving me permissions and retry", embed=None, view=None)
        else:
          await interaction.response.send_message("This is not for you ", embed=None, view=None, ephemeral=True)
      async def button1_callback(interaction: discord.Interaction):
        if interaction.user == ctx.author:
          await interaction.response.edit_message(content="Ok I will not unban anyone in this guild", embed=None, view=None)
        else:
          await interaction.response.send_message("This is not for you ", embed=None, view=None, ephemeral=True)
   # if ctx.guild.me.guild_permissions.ban_members:
      embed = discord.Embed(title='Confirmation',
                          color=0x2f3136,
                          description=f'**Are you sure you want to unban everyone in this guild?**')
      view = View()
      button.callback = button_callback
      button1.callback = button1_callback
      view.add_item(button)
      view.add_item(button1)
      await ctx.reply(embed=embed, view=view, mention_author=False)

@unbanall.error
async def unbanall_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command(aliases=["log", "audit", "audit-logs", "audit-log", "auditlogs"])
@commands.has_permissions(view_audit_log=True)
@blacklist_check()
@commands.cooldown(1, 12, commands.BucketType.user)
@commands.guild_only()
async def auditlog(ctx, lmt:int):
  if lmt >= 31:
     await ctx.reply("Action rejected, you are not allowed to fetch more than `30` entries.", mention_author=False)
     return
  idk = []
  str = ""
  async for entry in ctx.guild.audit_logs(limit=lmt):
    idk.append(f'''User: `{entry.user}`
Action: `{entry.action}`
Target: `{entry.target}`
Reason: `{entry.reason}`\n\n''')
  for n in idk:
       str += n
  str = str.replace("AuditLogAction.", "")
  embed = discord.Embed(title=f"AUDIT LOGS", description=f">>> {str}", color=0x2f3136)
  embed.set_footer(text=f"Audit Log Actions")
  await ctx.reply(embed=embed, mention_author=False)

@auditlog.error
async def auditlog_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command()
@blacklist_check()
async def roleinfo(ctx, role: discord.Role = None):
  riembed = discord.Embed(title=f"**{role.name}'s Information**", colour=discord.Colour(0x2f3136))
  perms = ""
  if role.permissions.administrator:
            perms += "Administrator, "
  if role.permissions.create_instant_invite:
            perms += "Create Instant Invite, "
  if role.permissions.kick_members:
            perms += "Kick Members, "
  if role.permissions.ban_members:
            perms += "Ban Members, "
  if role.permissions.manage_channels:
            perms += "Manage Channels, "
  if role.permissions.manage_guild:
            perms += "Manage Guild, "
  if role.permissions.add_reactions:
            perms += "Add Reactions, "
  if role.permissions.view_audit_log:
            perms += "View Audit Log, "
  if role.permissions.read_messages:
            perms += "Read Messages, "
  if role.permissions.send_messages:
            perms += "Send Messages, "
  if role.permissions.send_tts_messages:
            perms += "Send TTS Messages, "
  if role.permissions.manage_messages:
            perms += "Manage Messages, "
  if role.permissions.embed_links:
            perms += "Embed Links, "
  if role.permissions.attach_files:
            perms += "Attach Files, "
  if role.permissions.read_message_history:
            perms += "Read Message History, "
  if role.permissions.mention_everyone:
            perms += "Mention Everyone, "
  if role.permissions.external_emojis:
            perms += "Use External Emojis, "
  if role.permissions.connect:
            perms += "Connect to Voice, "
  if role.permissions.speak:
            perms += "Speak, "
  if role.permissions.mute_members:
            perms += "Mute Members, "
  if role.permissions.deafen_members:
            perms += "Deafen Members, "
  if role.permissions.move_members:
            perms += "Move Members, "
  if role.permissions.use_voice_activation:
            perms += "Use Voice Activation, "
  if role.permissions.change_nickname:
            perms += "Change Nickname, "
  if role.permissions.manage_nicknames:
            perms += "Manage Nicknames, "
  if role.permissions.manage_roles:
            perms += "Manage Roles, "
  if role.permissions.manage_webhooks:
            perms += "Manage Webhooks, "
  if role.permissions.manage_emojis:
            perms += "Manage Emojis, "

  if perms is None:
            perms = "None"
  else:
            perms = perms.strip(", ")
          
  riembed.add_field(name='__General info__', value=f"Name: {role.name}\nId: {role.id}\nPosition: {role.position}\nHex: {role.color}\nMentionable: {role.mentionable}\nCreated At: {role.created_at}\nManaged by Integration: {(role.managed)}\n\nmembers in this role: {(len(role.members))}\n\nPermissions: {perms}")
  await ctx.reply(embed=riembed, mention_author=False)
  





  
@bot.command()
@commands.has_guild_permissions(manage_roles=True)
@blacklist_check()
async def unhideall(ctx):
    author = ctx.message.author
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    else:
        for x in ctx.guild.channels:
            await x.set_permissions(ctx.guild.default_role,view_channel=True)
       #     await ctx.reply(embed=discord.Embed(title="Successfully unhide all channels", description=f"responsible {ctx.author}", color=0x2f3136))




@commands.has_guild_permissions(manage_roles=True)    
@bot.command()
@blacklist_check()
async def hideall(ctx):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    else:
        for x in ctx.guild.channels:
            await x.set_permissions(ctx.guild.default_role,view_channel=False)
           # await ctx.reply(embed=discord.Embed(title="successfully hide all channels", description=f"responsible {ctx.author}", color=0x2f3136))
      
     
@commands.cooldown(3, 300, commands.BucketType.user)


@commands.has_permissions(administrator=True)


@bot.command(

    name="unlockall",

    description=

    "Unlocks the server. | Warning: this unlocks every channel for the everyone role.",

    usage="unlockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)
@blacklist_check()

async def unlockall(ctx, server: discord.Guild = None, *, reason=None):
    

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=True),

                reason=reason)

        await ctx.send(f"**{server}** has been unlocked.\nReason: `{reason}`")

    except:

        await ctx.send(f"```**Failed to unlock, {server}**```")

    else:

        pass
@bot.command(name="lockall",

                description="Locks down the server.",

                usage="lockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)
@blacklist_check()

async def lockall(ctx, server: discord.Guild = None, *, reason=None):

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=False),

                reason=reason)

        await ctx.send(f"**{server}** has been locked.\nReason: `{reason}`")

    except:

        await ctx.send(f"```**Failed to lockdown, {server}.**```")

    else:

        pass
      







    





@bot.command()
@blacklist_check()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel : discord.TextChannel=None):
  
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | <#{channel.id}> is now hidden from the default role.", color=0x2f3136))
@bot.command()
@blacklist_check()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel : discord.TextChannel=None):
  
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(embed=discord.Embed(title=f'<:Icons_correct:1017402689027592222> | <#{channel.id}> is now visible to the default role.', color=0x2f3136))

@bot.command()
@blacklist_check()
async def hi(ctx):
    await ctx.send("hii")


      





@bot.command()
@blacklist_check()
async def antialt(ctx, turn):
    if turn == "off":
        try:
            data = getConfig(ctx.guild.id)
            if ctx.author.id == ctx.guild.owner.id:
                loading = await ctx.send("Setting up the Anti Alt Off...")
                data = getConfig(ctx.guild.id)
                data["antinew"] = False
                updateConfig(ctx.guild.id, data)
                await loading.delete()
                embed = discord.Embed(
                    title="Setup successfully",
                    description=
                    f"I have successfully set the Anti Alt Acc feature Off.\n\n",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                await ctx.send("Only the owner can use this command!")
        except:
            print("na")
    elif turn == "on":
        try:
            data = getConfig(ctx.guild.id)
            if ctx.author.id == ctx.guild.owner.id:
                loading = await ctx.send("Setting up the Anti Alt Acc...")
                data = getConfig(ctx.guild.id)
                data["antinew"] = True
                updateConfig(ctx.guild.id, data)
                await loading.delete()
                embed = discord.Embed(
                    title="Setup successfully",
                    description=
                    f"I have successfully setup the Anti New Acc feature.\n\n",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                await ctx.send("Only the owner can use this command!")
        except:
            print("na")
    else:
        await ctx.send("pls send in on or off")
      

@bot.command(aliases=["bug","bugreport","fixbug"])
@commands.cooldown(1, 43200, commands.BucketType.user)
@blacklist_check()
async def report(ctx, *, desc=None):
      if desc == None:
        await ctx.send("PLEASE SUPPLY THE BUG INFORMATION !")
      else:
        await ctx.send("THANKS FOR REPORTING THE BUG. IT WILL BE FIXED SOON !")
        link = await ctx.channel.create_invite(unique=True)
        channel = bot.get_channel(1007214201741250590)
        embed=discord.Embed(title="BUG REPORT",description =f"`REPORTED BY - `\n{ctx.author.name}\n\n`I'D-`\n{ctx.message.author.id}\n\n`BUG -`\n{desc}\n\n`BUG FOUND IN - `\n{ctx.message.guild.name}\n\n`SERVER INVITE -`\n{link}",color=0x2f3136)
        await channel.send(embed=embed)

@report.error
async def report_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command(aliases=["sg","sugg"])
@commands.cooldown(1, 43200, commands.BucketType.user)
@blacklist_check()
async def Suggestion(ctx, *, desc=None):
      if desc == None:
        await ctx.send("PLEASE SUPPLY THE SUGGESTION!")
      else:
        await ctx.send("THANKS FOR  SUGGESTION!")
        link = await ctx.channel.create_invite(unique=True)
        channel = bot.get_channel(1007214215632801832)
        embed=discord.Embed(title="SUGGESTIONS ",description =f"`SUGGESTION BY - `\n{ctx.author.name}\n\n`I'D-`\n{ctx.message.author.id}\n\n`SUGGESTION-`\n{desc}\n\n`SUGGESTION FROM- `\n{ctx.message.guild.name}\n\n`SERVER INVITE -`\n{link}",color=0x2f3136)
        await channel.send(embed=embed)

@Suggestion.error
async def Suggestion_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command()
async def vote(ctx):
    author = ctx.message.author
    b = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discordbotlist.com/bots/zenox-5355/upvote')
    view = View()
    view.add_item(b)
    embed = discord.Embed(description=f"click on button below!",color=0x2f3136)
    embed.set_author(name=f"{author.name}", icon_url=author.display_avatar.url)
    embed.set_thumbnail(url=author.display_avatar.url)
    embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=author.display_avatar.url) 
    await ctx.send(embed=embed, view=view)

@bot.command(aliases=["inv"])
async def invite(ctx):
    author = ctx.message.author
    b = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://discord.com/api/oauth2/authorize?client_id=1004248513435152484&permissions=8&scope=bot')
    view = View()
    view.add_item(b)
        
    embed = discord.Embed(description="click on button below!", color=0x2f3136) 
    embed.set_author(name=f"{author.name}", icon_url=author.display_avatar.url)
    embed.set_thumbnail(url=author.display_avatar.url)
    embed.set_footer(text=f"thanks for using Soward") 
    await ctx.send(embed=embed, view=view)

@bot.command()
@blacklist_check()
async def ping(ctx):
      author = ctx.message.author
      embed = discord.Embed(description=f"<a:th_heartbeat:1017469364712263691> Pong! {round(bot.latency * 1000)}ms", color=0x2f3136)
      embed.set_author(name=f"{author.name}", icon_url=author.display_avatar.url)
      embed.set_thumbnail(url=author.display_avatar.url)
      embed.set_footer(text=f"requested by {author.name}", icon_url=author.display_avatar.url)
      await ctx.channel.send(embed=embed)
OWNER_IDS =  980361546918162482

def is_bot_owner(ctx):
  return ctx.message.author.id == 1018139793789563000


@bot.command()
@commands.check(is_bot_owner)
async def lhguugt(ctx):
    activeservers = bot.guilds
    sum = 0
    for guild in activeservers:
      await  ctx.send(f"name: {guild.name} | member count: {guild.member_count}, id = {guild.id}")


@bot.command()
@commands.check(is_bot_owner)
async def getinv(ctx, guild_id: int):
  guild = bot.get_guild(guild_id)
  channel = guild.channels[0]
  invitelink = await channel.create_invite(max_age=300)
  await ctx.send(embed=discord.Embed(title="INVITE LINK",description=f"INVITE LINK OF REQUESTED SERVER\n\n{invitelink}",color=0x2f3136,timestamp=ctx.message.created_at)) 
  

@bot.command(aliases=["em"])
@blacklist_check()
@commands.has_permissions(embed_links=True)
async def embed(ctx,*,mesg=f"Format : embed [words]"):

    await ctx.message.delete()
    embed=discord.Embed(description=mesg,color=0x2f3136,timestamp=ctx.message.created_at)
    embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.display_avatar.url) 
    embed.set_footer(text=f"")
    await ctx.send(embed=embed)

@bot.command()
@commands.check(is_bot_owner)
async def adminservers(ctx):
	await ctx.message.delete()
	admins = []
	for guild in bot.guilds:
		if guild.me.guild_permissions.administrator:
			admins.append(discord.utils.escape_markdown(guild.name))
	adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
	await ctx.send(adminPermServers)

@bot.command()
@blacklist_check()
async def botlst(ctx):
	await ctx.message.delete()
	bots = []
	for member in ctx.guild.members:
		if member.bot:
			bots.append(
			    str(member.name).replace("`", "\`").replace("*", "\*").replace(
			        "_", "\_") + "#" + member.discriminator)
	bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
	await ctx.send(bottiez)  

@bot.command()
@commands.check(is_bot_owner)
async def leaveg(ctx, *, guild: discord.Guild=None):
  #if ctx.author.id in is_bot_owner:
    if guild is None:
        print("Please enter the guild ID!") # No guild found
        return
    await guild.leave() # Guild found
    await ctx.send(f"I left: {guild.name}!")
  

@bot.command(aliases=["cc"])
@blacklist_check()
@commands.has_permissions(manage_channels=True)
async def channelclean(ctx: Context, channeltodelete: str):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    else:
        if ctx.author.id == ctx.guild.owner_id:
            for channel in ctx.message.guild.channels:
                if channel.name == channeltodelete:
                    await channel.delete()
                    await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | Successfully Deleted All Channels With Name Of {channeltodelete}", color=0x2f3136))


@bot.command(aliases=["rc"])
@blacklist_check()
@commands.has_permissions(manage_roles=True)
async def roleclean( ctx: Context, roletodelete: str):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    else:
        for role in ctx.message.guild.roles:
            if role.name == roletodelete:
                await role.delete()
                await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | Successfully Deleted All Roles With Name Of {roletodelete}", color=0x2f3136))

def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner


##@commands.check(is_server_owner)
#@bot.command()
#@commands.has_permissions(administrator=True)
#@commands.cooldown(1, 10, commands.BucketType.user)
#@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
#@blacklist_check()
#@commands.guild_only()
#async def recover(ctx: Context):
   # for channel in ctx.guild.channels:
     #   if channel.name in ('rules', 'moderator-only'):
       #     try:
      #          await channel.delete()
       #         except:
      #              pass
       #         await ctx.reply(embed=discord.Embed(title="<:Icons_correct:1017402689027592222> | Successfully Deleted All Channels With Name Of `rules, moderator-only`", color=0x2f3136))

@bot.command(aliases=["channelcreate"])
@commands.has_permissions(manage_channels=True)
@blacklist_check()
async def addchannel(ctx, *names):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    else:
        for name in names:
            await ctx.guild.create_text_channel(name)
            await ctx.send(embed=discord.Embed(title=f'<:Icons_correct:1017402689027592222> | {name} has been created', color=0x2f3136))
    #    await sleep(1)

@bot.command(aliases=['deletechannel'])
@commands.has_permissions(manage_channels=True)
@blacklist_check()
async def delchannel(ctx, *channels: discord.TextChannel):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
    else:
        for ch in channels:
            await ch.delete()
            await ctx.send(embed=discord.Embed(title=f' <:Icons_correct:1017402689027592222> | {ch.name} has been deleted', color=0x2f3136))
       # await sleep(1)



@bot.command(aliases=["listen"])
@commands.check(is_bot_owner)
async def listening(ctx, *, message):
    await ctx.send("Soward | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    await ctx.send("Listening created!")

@bot.command(aliases=["watch"])
@commands.check(is_bot_owner)
async def watching(ctx, *, message):
    await ctx.send("Soward | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message,
        ))
    await ctx.send("watching created!")

@bot.command(aliases=["ply"])
@commands.check(is_bot_owner)
async def playing(ctx, *, message):
    await ctx.send("Soward | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name=message,
        ))
    await ctx.send("playing created!")

@bot.command()
@commands.check(is_bot_owner)
async def comp(ctx, *, message):
    await ctx.send("Soward | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.competing,
            name=message,
        ))
    await ctx.send("Competing created!")

@bot.command()
@commands.check(is_bot_owner)
async def stream(ctx, *, message):
    await ctx.send("Soward | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.streaming,
            name=message,
        ))
    await ctx.send("Streaming created!")

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def cnuke(ctx):

    channel_position = ctx.channel.position
    new_chan = await ctx.channel.clone()
    await ctx.channel.delete()
    await new_chan.edit(position = channel_position) 
    
    #embed=discord.Embed(title="Channel Nuked", description=f"<#{new_chan.id}> - {new_chan.name} has been nuked by {ctx.author}", color=0x13dd4e,timestamp=ctx.message.created_at)
    #embed.set_image(url="https://tenor.com/view/fire-boom-explosion-smoke-gif-17085230")
  #  embed.set_footer(text="Created by Prince")
    await new_chan.send(f"{new_chan.mention} ``nuked by`` {ctx.author.mention}")

@bot.command(aliases=["userbanner"])
@blacklist_check()
async def banner(ctx,  member: discord.Member = None):
    if member == None:
       member = ctx.author
    bannerUser = await bot.fetch_user(member.id)
    if not bannerUser.banner:
                pass
    
    embed=discord.Embed(title=f"{member.name}'s banner")
    embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=member.display_avatar.url)
    embed.set_image(url=bannerUser.banner)
    await ctx.send(embed=embed)

@banner.error
async def banner_error(ctx, error):
        if isinstance(error, commands.CommandInvokeError):
                await ctx.send(embed=discord.Embed(title="this user does not have any banner", color=0x13dd4e))


@bot.command()
@blacklist_check()
async def serverbanner(ctx: commands.Context):
      if not ctx.guild.banner:
        await ctx.send('This server does not have any banner!')
      embed = discord.Embed(title=f'{ctx.guild.name}\'s Banner', color = 0x2f3136)
      embed.set_image(url=ctx.guild.banner)
      await ctx.send(embed=embed)


             



@bot.command()
@blacklist_check()
async def source(ctx):
      embed = discord.Embed(description=f"[soward src](https://github.com/PRINCEOP24/Soward-bot-src.git)", color=0x2f3136)
     # embed.set_author(name=f"{user.avatar}")                          
      embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/kHT4vIV2yvQVr_TVRWuSfbSPVzLuI0hjxVULZroCx-E/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/fa3d59466f44e012f70d541d9d409520.png")
      embed.set_footer(text="enjoy")
      await ctx.channel.send(embed=embed)
 

@bot.command(
        name='servers',
        description='Owner Only | List the servers that the bot is in',
        usage='serverslist',
        aliases=["sl"]
    )
@commands.is_owner()
async def serverslist(ctx, page: int = 1):
        output = ''
        guilds = bot.guilds
        pages = (len(guilds)/15)
        if 1 <= page <= pages:
            counter = 1+(page-1)*15
            for guild in guilds[(page-1)*15:page*15]:
                gn = guild.name
                gi = str(guild.id)
                gm = str(len(guild.members))
                go = str(guild.owner)
                output += f'**{counter}.** `{gn}` **|** `{gi}` **|** `{gm}` **|** `{go}`\n'
                counter += 1
            embed = discord.Embed(
                colour=0,
                description=output,
                title='__**Server List**__',
                timestamp=ctx.message.created_at
            )
            embed.set_footer(
                text=f'Page {page} of {pages}'
            )
            msg = await ctx.send(
                embed=embed
            )
            await msg.add_reaction("⬅️")
            await msg.add_reaction("➡️")
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["➡️", "⬅️"]
            while True:
              try:
                reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
                if str(reaction.emoji) == "⬅️":
                  page += 1
                  await msg.remove_reaction(reaction, ctx.author)
                elif str(reaction.emoji) == "➡️":
                  page -= 1
                  await msg.remove_reaction(reaction, ctx.author)
              except asyncio.TimeoutError:
                await msg.remove_reaction(reaction, ctx.author)
                await msg.remove_reaction(reaction, ctx.author)
                await msg.remove_reaction(reaction, bot.user)
                await msg.remove_reaction(reaction, bot.user)
        else:
            await ctx.send(
                embed=discord.Embed(description='Invalid Page Number.'),delete_after=10)

             
   
    














@bot.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '$'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@bot.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)


@bot.command(aliases=["prefix"])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setprefix(ctx, prefixx):
  with open("prefixes.json", "r") as f:
    idk = json.load(f)
  if len(prefixx) > 5:
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x13dd4e), description=f'<:Wrong:1017402708703064144> | Prefix Cannot Exceed More Than 5 Letters'))
  elif len(prefixx) <= 5:
    idk[str(ctx.guild.id)] =  prefixx
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f'<:Icons_correct:1017402689027592222> | Updated Server Prefix To `{prefixx}`'))
  with open("prefixes.json", "w") as f:
    json.dump(idk, f, indent=4)

@bot.command()
@blacklist_check()
async def featurjhes(ctx):
  em = discord.Embed(description=f"**Antinuke Events**\nMove my role above for more protection.\n\nPunishments:\n\nAnti Ban: <:enabled:1017426787438960651>\nAnti Bot: <:enabled:1017426787438960651>\nAnti Channel create: <:enabled:1017426787438960651> \nAnti Channel delete: <:enabled:1017426787438960651>\nAnti Channel update: <:enabled:1017426787438960651>\nAnti Guild update: <:enabled:1017426787438960651>\nAnti Kick: <:enabled:1017426787438960651>\nAnti Member update: <:enabled:1017426787438960651>\nAnti Role create: <:enabled:1017426787438960651>\nAnti Role delete: <:enabled:1017426787438960651>\nAnti Role update: <:enabled:1017426787438960651>\nAnti Webhook: <:enabled:1017426787438960651>")
  em.set_thumbnail(url=bot.user.display_avatar.url)
  await ctx.send(embed=em)


with open('whitelisted.json') as f:
  whitelisted = json.load(f)

@bot.listen("on_guild_join")
async def update_json(guild):
    with open ('whitelisted.json', 'r') as f:
        whitelisted = json.load(f)


    if str(guild.id) not in whitelisted:
      whitelisted[str(guild.id)] = []


    with open ('whitelisted.json', 'w') as f: 
        json.dump(whitelisted, f, indent=4)

@commands.check(is_server_owner)
@bot.command(aliases = ['wlhd'])
@blacklist_check()
async def whihtelisted(ctx):

  embed = discord.Embed(title=f"Whitelisted users for {ctx.guild.name}", description="", color=0x13dd4e)

  with open ('whitelisted.json', 'r') as i:
        whitelisted = json.load(i)
  try:
    for u in whitelisted[str(ctx.guild.id)]:
      embed.description += f"<@{(u)}> - {u}\n"
    await ctx.reply(embed = embed)
  except KeyError:
    await ctx.reply("Nothing found for this guild!")

@bot.command(aliases = ['wul'])
@blacklist_check()
@commands.check(is_server_owner)
async def whitelistahah(ctx, user: discord.Member = None):
    if user is None:
        await ctx.reply("You must specify a user to whitelist.")
        return
    with open ('whitelisted.json', 'r') as f:
        whitelisted = json.load(f)


    if str(ctx.guild.id) not in whitelisted:
      whitelisted[str(ctx.guild.id)] = []
    else:
      if str(user.id) not in whitelisted[str(ctx.guild.id)]:
        whitelisted[str(ctx.guild.id)].append(str(user.id))
      else:
        await ctx.reply("That user is already in the whitelist.")
        return



    with open ('whitelisted.json', 'w') as f: 
        json.dump(whitelisted, f, indent=4)
    
    await ctx.reply(f"{user} has been added to the whitelist.")

#@whitelist.error
#async def whitelist_error(ctx, error):
  #  if isinstance(error, commands.CheckFailure):
   #     await ctx.reply("Sorry but only the guild owner can whitelist!")

#@whitelisted.error
#async def whitelisted_error(ctx, error):
  #  if isinstance(error, commands.CheckFailure):
      #  await ctx.reply("Sorry but only the guild owner can whitelisted!")

@bot.command(aliases = ['uwjl'])
@blacklist_check()
@commands.check(is_server_owner)
async def unwjhitelist(ctx, user: discord.User = None):
  if user is None:
      await ctx.reply("You must specify a user to unwhitelist.")
      return
  with open ('whitelisted.json', 'r') as f:
      whitelisted = json.load(f)
  try:
    if str(user.id) in whitelisted[str(ctx.guild.id)]:
      whitelisted[str(ctx.guild.id)].remove(str(user.id))
      
      with open ('whitelisted.json', 'w') as f: 
        json.dump(whitelisted, f, indent=4)
    
      await ctx.reply(f"{user} has been removed from the whitelist.")
  except KeyError:
    await ctx.reply("This user was never whitelisted.")

#@unwhitelist.error
#async def unwhitelist_error(ctx, error):
   # if isinstance(error, commands.CheckFailure):
   #     await ctx.reply("Sorry but only the guild owner can unwhitelist!")









keep_alive()

bot.run('MTAwNDI0ODUxMzQzNTE1MjQ4NA.Gn9shC.zvlZHy1KrvCKB0m4WXjBBB9XvGmBzHBN3Tvcy4', reconnect=True)