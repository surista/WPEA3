#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
wkr: Extending class to include neighborhoods
"""

class NotEnoughSpaceError(Exception):
    pass

class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return "{self.name}, {self.size}m".format(self=self)


class House:
    def __init__(self, available_space = 100):
        self.available_space = available_space
        self.rooms = []

    def add_rooms(self, *args):
        for item in args:
            if self.size() + item.size > self.available_space:
                raise NotEnoughSpaceError
            else:
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


class Neighborhood:
    total_size = 0

    def __init__(self, name):
        self.name = name
        self.homes = []

    def add_house(self, *args):
        for one_house in args:
            self.homes.append(one_house)
            Neighborhood.total_size += one_house.size()

    def size(self):
        return sum(one_house.size() for one_house in self.homes)



h1 = House(100)
h1bedroom = Room('bedroom', 15)
h1kitchen = Room('kitchen', 5)
h1bathroom = Room('bathroom', 8)
h1.add_rooms(h1bedroom,h1kitchen,h1bathroom)

h2 = House(100)
h2bedroom = Room('bedroom', 10)
h2kitchen = Room('kitchen', 9)
h2bathroom = Room('bathroom', 3)
h2.add_rooms(h2bedroom, h2kitchen, h2bathroom)

h3 = House(100)
h3bedroom = Room('bedroom', 7)
h3kitchen = Room('kitchen', 3)
h3bathroom = Room('bathroom', 2)
h3.add_rooms(h3bedroom,h3kitchen,h3bathroom)

h4 = House(100)
h4bedroom = Room('bedroom', 30)
h4kitchen = Room('kitchen', 19)
h4bathroom = Room('bathroom', 8)
h4.add_rooms(h4bedroom, h4kitchen, h4bathroom)

n1 = Neighborhood("Oak Valley")
n2 = Neighborhood("Mountain River")

n1.add_house(h1, h2)
n2.add_house(h3,h4)

