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


class Bullet(arcade.Sprite):  # хз пока что!


# нужны текстуры пули


class Weapon:
    """Базовый класс оружия"""

    def init(self, name, weapon_type, damage, fire_rate, reload_time,
             magazine_size, spread, bullet_speed, bullets_per_shot=1):
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
        self.recoil = 0

    def can_shoot(self):
        return (self.state == WeaponState.READY and
                self.current_ammo > 0 and
                self.time_since_last_shot >= self.fire_rate)

    def shoot(self, x, y):
        if not self.can_shoot():
            return False
        self.current_ammo -= 1
        self.time_since_last_shot = 0
        self.recoil = 10  # если будем отдачу делать потом

    def _after_shot(self):
        """Действия после выстрела (переопределяется)"""
        pass

    def start_reload(self):
        """Начать перезарядку"""
        if self.current_ammo < self.magazine_size and self.state != WeaponState.RELOADING:
            self.state = WeaponState.RELOADING
            self.reload_progress = 0
            return True
        return False

    def update(self, delta_time):
        """Обновление оружия"""
        self.time_since_last_shot += delta_time

        # Обновление визуальных эффектов
        if self.muzzle_flash_time > 0:
            self.muzzle_flash_time -= delta_time

        if self.recoil > 0:
            self.recoil -= delta_time * 30
            if self.recoil < 0:
                self.recoil = 0

        # Обработка перезарядки
        if self.state == WeaponState.RELOADING:
            self.reload_progress += delta_time
            if self.reload_progress >= self.reload_time:
                self._finish_reload()

        # Обработка взведения
        elif self.state == WeaponState.COCKING:
            if self.time_since_last_shot >= 0.3:  # Время взведения
                self.state = WeaponState.READY

        def _finish_reload(self):
            """Завершение перезарядки"""
            self.current_ammo = self.magazine_size
            self.state = WeaponState.READY
            self.reload_progress = 0
