import discord
from discord.ext import commands
import random
from colorama import Fore, Back, Style
import asyncio
from discord import Permissions
import datetime
import aiohttp
import requests
import io
import json

token = 'ODE4Nzc2MTI4MjI2NzIxODEz.YEc-sQ.Wnp6mKvH88-Jn4rurZ8HBAdmbxA'

intents = discord.Intents.all()
intents.members = True

wrld = commands.Bot(command_prefix = commands.when_mentioned_or(';'))
wrld.remove_command('help')


@wrld.event
async def on_ready():
  print('Bot Is Ready Prefix is ;')
  while True: 
    await wrld.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming,url="https://twitch.tv/wrld.",name="𝙒𝙍𝙇𝘿++!")) 
    await asyncio.sleep(10)
    await wrld.change_presence(activity=discord.Activity  (type=discord.ActivityType.playing,name=";help"))
    await asyncio.sleep(10)
    await wrld.change_presence(activity=discord.Activity  (type=discord.ActivityType.listening,name="Rayys Sex Noises"))
    await asyncio.sleep(10)
    await wrld.change_presence(activity=discord.Activity  (type=discord.ActivityType.watching,name="Solars Bed"))
    await asyncio.sleep(10)

c = 0x2f3136
@wrld.command(aliases=['Help'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def help(ctx):
  embed=discord.Embed(title='WRLDs Help Menu', description='*Do ;[category] for info on it.*',color=c)
  embed.add_field(name='__Mod/Moderation__', value='`Displays WRLDs Moderation Commands!`',inline=False)
  embed.add_field(name='__Fun__', value='`Displays WRLDs Fun Commands!`', inline=False)
  embed.add_field(name='__Utility__', value='`Displays WRLDs Utility Commands!`', inline=False)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@wrld.command(aliases=['mod','m'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def Mod(ctx):
  embed=discord.Embed(title='WRLDs Mod Commands', description='*Do ;[command] to execute.*',color=c)
  embed.add_field(name='__Ban__', value='`Bans Mentioned User`',inline=False)
  embed.add_field(name='__Kick__', value='`KIcks Mentioned User`', inline=False)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)



@wrld.command(aliases=['Fun','f'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def fun(ctx):
  embed=discord.Embed(title='WRLDs Fun Commands', description='*Do ;[command] to execute.*',color=c)
  embed.add_field(name='__Kiss__', value='`Kisses Mentioned User`',inline=False)
  embed.add_field(name='__Hug__', value='`Hugs Mentioned User`', inline=False)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@wrld.command(pass_contex=True, aliases=['Hug'])
async def hug(ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            if member == None:
                  embed = discord.Embed(description = f"**{ctx.author.mention} Hugged {ctx.author.mention}**", color=c)
                  HUG = ["https://cdn.discordapp.com/attachments/790405104280666122/806539106707439656/hug.gif","https://cdn.discordapp.com/attachments/790405104280666122/806540353150124062/anime_hug_2.gif"]
                  rhug = random.choice(HUG)
                  embed.set_image(url=rhug)
                  embed.set_footer(text=f"Requested by {ctx.author}")
                  await ctx.send(embed=embed)

            embed = discord.Embed(description = f"**{ctx.author.mention} Hugged {member.mention}**", color=c)
            HUG = ["https://cdn.discordapp.com/attachments/790405104280666122/806539106707439656/hug.gif","https://cdn.discordapp.com/attachments/790405104280666122/806540353150124062/anime_hug_2.gif"]
            rhug = random.choice(HUG)
            embed.set_image(url=rhug)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)

@wrld.command(pass_contex=True, aliases=['Kiss'])
async def kiss(ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            if member == None:
                  embed = discord.Embed(description = f"**{ctx.author.mention} Kissed {ctx.author.mention}**", color=c)
                  HUG = ["https://cdn.discordapp.com/attachments/790405104280666122/806543272168128572/TBKlQSx.gif","https://cdn.discordapp.com/attachments/790405104280666122/806543009612955708/anime_kiss.gif"]
                  rhug = random.choice(HUG)
                  embed.set_image(url=rhug)
                  embed.set_footer(text=f"Requested by {ctx.author}")
                  await ctx.send(embed=embed)

            embed = discord.Embed(description = f"**{ctx.author.mention} Kissed {member.mention}**", color=c)
            HUG = ["https://cdn.discordapp.com/attachments/790405104280666122/806543272168128572/TBKlQSx.gif","https://cdn.discordapp.com/attachments/790405104280666122/806543009612955708/anime_kiss.gif"]
            rhug = random.choice(HUG)
            embed.set_image(url=rhug)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)

@wrld.command(aliases=['utility','u'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def Utility(ctx):
  embed=discord.Embed(title='WRLDs Utility Commands', description='*Do ;[command] to execute.*',color=c)
  embed.add_field(name='__Av__', value='`Shows Avatar Of Mentioned User`',inline=False)
  embed.add_field(name='__Serverinfo__', value='`Shows Info On Server`', inline=False)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@wrld.command(aliases=["Av","av"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def Avatar(ctx, *, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(
        title=f"{member.name}'s avatar",
        color=c,
        timestamp=ctx.message.created_at)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@wrld.command(aliases=["serverinfo","si","Si"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def Serverinfo(ctx):
    a = ctx.guild.member_count
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        description=
        f"{a} **Members**\n {len(ctx.guild.roles)} **Roles**\n {len(ctx.guild.text_channels)} **Text-Channels**\n {len(ctx.guild.voice_channels)} **Voice-Channels**\n {len(ctx.guild.categories)} **Categories**",
        timestamp=datetime.datetime.utcnow(),
        color=c)
    embed.add_field(
        name="Server created at",
        value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=owner)
    embed.add_field(name="Server Region", value=region)
    embed.add_field(name="Server ID", value=id)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@wrld.command()
async def poll(ctx, *,message):
 embed=discord.Embed(title="Poll", description=f"``{message}``",color=c)
 msg=await ctx.channel.send(embed=embed)
 await msg.add_reaction('👍')
 await msg.add_reaction('👎')

@wrld.command()
async def ping(ctx):
  embed = discord.Embed(title='Pong!', description=f'{round(wrld.latency*1000)} ms',color=c, timestamp=ctx.message.created_at)
  await ctx.send(embed=embed)

wrld.run(token, bot=True)
