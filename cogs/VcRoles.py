import discord
from discord.ext import commands
from discord.utils import get
from .utils.config import *
import motor.motor_asyncio as mongodb
from utilities.Tools import*


class VcRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://GoViper:GoViper#123@unique--cord.hmhy6.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.connection["Soward"]["Princeop"]

   

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        try:
          data = await self.db.find_one({"guild": member.guild.id})
          if data["vcrole"]["enabled"]== False:
            return
          else:  
            if not before.channel and after.channel:                
                x = data["vcrole"]["roleid"]
                r = get(member.guild.roles, id=x)
                await member.add_roles(r)
                  
            elif before.channel and not after.channel:
                x = data["vcrole"]["roleid"]
                r = get(member.guild.roles, id=x)
                await member.remove_roles(r)
        except Exception as e:
            print(e)


    @commands.group(name="vcroles", description="vcroles new\nvcroles config\nvcroles delete",invoke_without_command=True)
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def VcRoles(self, ctx):
        """vcroles new\nvcroles config\nvcroles delete"""
        x = "$"
        await ctx.send(embed=discord.Embed(title=f"Avaliable Commands: `{x}vcroles new <role>`, `{x}vcroles [show|config]`", color=0x2f3136))

    @VcRoles.command()
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def new(self, ctx, r: discord.Role):
        try:
            await self.db.update_one(
                {
                    "guild": ctx.guild.id
                },
                {
                    "$set": {
                        "vcrole.enabled" : True
                    }
                }
            )
            await self.db.update_one(
                {
                    "guild": ctx.guild.id
                },
                {
                    "$set": {
                        "vcrole.roleid" : r.id
                    }
                }
            )
            await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> Vc Roles Updated to `{r.name}`", color=0x2f3136))
        except Exception as e:
            return await ctx.send(f"An error occoured {e}")

    @VcRoles.command(aliases=['show'])
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def config(self, ctx):
            data = await self.db.find_one({"guild": ctx.guild.id})
            x = data["vcrole"]["roleid"]
            embed = discord.Embed(title=f"VcRoles:", description=f"<@&{x}>", color = DEFAULT_COLOR)
            await ctx.send(embed=embed)

    @VcRoles.command()
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx: commands.Context):
        await self.db.update_one(
                {
                    "guild": ctx.guild.id
                },
                {
                    "$set": {
                        "vcrole.roleid" : None
                    }
                }
            )
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Successfully Deleted Vc Role", color=0x2f3136))


def setup(bot):
    bot.add_cog(VcRoles(bot))