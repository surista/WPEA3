#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Week 1 of WPA #3
"""

class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    # def __str__(self):
    #     return "{self.name}, {self.size}".format(self=self)

    def __str__(self):
        return f'{self.name}, {self.size}m'