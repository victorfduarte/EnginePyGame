from collections.abc import Iterator
from bases.interfaces.group_interface import GroupInterface

class GroupIterator(Iterator):
    def __init__(self, group: GroupInterface):
        self.group = group.get_objects()
        self.length = len(self.group)
        self.pos = 0

    def __next__(self):
        if self.pos < self.length:
            item = self.group[self.pos]
            self.pos += 1
            return item
        raise StopIteration()