from bases.interfaces.object_interface import ObjectInterface
from bases.interfaces.group_interface import GroupInterface
from bases.group import Group

class GameSystem:
    def __init__(self):
        self.__last_uid = 0
        self.__unused_uids = []
        self.__all_objects: Group = Group('AllObjects')
        self.__all_groups: Group = Group('AllGroups')
    

    def add_object(self, obj: ObjectInterface):
        self.__all_objects.add_object(obj)
    
    def add_group(self, group: GroupInterface):
        self.__all_groups.add_object(group)
    

    def generate_uid(self) -> int:
        if len(self.__unused_uids) != 0:
            return self.__unused_uids.pop()

        uid = self.__last_uid
        self.__last_uid += 1
        return uid
    

    def unlock_uid(self, uid: int) :
        if uid == self.__last_uid - 1:
            self.__last_uid -= 1
            return
        
        if uid not in self.__unused_uids:
            self.__unused_uids.append(uid)
    

    def get_element_by_uid(self, uid: int): pass

    def get_group_by_name(self, name: str): pass

    def get_objects_by_name(self, name: str): pass
    
