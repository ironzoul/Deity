import discord
import random
from discord.ext import commands

class fun(commands.Cog):

   def  __init__(self,client):
       self.client = client

   @commands.Cog.listener()
   async def on_ready(self):
       print('fun is ready')

   #commands
   @commands.command(aliases=['8b','8ball','eightball','8 b','8 ball'])
   async def _8b(self,ctx, *, question):
       responses = [ 'As I see it, yes.','Ask again later.',
                        'Better not tell you now.',
                        'Cannot predict now.',
                        'Concentrate and ask again.',
                        'Don’t count on it.',
                'It is certain.',
                'It is decidedly so',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.' ]
       await ctx.send(f'question : {question}\nanswer : {random.choice(responses)}' )

   @commands.command()
   async def roll(self,ctx):
       rolling_numbers= random.randint(1,101)
       await ctx.send(rolling_numbers)

   @commands.command()
   async def poll(self,ctx,poll1,poll2, sep='|'):
       embed=discord.Embed(colour=0x4d64ff)
       embed.set_author(name='poll')
       embed.add_field(name='vote for ur opinion', value='\u200b',inline=True)
       embed.add_field(name='\u200b', value=f':one: {poll1}', inline=False)
       embed.add_field(name='\u200b', value=f':two: {poll2}', inline=False)
       await ctx.send(embed=embed)




def setup(client):
    client.add_cog(fun(client))