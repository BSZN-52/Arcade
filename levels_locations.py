import arcade
from pyglet.graphics import Batch
import random

from enemy import *
from settings import *


class Level:
    def __init__(self, locations):
        self.locations = locations
        self.now_location = self.locations[0]
        self.is_finish_loc = False

    def to_next_location(self):
        if not self.now_location.is_loc_end:
            return
        self.next_location()

    def next_location(self):
        if self.is_finish_loc:
            ...
            return
        self.now_location = self.locations[self.now_location.find(self.locations) + 1]
        if self.now_location == self.locations[-1]:
            self.is_finish_loc = True


class Location:
    def __init__(self, bg_texture, objects, enemies_positions, enemies_count):
        self.bg_texture = bg_texture
        self.objects = arcade.SpriteList()
        for obj in objects:
            self.objects.append(obj)
        self.objects.sort(key=lambda x: -x.plan)
        self.enemies_positions = enemies_positions
        self.time_to_sp_enemy = 1.5
        self.enemies_count = enemies_count
        self.enemies_killed = 0
        self.is_loc_end = False

    def spawn_enemy(self):
        pos = random.choice(self.enemies_positions)
        enemy_type = random.choice(pos.enemies_types)
        enemy = enemy_type(random.randint(25, 45), pos.plan,
                           center_x=pos.coords[0], center_y=pos.coords[1])
        self.objects.append(enemy)
        self.objects.sort(key=lambda x: -x.plan)
        return pos


class EnemyPosition:
    def __init__(self, plan, coords, enemies_types):
        self.plan = plan
        self.coords = coords
        self.enemies_types = enemies_types


location1_level1 = Location(loc_1_bg, [BarrelObject(2, scale=0.6, center_x=350, center_y=290)],
                            [EnemyPosition(3, (850, 190),
                            [Enemy1, Enemy2])], 12)
level1 = Level([location1_level1])
