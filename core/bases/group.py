import pygame as pg
import bases
import bases.interfaces as interfaces
import gamesystem as gs


class Group(interfaces.DrawInterface, interfaces.CollisionInterface):
    def __init__(self, nome: str, *objs: 'bases.Object'):
        self.__nome = nome
        self.__conteiners: 'list[Group]' = []
        self.__objects: 'list[bases.Object]' = []

        self.add(*objs)


    def add(self, *objs: 'bases.Object'):
        for obj in objs:
            if obj not in self.__objects:
                self.__objects.append(obj)
                obj.compose(self)
    

    def remove(self, *objs: 'bases.Object'):
        for obj in objs:
            if obj in self.__objects:
                self.__objects.remove(obj)
                obj.decompose(self)
    

    def get_by_uid(self, uid: int) -> 'bases.Object':
        pass


    def get_by_name(self, name: str) -> 'tuple[bases.Object]':
        pass


    def __eq__(self, __o: 'Group'):
        return self.get_nome() == __o.get_nome()

    def __iter__(self) -> 'bases.GroupIterator':
        return bases.GroupIterator(self)
    

    # Getters
    def get_objects(self) -> 'list[bases.Object]':
        return self.__objects
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_surfaces(self) -> 'list[pg.Surface]':
        surfaces = []
        for obj in self.__objects:
            surfaces.append(obj.get_surfaces())
        return surfaces
    
    def get_collider(self) -> 'list[pg.Rect]':
        colliders = []
        for obj in self.__objects:
            colliders.append(obj.get_collider())
        return colliders
    
    
    # Setters
    def set_objects(self, *objs: 'bases.Object'):
        self.__objects = []
        self.add(*objs)
    
    def set_nome(self, nome: str) -> None:
        self.__nome = nome
    
    def set_sufaces(self, *surfaces: 'pg.Surface'):
        for obj in self.__objects:
            obj.set_sufaces(*surfaces)
    
    def set_collider(self, *colliders: 'pg.Rect') -> None:
        for obj in self.__objects:
            obj.set_collider(*colliders)
    