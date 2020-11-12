#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Week 2 of WPA #3
"""
class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return "{self.name}, {self.size}m".format(self=self)


class House:
    def __init__(self):
        self.rooms = []

    def add_rooms(self, *args):
        for item in args:
            self.rooms.append(item)

    def size(self):
        return sum(one_room.size for one_room in self.rooms)

    def room_names(self):
        output = (one_room for one_room in self.rooms)
        print(output)

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