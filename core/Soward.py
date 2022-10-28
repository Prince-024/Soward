import discord
from discord.ext import commands
import json
import os
import pymongo
os.system("pip install git+https://github.com/Pycord-Development/pycord")
os.system("pip install pymongo[srv]")


# ------------------------------ PREFIX AND INTENTS  -----------------------------------------



intents = discord.Intents.all()
#intents.presences = False


      


class Soward(commands.AutoShardedBot):
  def __init__(self) -> None:
    super().__init__()
    self.persistent_views_added = False
    
  
  
        
    print(f'╭────˚♪°𝄞°♪˚─────╮\n{self.user.name} is online.\n╰────˚♪°𝄞°♪˚─────╯')


   # self.bot = bot
 #   bot.lavalink_nodes = [
   # {"host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"},
    # Can have multiple nodes here
#]

# If you want to use spotify search
   # bot.spotify_credentials = {
   # 'client_id': '6ad677e7f4344a9ebd7958e3d6fa3e56',
   # 'client_secret': '6405a1b768e841ca8a6cf542b8f24f1d'
#}

    



    
#bot = commands.Bot(
#  command_prefix = get_prefix,
#  intents=intents,
#)      


#bot =Soward()

