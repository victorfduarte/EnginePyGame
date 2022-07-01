import bases

class ObjectManager:
    def __init__(self):
        self.__last_unused_uid: int = 0
        self.__unused_uids: 'list[int]' = []
        self.__all_objects: 'list[bases.Object | bases.Group]' = []
    

    def add_object(self, obj: 'bases.Object'):
        if obj.get_uid() == self.__last_unused_uid - 1:
            self.__all_objects.append(obj)
        else:
            self.__all_objects[obj.get_uid()] = obj
    

    def get_element_by_uid(self, uid: int): ...


    def get_element_by_name(self, name: str): ...
    

    def generate_uid(self) -> int:
        if len(self.__unused_uids) != 0:
            return self.__unused_uids.pop()

        uid = self.__last_unused_uid
        self.__last_unused_uid += 1
        return uid
    

    def unlock_uid(self, uid: int) :
        if uid == self.__last_unused_uid - 1:
            self.__last_unused_uid -= 1
            return
        
        if uid not in self.__unused_uids:
            self.__unused_uids.append(uid)
    
