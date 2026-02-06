import sys

import arcade
from arcade.examples.drawing_primitives import point_list
from pyglet.graphics import Batch
import random

from settings import *
from gun import *
from player import *
from levels_locations import *

window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT,
                       TITLE, fullscreen=True)


class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.bg_texture = arcade.load_texture(MENU_BG_TEXTURE)

        self.player_menu = arcade.play_sound(MENU_SOUND, loop=True, volume=VOlUME_MUSIC) # Запускаем саунд к меню
        self.diff = 1

        self.menu_btn_text_x = int((self.width + self.height) / 7.5)
        self.menu_btn_rects_l = int(self.menu_btn_text_x * 0.375)
        self.menu_btn_width = int((self.width + self.height) / 6)
        self.menu_btn_height = int(self.menu_btn_width / 5)
        self.menu_btn_font_size = int(self.menu_btn_height / 2 * 1.1)

    def set_objects_size(self):
        self.menu_btn_text_x = int((self.width + self.height) / 7.5)
        self.menu_btn_rects_l = int(self.menu_btn_text_x * 0.375)
        self.menu_btn_width = int((self.width + self.height) / 6)
        self.menu_btn_height = int(self.menu_btn_width / 5)
        self.menu_btn_font_size = int(self.menu_btn_height / 2 * 1.1)

        self.setup()

    def setup(self):
        """Настройка игры"""

        # Несколько сетов текстов меню, необходимых для последовательного переключения
        self.batch_set1 = Batch() # Первый сет - первая страничка меню
        self.text_set1 = (arcade.Text("SINGLE PLAYER", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[0] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set1),
                          arcade.Text("SETTINGS", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[1] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set1),
                          arcade.Text("EXIT GAME", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[2] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set1))

        self.batch_set2 = Batch() # Второй сет - если выбрали одиночную игру (пока не работает)
        self.text_set2 = (arcade.Text("CLASSIC LEVEL1", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[0] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set2),
                          arcade.Text("PLAY DUEL", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[1] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set2),
                          arcade.Text("THE SHOP", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[2] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set2),
                          arcade.Text("BACK", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[3] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set2))

        self.batch_set3 = Batch() # Третий сет - если выбрали настройки (пока не работают)
        self.text_set3 = (arcade.Text("Screen SIZE", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[0] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set3),
                          arcade.Text("Music VOLUME", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[1] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set3),
                          arcade.Text("Effects VOLUME", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[2] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set3),
                          arcade.Text("DIFFICULTY", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[3] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set3),
                          arcade.Text("BACK", self.menu_btn_text_x,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[4] + self.menu_btn_height // 4,
                                      arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                      width=self.menu_btn_width,
                                      anchor_x="center", batch=self.batch_set3))

        self.batch_set_size_setting = Batch() # сет вариантов размера экрана
        self.text_set_size_setting = (arcade.Text("FullScreen", self.menu_btn_text_x,
                                                  self.height * MENU_BTN_RECTS_BOTTOMS[0] + self.menu_btn_height // 4,
                                                  arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                                  width=self.menu_btn_width,
                                                  anchor_x="center", batch=self.batch_set_size_setting),
                                      arcade.Text("1920 X 1080", self.menu_btn_text_x,
                                                  self.height * MENU_BTN_RECTS_BOTTOMS[1] + self.menu_btn_height // 4,
                                                  arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                                  width=self.menu_btn_width,
                                                  anchor_x="center", batch=self.batch_set_size_setting),
                                      arcade.Text("1280 X 720", self.menu_btn_text_x,
                                                  self.height * MENU_BTN_RECTS_BOTTOMS[2] + self.menu_btn_height // 4,
                                                  arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                                  width=self.menu_btn_width,
                                                  anchor_x="center", batch=self.batch_set_size_setting),
                                      arcade.Text("1440 X 900", self.menu_btn_text_x,
                                                  self.height * MENU_BTN_RECTS_BOTTOMS[3] + self.menu_btn_height // 4,
                                                  arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                                  width=self.menu_btn_width,
                                                  anchor_x="center", batch=self.batch_set_size_setting))

        self.batch_set_difficulty = Batch()  # сет вариантов размера экрана
        self.text_set_difficulty = (arcade.Text("Easy", self.menu_btn_text_x,
                                                  self.height * MENU_BTN_RECTS_BOTTOMS[0] + self.menu_btn_height // 4,
                                                  arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                                  width=self.menu_btn_width,
                                                  anchor_x="center", batch=self.batch_set_difficulty),
                                      arcade.Text("Medium", self.menu_btn_text_x,
                                                  self.height * MENU_BTN_RECTS_BOTTOMS[1] + self.menu_btn_height // 4,
                                                  arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                                  width=self.menu_btn_width,
                                                  anchor_x="center", batch=self.batch_set_difficulty),
                                      arcade.Text("Hard", self.menu_btn_text_x,
                                                  self.height * MENU_BTN_RECTS_BOTTOMS[2] + self.menu_btn_height // 4,
                                                  arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                                  width=self.menu_btn_width,
                                                  anchor_x="center", batch=self.batch_set_difficulty),
                                      arcade.Text("Classic", self.menu_btn_text_x,
                                                  self.height * MENU_BTN_RECTS_BOTTOMS[3] + self.menu_btn_height // 4,
                                                  arcade.color.BRONZE, font_size=self.menu_btn_font_size,
                                                  width=self.menu_btn_width,
                                                  anchor_x="center", batch=self.batch_set_difficulty))

        self.now_set = self.text_set1 # текущий сет
        self.now_set_batch = self.batch_set1 # батч текущего сета

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.bg_texture,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2,
                                                  self.width, self.height)) # BG

        for i in range(len(self.now_set)): # прямоугольники под тексты
            arcade.draw_lbwh_rectangle_filled(self.menu_btn_rects_l,
                                              self.height * MENU_BTN_RECTS_BOTTOMS[i],
                                              self.menu_btn_width, self.menu_btn_height,
                                              (255, 255, 255,
                                               MENU_BTN_RECTS_ALPHAS[i]))

        self.now_set_batch.draw() # тексты

    def on_mouse_motion(self, x, y, dx, dy):
        """Обработка движения мыши"""
        if not (self.menu_btn_rects_l <= x <= self.menu_btn_rects_l + self.menu_btn_width):
            MENU_BTN_RECTS_ALPHAS[:] = [0, 0, 0, 0, 0, 0]
            return # Если мышь не попадает в возможные коор. по X,
            # то сразу альфа-канал всех кнопок = 0 и выходим из функции
        count_prov = len(self.now_set)
        if 50 in MENU_BTN_RECTS_ALPHAS[count_prov:]:
            for i in range(count_prov, 6): # Если рисующихся прямоугольников меньше
                MENU_BTN_RECTS_ALPHAS[i] = 0 # то альфа-канал оставшихся = 0
        for prov in range(count_prov):
            btn_bottom = self.height * MENU_BTN_RECTS_BOTTOMS[prov]
            if btn_bottom <= y <=btn_bottom + self.menu_btn_height:
                if MENU_BTN_RECTS_ALPHAS[prov] == 0: # Если мышь на кнопке впервый раз
                                                     # после зажигания
                    arcade.play_sound(MENU_MOVE_OPTION_S, volume=VOlUME_EFFECTS)
                    # звук наведения на кнопку
                MENU_BTN_RECTS_ALPHAS[prov] = 50
                return
            else:
                MENU_BTN_RECTS_ALPHAS[prov] = 0 # если мыши нет на кнопке

    def on_mouse_press(self, x, y, button, modifiers):
        """Обработка клика мышью"""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        if not (self.menu_btn_rects_l <= x <= self.menu_btn_rects_l + self.menu_btn_width):
            return # так же если мышь не попадёт ни по одной кнопке по X
        count_prov = len(self.now_set) # кол-во проверок (кнопок)
        for prov in range(count_prov):
            btn_bottom = self.height * MENU_BTN_RECTS_BOTTOMS[prov]
            if btn_bottom <= y <= btn_bottom + self.menu_btn_height:
                arcade.play_sound(MENU_CLICK_S, volume=VOlUME_EFFECTS) # Звук нажатия кнопки
                text =  self.now_set[prov].text
                if text == 'BACK':
                    self.now_set_batch = self.batch_set1
                    self.now_set = self.text_set1
                    return # сразу проверим Back, тк она есть в 2х сетах
                elif self.now_set_batch == self.batch_set1:
                    if text == 'SINGLE PLAYER':
                        self.now_set_batch = self.batch_set2
                        self.now_set = self.text_set2
                        return
                    elif text == 'SETTINGS':
                        self.now_set_batch = self.batch_set3
                        self.now_set = self.text_set3
                        return
                    else: # последняя кнопка - выход
                        self.window.close()
                elif self.now_set_batch == self.batch_set2:
                    if text == 'CLASSIC LEVEL1':
                        arcade.stop_sound(self.player_menu)
                        game_view = MainGameView(self.width, self.height,
                                                 TITLE, level1, self.diff)
                        game_view.setup()
                        self.window.show_view(game_view)
                        return
                    arcade.play_sound(MENU_NOT_EVENT_S)
                elif self.now_set_batch == self.batch_set3:
                    if text == 'Screen SIZE':
                        self.now_set_batch = self.batch_set_size_setting
                        self.now_set = self.text_set_size_setting
                        return
                    elif text == 'DIFFICULTY':
                        self.now_set_batch = self.batch_set_difficulty
                        self.now_set = self.text_set_difficulty
                        return
                    arcade.play_sound(MENU_NOT_EVENT_S, volume=VOlUME_EFFECTS)
                elif self.now_set_batch == self.batch_set_size_setting:
                    if text == 'FullScreen':
                        self.window.set_fullscreen(True)
                    else:
                        self.window.set_fullscreen(False)
                        w, h = text.split(' X ')
                        self.window.set_size(int(w), int(h))
                    self.set_objects_size()
                    return
                elif self.now_set_batch == self.batch_set_difficulty:
                    if text == 'Easy':
                        self.diff = 0
                    elif text == 'Medium':
                        self.diff = 1
                    elif text == 'Hard':
                        self.diff = 1.5
                    elif text == 'Classic':
                        self.diff = 2.5
                    self.now_set = self.text_set1
                    self.now_set_batch = self.batch_set1
                else: # Звук запрета, тк пока код не прописан
                    arcade.play_sound(MENU_NOT_EVENT_S, volume=VOlUME_EFFECTS)


