def level_function(xp):
    return int((xp/100)**(1/2) + 1)

# def updatelevel(xp):
#     if xp >= 1000000:
#         return 100
#     lvl = level_function(xp)
#     return lvl

def xp_function(lvl):
    return (lvl-1)**2*100

def lvl_info(xp):
    lvl = level_function(xp)
    lower_xp = xp_function(lvl)
    upper_xp = xp_function(lvl + 1)
    road_to_next_level = xp - lower_xp
    xp_needed_for_next_level = upper_xp - lower_xp
    return 0, road_to_next_level, xp_needed_for_next_level