import discord
import math
import os
from discord.ext import commands

client= commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('u are ready to go')

@client.command()
async def ping(ctx):
    embed= discord.Embed(colour=0xFF4500)
    embed.add_field(name='\u200b', value=f'pong! in {round(client.latency*1000)}ms', inline= True)

    await ctx.send(embed=embed)

for filename in os.listdir('./extention'):
    if filename.endswith('.py'):
        client.load_extension(f'extention.{filename[:-3]}')

@client.command()
async def load(ctx,extension):
    client.load_extension({extension})

@client.command()
async def unload(ctx,extension):
    client.unload_extension({extension})

@client.command()
async def reload(ctx,extension):
    client.unload_extension({extension})
    client.load_extension({extension})


client.run('token')