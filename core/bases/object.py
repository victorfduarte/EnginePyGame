from bases.interfaces.object_interface import ObjectInterface
from bases.group import Group
from gamesystem import game


class Object(ObjectInterface):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__uid = game.generate_uid()
        self.__colliders = []
        self.__surfaces = []
        self.__conteiners: Group = Group('Compose')

        game.add_object(self)
    

    def __eq__(self, __o: 'ObjectInterface') -> bool:
        return self.__uid == __o.get_uid()
    
    def compose(self, group: Group):
        self.__conteiners.add_object(group)
    
    def decompose(self, group: Group):
        self.__conteiners.remove_object(group)


    # GETTERS
    def get_nome(self) -> str:
        return self.__nome

    def get_uid(self) -> int:
        return self.__uid
    
    def get_surfaces(self) -> 'list[Surfaces]':
        return self.__colliders
    
    def get_collider(self) -> 'list[Rect]':
        return self.__surfaces
    

    # SETTERS
    def set_nome(self, nome: str) -> None:
        self.__nome = nome
    
    def set_uid(self, uid: int) -> None:
        self.__uid = uid
    
    def set_sufaces(self, *surfaces: 'Surface'):
        self.__surfaces = list(surfaces)

    def set_collider(self, *colliiders: 'Rect') -> None:
        self.__colliders = list(colliiders)