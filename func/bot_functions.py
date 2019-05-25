import random
import func.helper_functions as hf
import MySQLdb
import utilities.values as vals

random.seed()


mem_select = '''
SELECT      char_nm,
            realm_nm,
            race_nm,
            class_nm,
            raider_io_best,
            rank from (
    SELECT    char_nm,
              realm_nm,
              race_nm,
              char_realm,
              class_nm,
              raider_io_best,
              @curRank := @curRank + 1 AS rank
    FROM      guild_members gm, (SELECT @curRank := 0) r
    ORDER BY  raider_io_best DESC
    ) sub
where char_realm = "{}"
'''


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
        db = MySQLdb.connect(host=vals.HOST,user=vals.USER,passwd=vals.PW,db=vals.DB)
        c = db.cursor()
        c.execute(mem_select.format(mem))
        results = c.fetchall()
        if len(results) == 1:
            response = hf.member_info(results[0])
        else:
            response = "This member doesn't exist in this guild. Are you spelling it correctly?"
            response += " If the realm has an apostrophe, please remove it and try again!"
            c.close()
            db.close()
    else:
        response = "Please say -sawce info x where x is the guild member's character name!"
    return response