import discord
import os
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix="m!")


@client.slash_command()
async def ping(ctx):
  await ctx.respond('pong!')

@client.command()
async def hello(ctx):
  member = ctx.author

  em = discord.Embed(title = 'Hello! 👋🏻', description = f'Hello {member.mention}!', colour = 0x31bd54)

  await ctx.send(embed = em)


keep_alive()
client.run(os.getenv("token"))

#Watch the tutorial here if you do not understand the code or join my discord server!
