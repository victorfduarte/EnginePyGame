# from bases.group import Group
# from bases.object import Object

from bases import *

o1 = Object('Primeiro')
o2 = Object('Segundo')
o3 = Object('Terceiro')

grupo = Group('gp1', o1, o2, o3, o2)
grupo.add_object(o3)
grupo.remove_object(o2)
grupo.set_objects(o1, o3, o2, o1)
print(grupo.get_nome())

del o2

for item in grupo:
    print('item:', item.get_nome())


def func(a: int):
    if a == 5:
        return 10
    return False
    



