# -*- coding: utf-8 -*-
import random

def dice_game():
    a=random.randint(1,6)
    b=random.randint(1,6)

    if a>b:
        return "Win alice"
    elif a<b:
        return "Win bob"
    return "Draw"

def roulette():
    r=random.randint(1,36)

    if r<=15:
        return "Win alice"
    elif r<=30:
        return "Win bob"
    return "Draw"

if __name__ == '__main__':
    print(roulette())
