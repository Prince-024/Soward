import string
import discord
import asyncio
from utilities.Tools import*
from .utils.config import DEFAULT_COLOR
from discord.ext import commands
from datetime import datetime, timedelta
from views import help as vhelp #need big refactor

class HelpCommand(commands.HelpCommand):
    """Help command"""
        


    
    async def on_help_command_error(self, ctx, error) -> None:
            
        handledErrors = [
            commands.CommandOnCooldown, 
            commands.CommandNotFound
        ]

        if not type(error) in handledErrors:
            print("! Help command Error :", error, type(error), type(error).__name__)
            return await super().on_help_command_error(ctx, error)

    def command_not_found(self, string) -> None:
        raise commands.CommandNotFound(f"Command {string} is not found")
    
    async def send_bot_help(self, mapping) -> None:
        

        
        
        allowed = 5
        close_in = round(datetime.timestamp(datetime.now() + timedelta(minutes=allowed)))
        embed = discord.Embed(color = 0x35393D)
        embed.set_thumbnail(url ="https://images-ext-2.discordapp.net/external/vbj6ibvLs55RTX2t0uvyX54lJw3BRSlIMUEOYyAFg4o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/64dea1f7b0728ca6153a037725bdd037.png")
#        embed.set_image(url="https://cdn.discordapp.com/attachments/981877607597481989/983972390973349958/standard_4.gif")
      #  embed.set_author(name=f"{author.name}", icon_url=author.display_avatar.url )
        embed.set_footer(text=f"")
        embed.add_field(name="Soward ", value="Discord Multipurpose bot with  Moderation, ticket, information, utility and more. default Prefix = $ \n\n  [Get Soward](https://discord.com/oauth2/authorize?client_id=1004248513435152484&permissions=1101052116095&scope=applications.commands%20bot) | [Support](https://discord.gg/q8es72uZ7X)\n\n<:ModulesEmoji:1027644549310464030>__** COMMAND MODULE**__**\n\n<:F_lock:1001404597270741042> • Antinuke\n<a:moderation_animated:1017402486258151534> •  **Moderation**\n<:utility:1017405604987404408> • **Utility**\n<a:sinfo:1021052539216609351> • **Info**\n<:Ticket:1017405493477638205> • **Ticket**\n<a:welcome:1017405722226610247> • **Welcome**\n<a:coins:1017429986833076234> • **Economy\n\n```Select your category to see all commands!```", inline=True)
  #  embed.set_thumbnail(url=author.avatar) 
      #    embed.add_field(name="__Soward__", value=f">>> <:icons_bots:1005803665724031037> Soward is a multipurpose bot which comes with various premium fetures which you only need to mange your server\n<:Icons_correct:1005809876922007582> Total no. of commands: 245 |\n Usable by you (here) 82\n<:Icons_correct:1005809876922007582> Total modules: 15\n<:Icons_correct:1005809876922007582> Prefix: `$`", inline=True)
    #    embed.add_field(name="__Main Modules:__", value=f"\n>  <:icons_tada:1005823913244246046> ➜ 𝗚𝗶𝘃𝗲𝗮𝘄𝗮𝘆\n> <:spy_icons_Discord:1005805306682560612> ➜ 𝗚𝗲𝗻𝗲𝗿𝗮𝗹", inline=True)
   #     embed.add_field(name="__Extra Modules:__", value=f">>> <:emgames:1005805974042456064> ➜ 𝗚𝗮𝗺𝗲𝘀\n<:icons_human:1005806737397391410> ➜ 𝗔𝘂𝘁𝗼𝗿𝗼𝗹𝗲\n<:icons_spark:1005807400235835472> ➜ 𝗙𝘂𝗻\n<:icons_mod:1005808491837018112> ➜ 𝗠𝗼𝗱𝗲𝗿𝗮𝘁𝗶𝗼𝗻", inline=True)
          
      #  embed.add_field(name="SUPPORT", value=f"[Get Soward](https://discord.com/oauth2/authorize?client_id=1004248513435152484&permissions=1101052116095&scope=applications.commands%20bot) | [Support](https://discord.gg/dYNudnQtff)",inline=True)
    # embed.add_field(name="User count", value=len(bot.users)
  #  embed.add_field(name="User Count", value=len(bot.users))
   # embed.add_field(name="Ping", value=f"{bot.latency*1000:.2f}ms")
        





        view = vhelp.View(mapping = mapping, ctx = self.context, homeembed = embed, ui = 2)
        message = await self.context.send(embed = embed, view = view)
        try:
            await asyncio.sleep(60*allowed)
            view.stop()
            await message.delete()
        except: pass

    async def send_command_help(self, command):
        cog = command.cog
        if "help_custom" in dir(cog):
            emoji, label, _ = cog.help_custom()
            embed = discord.Embed(title = f"Help · {label} : {command.name}", description=f"**command** : {command.name}\n{command.help}", url="https://discord.gg/q8es72uZ7X", color = 0x35393D)
            params = ""
            for param in command.clean_params: 
                params += f" <{param}>"
            embed.add_field(name="Usage", value=f"{command.name}{params}", inline=False)
            embed.add_field(name="Aliases", value=f"{command.aliases}`")
            embed.set_footer(text="Made By Prince", icon_url=self.context.message.author.display_avatar.url)
            await self.context.send(embed=embed)

    async def send_cog_help(self, cog):
        if "help_custom" in dir(cog):
            emoji, label, _ = cog.help_custom()
            embed = discord.Embed(title = f"Help ", url="https://discord.gg/meta-development", color = 0x35393D)
            for command in cog.get_commands():
                params = ""
                for param in command.clean_params: 
                    params += f" <{param}>"
                embed.add_field(name=f"{command.name}{params}", value=f"{command.help}\n\u200b", inline=False)
            embed.set_footer(text="Made By Prince", icon_url=self.context.message.author.display_avatar.url)
            await self.context.send(embed=embed)

    async def send_group_help(self, group):
        await self.context.send("Group commands unavailable.")
     

class Help(commands.Cog, name="help"):
    """Help commands."""
    
    def __init__(self, bot):
        self._original_help_command = bot.help_command

        attributes = {
            'name': "help",
            'aliases': ['h'],
            'cooldown': commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.user) # discordpy2.0
        } 

        bot.help_command = HelpCommand(command_attrs=attributes)
        bot.help_command.cog = self
        
    def cog_unload(self):
        self.bot.help_command = self._original_help_command

    def help_custom(self):
        emoji = '<a:sq:1017393718329872425>'
        label = "Help"
        description = ""
        return emoji, label, description

def setup(bot):
	bot.add_cog(Help(bot))