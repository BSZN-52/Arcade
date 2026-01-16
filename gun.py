import arcade
import math
import random
from enum import Enum

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


class Weapon:
    """Базовый класс оружия"""


    def init(self, name, weapon_type, damage, fire_rate, reload_time,
             magazine_size, spread, bullet_speed, bullets_per_shot = 1):
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

        self.state = WeaponState.READY
        self.time_since_last_shot = fire_rate  # Готово стрелять сразу
        self.reload_progress = 0


    def can_shoot(self):
        return (self.state == WeaponState.READY and
                    self.current_ammo > 0 and
                    self.time_since_last_shot >= self.fire_rate)

    def shoot(self):
