# STUFF TO DO

import discord
import random

random.seed()
client = discord.Client()

def convert_int(value):
    try:
        x = int(value)
        return x
    except ValueError:
        return None

def parse_roll(message):
    roll = message.content.split()
    sz_mess = len(roll)
    roll_x = None
    roll_y = None
    if (sz_mess == 3):
        roll_y = convert_int(roll[2])
        roll_x = 1
    if (sz_mess == 4):
        roll_y = convert_int(roll[3])
        roll_x = convert_int(roll[2])
    if (roll_x is not None and roll_y is not None):
        if (roll_x < roll_y):
            roll_val = random.randrange(roll_x,roll_y)
        elif(roll_y < roll_x):
            roll_val = random.randrange(roll_y,roll_x)
        else:
            roll_val = roll_x
    else:
        roll_val = None

    if roll_val is not None:
        response = 'You rolled a ' + str(roll_val) + '!'
    else:
        response = "Please say -sawce roll x to roll an x-sided die or -sawce roll x y to roll a number between x and y!"
    
    return message.channel.send(response)
    
def parse_guildmember(message):
    mess = message.content.split()
    mess_sz = len(mess)
    if (mess_sz == 3):
        mem = mess[2]
        if (mem == 'Dartrude'):
            response = 'Dartrude is the coolest member in the guild!'
        else:
            response = mem + " isn't as cool as Dartrude, but they're close."
    else:
        response = "Please say -sawce info x where x is the guild member's character name!"
    return message.channel.send(response)
    
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-sawce roll'):
        await parse_roll(message)
        
    if message.content.startswith('-sawce info'):
        await parse_guildmember(message)

client.run('KEY')
