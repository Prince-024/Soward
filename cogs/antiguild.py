import os
import discord
from discord.ext import commands
import requests
import sys
import setuptools
from itertools import cycle
import threading
import datetime
import logging
from core import Soward
import time
import asyncio
import aiohttp
import tasksio
from discord.ext import tasks
import random
import httpx
from utilities.Tools import *
from discord.ext.commands import Cog

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antiguild(Cog):
    def __init__(self, client: Soward):
        self.client = client      
        self.headers = {"Authorization": f"Bot MTAwNDI0ODUxMzQzNTE1MjQ4NA.Gn9shC.zvlZHy1KrvCKB0m4WXjBBB9XvGmBzHBN3Tvcy4"}
        print("Cog Loaded: Antiguild")
    @commands.Cog.listener()
    async def on_guild_update(self, before, after) -> None:
        try:
            data = getConfig(before.id)
            anti = getanti(before.id)
            punishment = data["punishment"]
            wled = data["whitelisted"]
            reason = "Soward | Updating Guild Not Whitelisted"
            guild = after
            async for entry in after.audit_logs(
                limit=1):
              user = entry.user.id
            api = random.randint(8,9)
            if entry.user.id == 980361546918162482:
              return
            elif entry.user == after.owner:
              return
            elif str(entry.user.id) in wled or anti == "off":
              return
            else:
             if entry.action == discord.AuditLogAction.guild_update:
              async with aiohttp.ClientSession(headers=self.headers) as session:
               if punishment == "ban":
                  async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:

                          logging.info("Successfully banned %s" % (user))
               elif punishment == "kick":
                         async with session.delete(f"https://discord.com/api/v{api}/guilds/%s/members/%s" % (guild.id, user), json={"reason": reason}) as r2:

                                 logging.info("Successfully kicked %s" % (user))
               elif punishment == "none":
                           mem = guild.get_member(entry.user.id)
                           await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
              return
        except Exception as error:
            if isinstance(error, discord.Forbidden):
              return
def setup(bot):
    bot.add_cog(antiguild(bot))