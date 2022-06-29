from typing import Iterator
from bases.interfaces.object_interface import ObjectInterface
from bases.interfaces.group_interface import GroupInterface
from bases.group_iterator import GroupIterator
from gamesystem import game


class Group(GroupInterface):
    def __init__(self, nome: str, *objs: ObjectInterface):
        self.__nome = nome
        self.__uid = game.generate_uid()
        self.__conteiners: 'Group' = Group()
        self._objects: 'list[ObjectInterface]' = []

        self.add_object(*objs)



    def add_object(self, *objs: ObjectInterface):
        for obj in objs:
            if obj not in self._objects:
                self._objects.append(obj)
    

    def remove_object(self, *objs: ObjectInterface):
        for obj in objs:
            if obj in self._objects:
                self._objects.remove(obj)
    

    def get_by_uid(self, uid: int) -> ObjectInterface:
        pass


    def get_by_name(self, name: str) -> 'tuple[ObjectInterface]':
        pass


    def __eq__(self, __o: GroupInterface):
        return self.get_nome() == __o.get_nome()

    def __getitem__(self, index: int) -> ObjectInterface :
        return self._objects[index]
    
    def __setitem__(self, index: int, item: ObjectInterface):
        self._objects[index] = item

    def __iter__(self) -> Iterator:
        return GroupIterator(self)
    

    # Getters
    def get_objects(self) -> 'list[ObjectInterface]':
        return self._objects
    
    def get_nome(self) -> str:
        return self._nome
    
    def get_uid(self) -> int:
        return self._uid
    
    def get_surfaces(self) -> 'list[Surfaces]':
        surfaces = []
        for obj in self._objects:
            surfaces.append(obj.get_surfaces())
        return surfaces
    
    def get_collider(self) -> 'list[Rect]':
        colliders = []
        for obj in self._objects:
            colliders.append(obj.get_collider())
        return colliders
    
    
    # Setters
    def set_objects(self, *objs: ObjectInterface):
        self._objects = []
        self.add_object(*objs)
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def set_uid(self, uid: int) -> None:
        self._uid = uid
    
    def set_sufaces(self, *surfaces: 'Surface'):
        for obj in self._objects:
            obj.set_sufaces(*surfaces)
    
    def set_collider(self, *colliders: 'Rect') -> None:
        for obj in self._objects:
            obj.set_collider(*colliders)
    