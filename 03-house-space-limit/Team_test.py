#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

class TooOldError(Exception):
    pass

class Team_Member:
    def __init__(self, fname,lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        return "{self.fname} {self.lname}".format(self=self)


class Team:
    def __init__(self, team_name, max_age = 100):
        self.team_name = team_name
        self.max_age = max_age
        self.members = []

    def add_member(self, *args):
        for item in args:
            if item.age + self.team_age() > self.max_age:
                raise TooOldError
            else:
                self.members.append(item)


    def team_age(self):
        return sum(item.age for item in self.members)


    def __str__(self):
        output = ("Team name: " + self.team_name + "\n")
        output += "Team age: " + str(self.team_age()) + "\n\t"
        output += '\n\t'.join(str(item) for item in self.members)
        return output


johnnyVikings = Team_Member('John', 'Paul', 34)
vikings = Team("Vikings")
vikings.add_member(johnnyVikings)

paulVikings = Team_Member("Paul", "Scott", 38)
vikings.add_member(paulVikings)

scottVikings = Team_Member("Steve", "Tony", 20)
vikings.add_member(scottVikings)

print(vikings)