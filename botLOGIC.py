import random



def gen_pass(passi):
    password = ""
    simbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for i in range(passi):
        password += random.choice(simbol)
    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923","\U0001F601","\U0001F929","\U0001F607","\U0001F61C","\U0001FAE2","\U0001F922","\U0001F92F","\U0001F920","\U0001F921"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
