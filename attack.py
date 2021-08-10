from game import *
from randomMaker import *
from arrs import *



def attack_enemy(enemyCount):
    rickSays = get_attack()[randomAtttackMaker()]["saying"]+ " "
    damageAmt = get_attack()[randomAtttackMaker()]["attack"]
    enemyCount -= damageAmt
    x = rickSays + f'{enemyCount}'
    return x
