import random
import mySQLdb
import func.helper_functions as hf
random.seed()

def parse_roll(message):

    roll = message.split()
    sz_mess = len(roll)
    roll_x = None
    roll_y = None
    if (sz_mess == 3):
        roll_y = hf.convert_int(roll[2])
        roll_x = 1
    if (sz_mess == 4):
        roll_y = hf.convert_int(roll[3])
        roll_x = hf.convert_int(roll[2])
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
    
    return response

def parse_guildmember(message):
    mess = message.split()
    mess_sz = len(mess)
    if (mess_sz == 3):
        mem = mess[2]
        if (mem == 'Dartrude'):
            response = 'Dartrude is the coolest member in the guild!'
        else:
            response = mem + " isn't as cool as Dartrude, but they're close."
    else:
        response = "Please say -sawce info x where x is the guild member's character name!"
    return response