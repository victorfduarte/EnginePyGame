from typing import Iterable
from typing import Iterator
from bases.interfaces.object_interface import ObjectInterface

class GroupInterface(ObjectInterface, Iterable):
    def add_object(self, *objs: 'ObjectInterface'): pass
    def remove_object(self, *objs: 'ObjectInterface'): pass
    def get_objects(self) -> 'tuple[ObjectInterface]': pass
    def set_objects(self, *objs: 'ObjectInterface'): pass
    def get_by_uid(self, uid: int) -> 'ObjectInterface': pass
    def get_by_name(self, name: str) -> 'tuple[ObjectInterface]': pass
    def __getitem__(self, index: int) -> 'ObjectInterface': pass
    def __setitem__(self, index: int, item: 'ObjectInterface'): pass
    def __iter__(self) -> Iterator: pass
