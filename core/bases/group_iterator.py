from collections.abc import Iterator
import bases

class GroupIterator(Iterator):
    def __init__(self, group: 'bases.Group'):
        self.group = group.get_objects()
        self.length = len(self.group)
        self.pos = 0

    def __next__(self) -> 'bases.Object':
        if self.pos < self.length:
            item = self.group[self.pos]
            self.pos += 1
            return item
        raise StopIteration()