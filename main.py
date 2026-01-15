import arcade
from pyglet.graphics import Batch
import random

from settings import *

class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.bg_texture = arcade.load_texture(MENU_BG_TEXTURE)

    def setup(self):
        """Настройка игры"""
        arcade.play_sound(MENU_SOUND, loop=True, volume=VOlUME_MUSIC) # Запускаем саунд к меню

        # Несколько сетов текстов меню, необходимых для последовательного переключения
        self.batch_set1 = Batch() # Первый сет - первая страничка меню
        self.text_set1 = (arcade.Text("SINGLE PLAYER", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[0] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set1),
                          arcade.Text("SETTINGS", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[1] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set1),
                          arcade.Text("EXIT GAME", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[2] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set1))

        self.batch_set2 = Batch() # Второй сет - если выбрали одиночную игру (пока не работает)
        self.text_set2 = (arcade.Text("CLASSIC LEVELS", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[0] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set2),
                          arcade.Text("PLAY DUEL", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[1] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set2),
                          arcade.Text("THE SHOP", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[2] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set2),
                          arcade.Text("BACK", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[3] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set2))

        self.batch_set3 = Batch() # Третий сет - если выбрали настройки (пока не работают)
        self.text_set3 = (arcade.Text("Screen SIZE", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[0] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set3),
                          arcade.Text("Music VOLUME", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[1] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set3),
                          arcade.Text("Effects VOLUME", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[2] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set3),
                          arcade.Text("DIFFICULTY", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[3] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set3),
                          arcade.Text("BACK", MENU_BTN_TEXT_X,
                                      self.height * MENU_BTN_RECTS_BOTTOMS[4] + 25,
                                      arcade.color.BRONZE, font_size=55, width=500,
                                      anchor_x="center", batch=self.batch_set3))

        self.now_set = self.text_set1 # текущий сет
        self.now_set_batch = self.batch_set1 # батч текущего сета

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.bg_texture,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2,
                                                  self.width, self.height)) # BG

        for i in range(len(self.now_set)): # прямоугольники под тексты
            arcade.draw_lbwh_rectangle_filled(MENU_BTN_RECTS_LEFT,
                                              self.height * MENU_BTN_RECTS_BOTTOMS[i],
                                              500, 100, (255, 255, 255,
                                                         MENU_BTN_RECTS_ALPHAS[i]))

        self.now_set_batch.draw() # тексты

    def on_mouse_motion(self, x, y, dx, dy):
        """Обработка движения мыши"""
        if not (MENU_BTN_RECTS_LEFT <= x <= 651):
            MENU_BTN_RECTS_ALPHAS[:] = [0, 0, 0, 0, 0, 0]
            return # Если мышь не попадает в возможные коор. по X,
            # то сразу альфа-канал всех кнопок = 0 и выходим из функции
        count_prov = len(self.now_set)
        if 50 in MENU_BTN_RECTS_ALPHAS[count_prov:]:
            for i in range(count_prov, 6): # Если рисующихся прямоугольников меньше
                MENU_BTN_RECTS_ALPHAS[i] = 0 # то альфа-канал оставшихся = 0
        for prov in range(count_prov):
            btn_bottom = self.height * MENU_BTN_RECTS_BOTTOMS[prov]
            if btn_bottom <= y <=btn_bottom + 101:
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
        if not (MENU_BTN_RECTS_LEFT <= x <= 651):
            return # так же если мышь не попадёт ни по одной кнопке по X
        count_prov = len(self.now_set) # кол-во проверок (кнопок)
        for prov in range(count_prov):
            btn_bottom = self.height * MENU_BTN_RECTS_BOTTOMS[prov]
            if btn_bottom <= y <= btn_bottom + 101:
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
                else: # Звук запрета, тк пока код не прописан
                    arcade.play_sound(MENU_NOT_EVENT_S, volume=VOlUME_EFFECTS)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT,
                           TITLE, fullscreen=True)
    main_view = MainMenuView()
    main_view.setup()
    window.show_view(main_view)
    arcade.run()


if __name__ == "__main__":
    main()
