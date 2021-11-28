import random

def gq_randomizer():
    gifted_quotient_n = random.randint(0,1000)
    gifted_quotient = ''
    if gifted_quotient_n in range(0,500):
        gifted_quotient += 'Comum'
    elif gifted_quotient_n in range(500,750):
        gifted_quotient += 'Incomum'
    elif gifted_quotient_n in range(750,875):
        gifted_quotient += 'Raro'
    elif gifted_quotient_n in range(875,935):
        gifted_quotient += 'Talentoso'
    elif gifted_quotient_n in range(935,970):
        gifted_quotient += 'Único'
    elif gifted_quotient_n in range(970,988):
        gifted_quotient += 'Lendário'
    elif gifted_quotient_n in range(988,1000):
        gifted_quotient += 'Abençoado'
    elif gifted_quotient_n == 1000:
        gifted_quotient += 'Xamã'
    return gifted_quotient



def stat_ramdomizer(gq):
    if gq == 'Comum':
        n = 50
    elif gq == 'Incomum':
        n = 75
    elif gq == 'Raro':
        n = 100
    elif gq == 'Talentoso':
        n = 125
    elif gq == 'Único':
        n = 150
    elif gq == 'Lendário':
        n = 200
    elif gq == 'Abençoado':
        n = 500
    elif gq == 'Xamã':
        n = 1000
    n += 1
    rep = range(1,n)
    STR = AGI = INT = WIS = CHA = TGH = PER = WIL = LUC = INS = 1
    for x in rep:
        stat_n = random.randint(1,11)
        if stat_n == 1:
            STR += 1
        if stat_n == 2:
            AGI += 1
        if stat_n == 3:
            INT += 1
        if stat_n == 4:
            WIS += 1
        if stat_n == 5:
            CHA += 1
        if stat_n == 6:
            TGH += 1
        if stat_n == 7:
            PER += 1
        if stat_n == 8:
            WIL += 1
        if stat_n == 9:
            LUC += 1
        if stat_n == 10:
            INS += 1
    stat_stement = (f'''GQ: {gq}
    Stats: STRENGTH: {STR}, AGILITY: {AGI}, INTELLIGENCE: {INT}, WISDOM: {WIS} CHARISMA: {CHA},
TOUGHNESS: {TGH}, PERCEPTION: {PER}, WILLPOWER: {WIL}, LUCK: {LUC}, INSIGHT: {INS}
''')
    return stat_stement



