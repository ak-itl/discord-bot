import discord
import os
from scrape import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('hey there!')

  # replace direct link with os env variables
  if message.content.startswith('$grailed'):
    list = scrape(os.environ['GRAILED_LIKES'])
    for i in list:
      await message.channel.send(i)

  if message.content.startswith('$depop'):
    list = scrape(os.environ['DEPOP_LIKES'])
    for i in list:
      await message.channel.send(i)


client.run(os.environ['TOKEN'])
