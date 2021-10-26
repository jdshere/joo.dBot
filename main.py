import discord
import os
from discord.ext import commands

client = discord.Bot()

@client.event
async def on_ready():
  print('Online!!')


@client.slash_command(guild_ids=[902177990916579399])
async def ping(ctx):
  await ctx.respond('pong!')


client.run(os.getenv("token"))

#Watch the tutorial here if you do not understand the code or join my discord server!
