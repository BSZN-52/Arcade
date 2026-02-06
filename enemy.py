import random
import arcade

from settings import *


class Enemy(arcade.Sprite):
    def __init__(self, shot_texture, walk_textures,
                 dead_texture, damage, plan, izm_coords_anim, izm_time, scale=0.7, center_x=0,
                 center_y=0, damage_coof=1, shot_time=2):
        super().__init__(scale=scale, center_x=center_x, center_y=center_y)

        self.hp = 100
        self.damage_coof = damage_coof  # коэфицент получаемого урона
        self.damage = damage
        self.izm_coords_anim = izm_coords_anim
        self.plan = plan

        self.shot_texture = shot_texture
        self.walk_textures = []
        for t in walk_textures:
            self.walk_textures.append(t)
        self.dead_texture = dead_texture

        self.texture = shot_texture
        if self.walk_textures:
            self.texture = self.walk_textures[0]
        self.current_texture = 0
        self.texture_change_time = 0
        self.texture_change_delay = 0.3
        self.shot_time = shot_time
        self.time_to_shot = 0
        self.time_to_remove = 1.5 # время исчезновения после смерти
        self.izm_coords_anim = izm_coords_anim
        self.izm_time = izm_time
        self.curr_izm_coords = 0
        self.is_going = True
        self.is_walking = True
        self.is_shot = False
        self.is_dead = False

    def update_animation(self, delta_time: float=1/60):
        if self.is_shot:
            return
        elif self.is_dead:
            if self.texture is None:
                self.texture = self.dead_texture
            else:
                self.texture = None
        elif self.is_walking:
            self.texture_change_time += delta_time
            if self.texture_change_time >= self.texture_change_delay:
                self.texture_change_time = 0
                self.current_texture += 1
                if self.current_texture >= len(self.walk_textures):
                    self.current_texture = 0
                    self.is_walking = False
                    self.is_shot = True # Не реализуем, тк нет картинок для анимаций
                    self.texture = self.shot_texture

    def get_damage(self, damage):
        self.hp -= damage * self.damage_coof
        if self.hp <= 0:
            self.is_shot = False
            self.is_dead = True
            self.texture = self.dead_texture

    def update(self, delta_time: float = 1 / 60, *args, **kwargs):
        if self.is_going:
            izm = self.izm_coords_anim * self.izm_time * delta_time
            self.center_y += izm
            self.curr_izm_coords += izm
            if self.curr_izm_coords >= self.izm_coords_anim:
                self.is_shot = True
                self.is_going = False
        if self.is_shot:
            self.time_to_shot += delta_time
            if self.time_to_shot >= self.shot_time:
                self.time_to_shot = 0
                self.shot()

    def shot(self):
        arcade.play_sound(REVOLVE_SHOT_S)
        arcade.play_sound(random.choice(HIT_SOUNDS))
        return random.randint(self.damage - 10, self.damage + 10)

    def is_enemy(self):
        return True


'''Болванки врагов'''
class Enemy1(Enemy):
    def __init__(self, damage, plan, scale=0.7, center_x=0,
                 center_y=0, damage_coof=1, shot_time=2):
        super().__init__(ENEMY1_TEXTURE, [], ENEMY1_TEXTURE,
                         damage, plan, 200, 0.5,
                         scale=scale, center_x=center_x, center_y=center_y,
                         damage_coof=damage_coof, shot_time=shot_time)
        self.is_walking = False
        self.texture = self.shot_texture


class Enemy2(Enemy):
    def __init__(self, damage, plan, scale=0.7, center_x=0,
                 center_y=0, damage_coof=1, shot_time=2):
        super().__init__(ENEMY2_TEXTURE, [], ENEMY2_TEXTURE,
                         damage, plan, 250, 0.4,
                         scale=scale, center_x=center_x, center_y=center_y,
                         damage_coof=damage_coof, shot_time=shot_time)
        self.is_walking = False
        self.texture = self.shot_texture


'''Объекты'''
class BoxObject(arcade.Sprite):
    def __init__(self, plan, scale=0.5, center_x=0, center_y=0):
        super().__init__(scale=scale, center_x=center_x, center_y=center_y)
        self.texture = BOX_TEXTURE
        self.plan = plan

    def is_enemy(self):
        return False


class BarrelObject(arcade.Sprite):
    def __init__(self, plan, scale=0.5, center_x=0, center_y=0):
        super().__init__(scale=scale, center_x=center_x, center_y=center_y)
        self.texture = BARREL_TEXTURE
        self.plan = plan

    def is_enemy(self):
        return False
