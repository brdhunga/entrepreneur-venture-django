import random

def randomid():
    strings = "0123456789qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ"
    rand_id = ""
    for x in range(0, 10):
        rand = random.randint(0,61)
        print rand
        new = strings[rand]
        rand_id = rand_id + new
    return rand_id