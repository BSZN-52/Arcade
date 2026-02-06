from http.server import nobody
from random import randint
import arcade
import math
import random
from enum import Enum

from settings import (REVOLVE_SHOT_S, RIFLE_SHOT_S, SHOTGUN_SHOT_S,
                      REVOLVE_RELOAD_S, RIFLE_RELOAD_S, RIFLE_LOAD_S,
                      SHOTGUN_RELOAD_S)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class WeaponType(Enum):
    """Типы оружия"""
    ONE_HANDED = 1
    TWO_HANDED = 2


class WeaponState(Enum):
    """Состояния оружи"""
    READY = 1
    RELOADING = 2
    SHOOTING = 3
    COCKING = 4


class Bullet(arcade.Sprite):  # хз пока что!
    ...

# нужны текстуры пули


class Weapon:
    """Базовый класс оружия"""

    def __init__(self, name, weapon_type, damage, fire_rate, reload_time,
                 magazine_size, spread, bullet_speed, magazine_textures,
                 shot_sound=None, reload_sound=None, bullets_per_shot=1, load_sound=None):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.fire_rate = fire_rate  # Интервал между выстрелами (секунды)
        self.reload_time = reload_time
        self.magazine_size = magazine_size
        self.current_ammo = magazine_size
        self.spread = spread  # Разброс в градусах
        self.bullet_speed = bullet_speed
        self.bullets_per_shot = bullets_per_shot
        self.shot_sound = shot_sound
        self.reload_sound = reload_sound
        self.load_sound = load_sound

        self.state = WeaponState.READY
        self.time_since_last_shot = fire_rate  # Готово стрелять сразу
        self.reload_progress = 0

    def can_shot(self):
        return (self.state == WeaponState.READY and
                self.current_ammo > 0 and
                self.time_since_last_shot >= self.fire_rate)

    def shot(self, x, y):
        if not self.can_shot():
            return
        self.current_ammo -= 1
        self.time_since_last_shot = 0
        shot_points = []
        for i in range(self.bullets_per_shot):
            shot_points.append((randint(x - self.spread, x + self.spread),
                                randint(y - self.spread, y + self.spread)))
        arcade.play_sound(self.shot_sound)
        return shot_points

    def _after_shot(self):
        """Действия после выстрела (переопределяется)"""
        pass

    def start_reload(self):
        """Начать перезарядку"""
        if self.current_ammo < self.magazine_size and self.state != WeaponState.RELOADING:
            self.state = WeaponState.RELOADING
            self.reload_progress = 0
            self.re_pl = arcade.play_sound(self.reload_sound, loop=True)
            return True
        return False

    def update(self, delta_time):
        """Обновление оружия"""
        self.time_since_last_shot += delta_time
        if self.name == 'Rifle':
            if self.fire_rate > self.time_since_last_shot >= self.fire_rate * 0.3:
                arcade.play_sound(self.load_sound)
        elif self.time_since_last_shot >= self.fire_rate:
            self.state = WeaponState.READY

        # Обработка перезарядки
        if self.state == WeaponState.RELOADING:
            self.reload_progress += delta_time
            if self.reload_progress >= self.reload_time:
                self._finish_reload()

    def _finish_reload(self):
        """Завершение перезарядки"""
        self.current_ammo = self.magazine_size
        arcade.stop_sound(self.re_pl)
        self.state = WeaponState.READY
        self.reload_progress = 0


CLASSIC_GUN = Weapon('Classic gun', WeaponType.ONE_HANDED, 55,
                     1.5, 5, 6, 15, 0,
                     ['images/revolve_6_pt', 'images/revolve_5_pt',
                      'images/revolve_4_pt', 'images/revolve_3_pt', 'images/revolve_2_pt',
                      'images/revolve_1_pt', 'images/revolve_0_pt'],
                     shot_sound=REVOLVE_SHOT_S, reload_sound=REVOLVE_RELOAD_S)
QUICKSHOTER = Weapon('Quickshoter', WeaponType.ONE_HANDED, 40,
                     1, 3, 6, 18, 0,
                     ['images/revolve_6_pt', 'images/revolve_5_pt',
                      'images/revolve_4_pt', 'images/revolve_3_pt', 'images/revolve_2_pt',
                      'images/revolve_1_pt', 'images/revolve_0_pt'],
                     shot_sound=REVOLVE_SHOT_S, reload_sound=REVOLVE_RELOAD_S)
SHOTGUN = Weapon('Shotgun', WeaponType.TWO_HANDED, 18,
                 0.2, 2.5, 2, 30, 0,
                 ['images/shotgun_2_pt', 'images/shotgun_1_pt',
                  'images/shotgun_0_pt'],
                 bullets_per_shot=6, shot_sound=SHOTGUN_SHOT_S, reload_sound=SHOTGUN_RELOAD_S)
SAWED_OFF = Weapon('Sawed-off', WeaponType.ONE_HANDED, 17,
                   0.3, 2.8, 2, 34, 0,
                   ['images/shotgun_2_pt', 'images/shotgun_1_pt',
                    'images/shotgun_0_pt'],
                    bullets_per_shot=6, shot_sound=SHOTGUN_SHOT_S, reload_sound=SHOTGUN_RELOAD_S)
RIFLE = Weapon('Rifle', WeaponType.ONE_HANDED, 115,
               2.2, 8, 8, 4, 0,
               ['images/rifle_pt'],
               shot_sound=RIFLE_SHOT_S, reload_sound=RIFLE_RELOAD_S, load_sound=RIFLE_LOAD_S)