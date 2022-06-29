from typing import TYPE_CHECKING
from bases.interfaces.draw_interface import DrawInterface
from bases.interfaces.collider_interface import CollisionInterface

class ObjectInterface(DrawInterface, CollisionInterface):
    def __init__(self, nome: str, *args): pass
    def get_nome(self) -> str : pass
    def get_uid(self) -> int: pass
    def set_nome(self, nome: str) -> None: pass
    def set_uid(self, uid: int) -> None: pass