from typing import Any
import pygame as pg
import bases


class CleanGroup:
    def __init__(self, nome: str, *objs: 'Any'):
        self.__nome = nome
        self.__conteiners: 'list[CleanGroup | bases.Group]' = []
        self.__objects = []

        self.add(*objs)


    def add(self, *objs: 'Any'):
        for obj in objs:
            if obj not in self.__objects:
                self.__objects.append(obj)
                obj.compose(self)
    

    def remove(self, *objs: 'Any'):
        for obj in objs:
            if obj in self.__objects:
                self.__objects.remove(obj)
                obj.decompose(self)
    

    def get_by_name(self, name: str) -> 'tuple[Any]':
        pass


    def __eq__(self, __o: 'CleanGroup'):
        return self.get_nome() == __o.get_nome()

    def __iter__(self) -> 'bases.GroupIterator':
        return bases.GroupIterator(self)
    

    # Getters
    def get_objects(self) -> 'list[Any]':
        return self.__objects
    
    def get_nome(self) -> str:
        return self.__nome

    
    # Setters
    def set_objects(self, *objs: 'Any'):
        self.__objects = []
        self.add(*objs)
    
    def set_nome(self, nome: str) -> None:
        self.__nome = nome