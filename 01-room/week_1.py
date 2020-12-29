#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

class Room:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        print(f"{self.name}, {self.size}m")



