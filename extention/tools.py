import discord
from discord.ext import commands

class tools(commands.Cog):
    def __init__(self,client):
        self.client= client

    @commands.Cog.listener()
    async def when_ready(self):
        print('tools are ready')

    @commands.command()
    async def clear(self,ctx,ammount=1):
        await ctx.channel.purge(limit=ammount)
    

def setup(client):
    client.add_cog(tools(client))