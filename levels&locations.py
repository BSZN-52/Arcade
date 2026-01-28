import arcade
from pyglet.graphics import Batch
import random

from settings import *


class Level:
    def __init__(self):
        self.locations = [...]
        self.now_location = self.locations[0]

    def next_location(self):
        self.now_location = self.locations[self.now_location.find(self.locations) + 1]


class Location:
    def __init__(self):
        self.bg_texture = arcade.load_texture('')
        self.objects = [...]
        self.enemies_count = ...
        self.enemies_positions = [...]


class EnemyPosition:
    def __init__(self):
        self.coords = ...
        self.enemies_types = [...]
