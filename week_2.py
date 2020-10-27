#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""
class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return "{self.name}, {self.size}".format(self=self)



class House:
    def __init__(self):
        self.rooms = []

    def add_rooms(self, *args):
        for item in args:
            self.rooms.append(item)

    def size(self):
        return sum([one_room.size for one_room in self.rooms])


    def __str__(self):
        return self.rooms



bedroom = Room('bedroom', 10)
kitchen = Room('kitchen', 9)
bathroom = Room('bathroom', 3)

h = House()

print(bedroom.size)
print(kitchen.name)
print(bathroom.size)
print(h)