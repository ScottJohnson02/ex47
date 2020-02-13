# Exercise 47: game.py
# NOTE: This should be added to the main package inside a newly created project
import random
items = ['ball', 'stick', 'cup', 'hat']


class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def loot(self):
        x = random.randint(0, (len(items) - 1))
        return items[x]