class MainGameView(arcade.View):
    def __init__(self, width, height, title, level, diff):
        super().__init__()
        self.level = level
        self.player = Player('No-name', diff,
                             [CLASSIC_GUN, QUICKSHOTER, SHOTGUN],
                             100, CLASSIC_GUN, QUICKSHOTER, SHOTGUN,
                             revolve_patrons=40 - 10 * diff, shotgun_patrons=12)
        self.kils = 0
        self.time = 0
        self.is_pause = False
        self.pric_center = (0, 0)
        self.pric_lines_size = ((self.width + self.height) // 120,
                                (self.width + self.height) // 1500)
        self.or_razb = self.player.right_hand.spread
        self.max_enemy = 2
        self.now_enemy = 0
        self.time_bef_spawn = 0
        window.set_mouse_visible(False)

        self.player_game = arcade.play_sound(FIGHT_THEME_S, loop=True, volume=VOlUME_MUSIC)

    def setup(self):
        self.bottom_bg = (self.width + self.height) // 13

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.level.now_location.bg_texture,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2 + self.bottom_bg // 2,
                                                  self.width, self.height - self.bottom_bg)) # BG
        self.level.now_location.objects.draw()

        arcade.draw_lbwh_rectangle_filled(0, 0, self.width, self.bottom_bg, arcade.color.BLACK)
        if self.is_pause:
            arcade.draw_lbwh_rectangle_filled(0, 0, self.width, self.height, (0, 0, 0, 160))
        else:
            arcade.draw_line(self.pric_center[0] - self.pric_lines_size[0] - self.or_razb,
                             self.pric_center[1], self.pric_center[0] - self.or_razb, self.pric_center[1],
                             arcade.color.WHITE, self.pric_lines_size[1]) # левая линия прицела
            arcade.draw_line(self.pric_center[0] + self.or_razb, self.pric_center[1],
                             self.pric_center[0] + self.or_razb + self.pric_lines_size[0],
                             self.pric_center[1], arcade.color.WHITE,
                             self.pric_lines_size[1]) # правая линия прицела
            arcade.draw_line(self.pric_center[0], self.pric_center[1] + self.or_razb,
                             self.pric_center[0], self.pric_center[1] + self.or_razb + self.pric_lines_size[0],
                             arcade.color.WHITE, self.pric_lines_size[1]) # верхняя линия прицела
            arcade.draw_line(self.pric_center[0], self.pric_center[1] - self.or_razb - self.pric_lines_size[0],
                             self.pric_center[0], self.pric_center[1] - self.or_razb,
                             arcade.color.WHITE, self.pric_lines_size[1]) # нижняя линия прицела


    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.play_sound(PAUSE_PRESS_SOUND)
            if self.is_pause:
                self.is_pause = False
                self.player_game.play()
                window.set_mouse_visible(False)
            else:
                self.is_pause = True
                arcade.stop_sound(self.player_game)
                window.set_mouse_visible(True)
                return
        if self.is_pause:
            if symbol == arcade.key.F5:
                self.window.close()
            return
        if symbol == arcade.key.KEY_1:
            self.player.left_hand = None
            self.player.right_hand = self.player.left_gun
            return
        if symbol == arcade.key.KEY_2:
            self.player.left_hand = None
            self.player.right_hand = self.player.right_gun
            return
        if symbol == arcade.key.KEY_3:
            self.player.left_hand = self.player.left_gun
            self.player.right_hand = self.player.right_gun
            return
        if symbol == arcade.key.KEY_4:
            self.player.left_hand = None
            self.player.right_hand = self.player.two_hands_gun
            return

    def on_update(self, delta_time: float):
        if self.is_pause:
            return
        self.time += delta_time
        self.time_bef_spawn += delta_time
        if self.time_bef_spawn >= self.level.now_location.time_to_sp_enemy and self.now_enemy < self.max_enemy:
            self.time_bef_spawn = 0
            self.level.now_location.spawn_enemy()
            self.now_enemy += 1
        for s in self.level.now_location.objects:
            if s.is_enemy():
                s.update()

    def on_mouse_motion(self, x, y, dx, dy):
        if self.is_pause:
            return
        self.pric_center = (x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.is_pause:
            return
        if button not in (arcade.MOUSE_BUTTON_LEFT, arcade.MOUSE_BUTTON_RIGHT):
            return
        if self.player.left_hand:
            if button == arcade.MOUSE_BUTTON_LEFT:
                points_shot = self.player.left_hand.shot(int(x), int(y))
                hand = self.player.left_hand
            elif button == arcade.MOUSE_BUTTON_RIGHT:
                points_shot = self.player.right_hand.shot(int(x), int(y))
                hand = self.player.right_hand
        else:
            points_shot = self.player.right_hand.shot(int(x), int(y))
            hand = self.player.right_hand
        if not points_shot:
            return
        else:
            for p in points_shot:
                for s in self.level.now_location.objects:
                    if s.is_within_sprite(p):
                        if s.is_enemy():
                            s.get_damage(hand.damage - 10 * self.player.difficulty)


def main():
    main_view = MainMenuView()
    main_view.setup()
    window.show_view(main_view)
    arcade.run()


if __name__ == "__main__":
    main()
