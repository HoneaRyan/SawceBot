# STUFF TO DO

import discord
import func.bot_functions as bf
import utilities.values as vals

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-sawce roll'):
        await message.channel.send(bf.parse_roll(message.content))

    if message.content.startswith('-sawce info'):
        await message.channel.send(bf.parse_guildmember(message.content))

client.run(vals.SECRET_KEY)
