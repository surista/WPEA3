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
    def __init__(self, home_name):
        self.home_name = home_name

    def add_rooms(self, room):
        self.room = room

    def __str__(self):
        return "{self.name}: ".format(self=self)
h = House()
myoffice = Room('office', 10)
h.add_rooms(myoffice)
print(h)