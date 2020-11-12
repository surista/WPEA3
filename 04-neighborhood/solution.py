#!/usr/bin/env python3


class NotEnoughSpaceError(Exception):
    pass


class Room():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name}, {self.size}m'


class House():
    def __init__(self, available_space=100):
        self.rooms = []
        self.available_space = available_space

    def add_rooms(self, *args):
        for one_item in args:
            if self.size() + one_item.size > self.available_space:
                raise NotEnoughSpaceError(
                    f'{one_item.name} needs {one_item.size}; only {self.available_space - self.size()} available')
            self.rooms.append(one_item)

    def size(self):
        return sum(one_room.size
                   for one_room in self.rooms)

    def __str__(self):
        output = 'House:\n'
        output += '\n'.join(str(one_room)
                            for one_room in self.rooms)
        return output


class Neighborhood():
    total_size = 0

    def __init__(self):
        self.houses = []

    def add_houses(self, *args):
        for one_house in args:
            self.houses.append(one_house)
            Neighborhood.total_size += one_house.size()

    def size(self):
        return sum(one_house.size()
                   for one_house in self.houses)
