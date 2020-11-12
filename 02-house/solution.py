#!/usr/bin/env python3


class Room():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name}, {self.size}m'


class House():
    def __init__(self):
        self.rooms = []

    def add_rooms(self, *args):
        for one_item in args:
            self.rooms.append(one_item)

    def size(self):
        return sum(one_room.size
                   for one_room in self.rooms)

    def __str__(self):
        output = 'House:\n'
        output += '\n'.join(str(one_room)
                            for one_room in self.rooms)
        return output


h = House()
bedroom = Room('bedroom', 10)
kitchen = Room('kitchen', 9)
bathroom = Room('bathroom', 3)
h.add_rooms(bedroom, kitchen, bathroom)

print(h)