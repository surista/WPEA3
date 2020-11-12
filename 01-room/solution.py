#!/usr/bin/env python3


class Room():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name}, {self.size}m'
