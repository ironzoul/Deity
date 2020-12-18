import discord
import os
import json
from discord.ext import commands
# supplement of guild prefix


def get_prefix(message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
# end of supplement


bot = commands.Bot(command_prefix='-')


# removing default help
bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(colour=0x551dad)
    embed.set_author(name=f'Help?? Indeed!!!', icon_url='https://cdn.discordapp.com/avatars/607219826221645855/f89247af5f3dde319274dd9c2b3cd84f.png?size=128')
    embed.add_field(name='admin tools',value='`ping` `clear` `kick` `ban`  `command_prefix`', inline=True)
    embed.add_field(name='fun commands:',value='`roll` `8b` `poll` `whatsnew` `poll`', inline=False)
    embed.add_field(name='emotes:relieved::',value='`hug`, `pat(very soon)`', inline=False)
    await ctx.send(embed=embed)


# new code      for guild prefix


@bot.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes=json.load(f)

    prefixes[str(guild.id)] = '-'

    with open('prefixes.json','w') as f:
        json.dump(prefixes, f, indent=4)


@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes=json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json','w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
async def changeprefix(ctx,prefix):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
# end of new code
# bot status
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='Your Server'))
# bot status
# @bot.event
# async def on_ready():
#    print('u are ready to go')

@bot.command()
async def ping(ctx):
    embed= discord.Embed(colour=0xFF4500)
    embed.set_author(name=f'pong! in {round(bot.latency*1000)}ms',icon_url='https://cdn.discordapp.com/attachments/749953221669421119/754838619591540866/41.png')
    # embed.add_field(name='\u200b', value=f'pong! in {round(bot.latency*1000)}ms', inline= True)

    await ctx.send(embed=embed)

for filename in os.listdir('./extention'):
    if filename.endswith('.py'):
        bot.load_extension(f'extention.{filename[:-3]}')

@bot.command()
async def load(extension):
    bot.load_extension(extension)

@bot.command()
async def unload(extension):
    bot.unload_extension(extension)

@bot.command()
async def reload(extension):
    bot.unload_extension(extension)
    bot.load_extension(extension)


bot.run('NzA3ODU2MTAzODYxMzg3Mjc0.XrO4Xg.OCgn3O_J_1xzPKYqVvcuFkp-DYE')