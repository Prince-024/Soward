import datetime
import discord
from discord.ext import commands
from Errorembed import ErrorEmbed
from typing import Optional
import urllib.request
import json
from utilities.Tools import *
class Colorcalc(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['rgb2h', 'rgb2hex'])
  @blacklist_check()
  async def rgbtohex(self, ctx, r=None, g=None, b=None):
    """Convert an RGB color code to a hexadecimal color code."""
    try:
      r = int(r)
      g = int(g)
      b = int(g)
    except:
      embed = ErrorEmbed.error("Invalid Command Arguments", "One or more of your R, G, or B values are invalid!  Make sure they are numbers between 0 and 255.")
      await ctx.send(embed=embed)
      return

    color = int(r*256*256)
    color += int(g*256)
    color += int(b)

    url = f"https://some-random-api.ml/canvas/hex?rgb={r},{g},{b}"
    response = urllib.request.urlopen(url).read().decode()
    colors = json.loads(response)
    hexcode = colors["hex"]

    embed = discord.Embed(
      title = "Color Conversion Calculator",
      description = f"Your color from RGB to Hex: {hexcode}",
      color = color,
      timestamp = datetime.datetime.utcnow()
    )
    await ctx.send(embed=embed)

  @commands.command(aliases=['h2rgb', 'hex2rgb', 'htrgb'])
  @blacklist_check()
  async def hextorgb(self, ctx, hex_code=None):
    """Convert a hexadecimal color code to a RGB color code."""
    if hex_code is None:
      embed = ErrorEmbed.error("Missing Command Arguments", "You must provide a valid 6-digit hex code!  Hex codes can contain numbers 0-9 and letters a-f.")
      await ctx.send(embed=embed)
      return
    url = f"https://some-random-api.ml/canvas/rgb?hex={hex_code}"
    try:
      response = urllib.request.urlopen(url).read().decode()
      colors = json.loads(response)
      if "error" in colors:
        embed = ErrorEmbed.error("Invalid Command Arguments", colors["error"])
        await ctx.send(embed=embed)
        return
      r = colors["r"]
      g = colors["g"]
      b = colors["b"]
      
      color = int(r*256*256)
      color += int(g*256)
      color += int(b)

      embed = discord.Embed(
        title = "Color Conversion Calculator",
        description = f"Your color from Hex to RGB: {r}, {g}, {b}",
        color = color,
        timestamp = datetime.datetime.utcnow()
      )
      await ctx.send(embed=embed)
    except:
      embed = ErrorEmbed.error("Invalid Command Arguments", "The hex code you provided is invalid!")
      await ctx.send(embed=embed)

  @commands.command(aliases=['cv', 'colorviewer'])
  @blacklist_check()
  async def colorview(self, ctx, hex_code = None):
    """Provide a hexadecimal color code and see the color that it stands for.  Using a color calculator might be useful to get a color that you want."""
    if hex_code is None:
      embed = ErrorEmbed.error("Missing Command Arguments", "You must provide a valid 6-digit hex code!  Hex codes can contain numbers 0-9 and letters a-f.")
      await ctx.send(embed=embed)
      return
    hex_code = hex_code.lower().strip("#").strip(" ")
    embed = discord.Embed(
      title = f"Hex Code: {hex_code}",
      color = 0x2f3136,
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_image(url=f"https://some-random-api.ml/canvas/colorviewer?hex={hex_code}")
    await ctx.send(embed=embed)

  @commands.command(description = "Convert an RGB color code to a decimal color code.", aliases = ['rgbtdec', 'rgb2dec','rgb2d'])
  @blacklist_check()
  async def rgbtodecimal(self, ctx, red:int=None, green:int=None, blue:int=None):
    """Convert an RGB color code to a decimal color code."""
    if red == None or green == None or blue == None:
      embed = ErrorEmbed.error("Missing Command Arguments", "You have to specify a value between 0 and 255 for each red, green and blue, in that order.")
      await ctx.send(embed=embed)
    elif red > 255 or green > 255 or blue > 255:
      embed = ErrorEmbed.error("Invalid Command Arguments", "Your R, G, and B values can be no more than 255.")
      await ctx.send(embed=embed)

    else:
      color = int(red*256*256)
      color += int(green*256)
      color += int(blue)
      embed = discord.Embed(
        title = "Color Conversion Calculator",
        description = f"Your color from RGB to decimal: {color}",
        color = color,
        timestamp = datetime.datetime.utcnow()
      )
      msg = await ctx.send(embed=embed)
      await msg.add_reaction("🟢")

  @commands.command(description = "Convert a decimal color code to an RGB color code.", aliases = ['dec2rgb', 'dectrgb', 'd2rgb'])
  @blacklist_check()
  async def decimaltorgb(self, ctx, c:int=None):
    """Convert a decimal color code into an RGB color code."""
    if c == None:
      embed = ErrorEmbed.error("Missing Command Arguments", "Please specify a decimal value no greater than 16777215 to convert into RGB.")
      await ctx.send(embed=embed)
    elif c > 16777215:
      embed = ErrorEmbed.error("Invalid Command Arguments", "Your decimal color value can be no more than 16,777,215.")
      await ctx.send(embed=embed)
    else:
      b = int(c) % 256
      g_0 = (int(c) % 65536 - int(b))
      r_0 = int(c) - int(g_0) - int(b)
      g = int(g_0) / 256
      r = int(r_0) / 65536
      int(r)
      int(g)
      int(b)
      embed = discord.Embed(
        title = "Color Conversion Calculator",
        description = f"Your color from Decimal to RGB: {r}, {g}, {b}",
        color = int(c),
        timestamp = datetime.datetime.utcnow()
      )
      msg = await ctx.send(embed=embed)
      await msg.add_reaction("🟢")

def setup(client):
  client.add_cog(Colorcalc(client))