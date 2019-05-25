def convert_int(value):
    try:
        x = int(value)
        return x
    except ValueError:
        return None

def member_info(mem_info):
    char_nm = mem_info[0]
    realm_nm = mem_info[1]
    race_nm = mem_info[2]
    class_nm = mem_info[3]
    raider_io_best = mem_info[4]
    guild_rank = mem_info [5]
    result = '**Character Name:** ' + char_nm + '\n'
    result += '**Realm: **' + realm_nm + '\n'
    result += '**Race: **' + race_nm + '\n'
    result += '**Class: **' + class_nm + '\n'
    result += '**Raider IO: **' + str(raider_io_best) + '\n'
    result += '**Guild IO Ranking: **' + str(guild_rank)
    return result