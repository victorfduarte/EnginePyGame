
import pygame
import gamesystem
from bases import *

pygame.init()
gamesystem.init()

tela = Screen('Jogo')

o1 = Object(tela, 'Primeiro')
o2 = Object(tela, 'Segundo')
o3 = Object(tela, 'Terceiro')

grupo = Group('gp1', o1, o2, o3, o2)
grupo.add(o3)
grupo.remove(o2)
grupo.set_objects(o1, o3, o2, o1)
print(grupo.get_nome())

del o2

for item in grupo:
    print('item:', item.get_nome(), item.get_uid())


def func(a: int):
    if a == 5:
        return 10
    return False
    



