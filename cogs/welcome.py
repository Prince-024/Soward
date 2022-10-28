import discord
import logging
from discord.ext import commands
import motor.motor_asyncio as mongodb
from discord.colour import Color

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

class welcome_event(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = discord.Colour.green()
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://hacker:chetan2004@cluster0.rxh8r.mongodb.net/Flame?retryWrites=true&w=majority")
        self.db = self.connection["Zeon"]["servers"]
      
    @commands.Cog.listener()
    async def on_member_join(self, user):
        try:
            guild = user.guild
            data = await self.db.find_one({"guild": guild.id})

            if data["welcome"]["enabled"] != True:
                return 
            if data["welcome"]["message"] == None:
                return
            if data["welcome"]["channel"] == None:
                return

            channel = self.client.get_channel(data["welcome"]["channel"])
            message = data["welcome"]["message"]
            if "++user.id++" in message:
                    message = message.replace("++user.id++", "%s" % (user.id))

            if "++user.mention++" in message:
                message = message.replace("++user.mention++", "%s" % (user.mention))

            if "++user.tag++" in message:
                message = message.replace("++user.tag++", "%s" % (user.discriminator))

            if "++user.name++" in message:
                message = message.replace("++user.name++", "%s" % (user.name))
                
            if "++user.avatar++" in message:
                message = message.replace("++user.avatar++", "%s" % (user.avatar.url))

            if "++server.name++" in message:
                message = message.replace("++server.name++", "%s" % (user.guild.name))

           # if "++author.name++" in message:
              #  message = message.replace("++author.name++", "%s" % embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.avatar_url)
                
            if "++server.membercount++" in message:
                message = message.replace("++server.membercount++", "%s" % (user.guild.member_count))
                
            if "++server.icon++" in message:
                message = message.replace("++server.icon++", "%s" % (user.guild.icon.url))
            embed = discord.Embed(description=message,color = 0x0a44f5)
            embed.set_author(name=f"{user.name}",icon_url=user.display_avatar.url)
            embed.set_thumbnail(url=user.guild.icon.url)
            embed.set_footer(text="Made By Prince",icon_url="https://images-ext-2.discordapp.net/external/XpYSeN_4K1TG8OtzI3R3LE3zXbhvqB1rwgQkKRSs-Ww/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/980361546918162482/aa3b4e68dd27540854c0e0e3f374fe32.png")
            await channel.send(user.mention,embed=embed)
            #await channel.send(user.mention, embed=discord.Embed(
                #description=message,
                #color = 0x0a44f5))
        except Exception:
            pass

def setup(client):
    client.add_cog(welcome_event(client))