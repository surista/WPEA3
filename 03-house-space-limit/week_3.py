#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

class NotEnoughSpace(Exception):
    pass


class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name}, {self.size}m'


class House:
    def __init__(self, available_space = 100):
        self.rooms = []
        self.available_space = available_space

    def add_rooms(self, *args):
        for one_item in args:
            if (one_item.size + self.size()) < self.available_space:
                self.rooms.append(one_item)
            else:
                raise NotEnoughSpace(f'{one_item.name} needs {one_item.size}; only {self.available_space - self.size()} available')

    def size(self):
        return sum(one_room.size for one_room in self.rooms)

    def __str__(self):
        output = 'House:\n'
        output += '\n'.join(str(one_room) for one_room in self.rooms)
        return output


h = House(100)
r1 = Room('master bedroom', 25)
r2 = Room('bathroom', 5)
r3 = Room('living room', 30)
r4 = Room('kitchen', 20)

h.add_rooms(r1, r2, r3, r4)
print(h.size)  # returns 80

h.add_rooms(r1)  # try to add another master bedroom