import pygame as pg
import bases
import bases.interfaces as interfaces
import gamesystem as gs


class Object(interfaces.DrawInterface, interfaces.CollisionInterface):
    def __init__(self, parent: 'bases.Screen', nome: str):
        self.__nome: str = nome
        self.__uid: int = gs.game.generate_uid()
        self.__parent: 'bases.Screen' = parent
        self.__colliders: 'pg.Rect' = []
        self.__surfaces: 'pg.Surface' = []
        self.__conteiners: 'list[bases.Group]' = []

        gs.game.add_object(self)
        parent.add(self)
    

    def __eq__(self, __o: 'Object') -> bool:
        return self.__uid == __o.get_uid()

    
    def compose(self, group: 'bases.Group'):
        self.__conteiners.append(group)
    
    def decompose(self, group: 'bases.Group'):
        self.__conteiners.remove(group)


    # GETTERS
    def get_nome(self) -> str:
        return self.__nome

    def get_uid(self) -> int:
        return self.__uid
    
    def get_parent(self) -> 'bases.Screen':
        return self.__parent
    
    def get_surfaces(self) -> 'list[pg.Surface]':
        return self.__colliders
    
    def get_collider(self) -> 'list[pg.Rect]':
        return self.__surfaces
    

    # SETTERS
    def set_nome(self, nome: str) -> None:
        self.__nome = nome
    
    def set_uid(self, uid: int) -> None:
        self.__uid = uid
    
    def set_parent(self, parent: 'bases.Screen') -> None:
        self.__parent = parent
    
    def set_sufaces(self, *surfaces: 'pg.Surface') -> None:
        self.__surfaces = list(surfaces)

    def set_collider(self, *colliiders: 'pg.Rect') -> None:
        self.__colliders = list(colliiders)