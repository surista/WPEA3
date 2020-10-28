#!/usr/bin/env python3
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
        return "{self.name}, {self.size}m".format(self=self)


class House:
    def __init__(self, h_size=100, available_space=100):
        self.rooms = []
        self.h_size = h_size
        self.available_space = available_space

    def add_rooms(self, *args):

        for item in args:
            if item.size > self.available_space:
                raise NotEnoughSpaceError(f'{item.name} needs {item.size}; only {self.available_space - self.h_size()} available')
            else:
                self.rooms.append(item)
                self.available_space -= item.size

    def size(self):
        return sum(one_room.size for one_room in self.rooms)

    def room_names(self):
        output = (one_room for one_room in self.rooms)
        print(output)

    def __str__(self):
        output = "House: \n"
        output += "\n".join(str(one_room) for one_room in self.rooms)
        return output


class NotEnoughSpaceError(Exception):
    "Raised if trying to add new room puts total size over limit "
    pass
