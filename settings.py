import arcade

'''main options'''
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
TITLE = "Lethal Shot"

'''sounds volume'''
VOlUME_EFFECTS = 1.0
VOlUME_MUSIC = 1.0

'''menu sounds'''
MENU_SOUND = arcade.load_sound('sound/main_theme (2) .mp3')
MENU_CLICK_S = arcade.load_sound('sound/menu_option_select.mp3')
MENU_MOVE_OPTION_S = arcade.load_sound('sound/menu_move_option.wav')
MENU_NOT_EVENT_S = arcade.load_sound('sound/fx_buzz.wav')
BUY_IN_SHOP_S = arcade.load_sound('sound/buy_in_shop.wav')

'''main game sounds'''
FIGHT_THEME_S = arcade.load_sound('sound/fight_theme.mp3')
GAME_OVER_S = arcade.load_sound('sound/game_over.mp3')
HIT_SOUNDS = (arcade.load_sound('sound/hit1.WAV'), arcade.load_sound('sound/hit2.WAV'))
PAUSE_PRESS_SOUND = arcade.load_sound('sound/menu_settings.wav')

'''weapon sounds'''
REVOLVE_SHOT_S = arcade.load_sound('sound/shot_pistol.mp3')
RIFLE_SHOT_S = arcade.load_sound('sound/shot_vinchester.mp3')
SHOTGUN_SHOT_S = arcade.load_sound('sound/shot_shotgun.mp3')
REVOLVE_RELOAD_S = arcade.load_sound('sound/revolve_reload.wav')
RIFLE_LOAD_S = arcade.load_sound('sound/venchester_load.wav')
RIFLE_RELOAD_S = arcade.load_sound('sound/vinchester_reload.wav')
SHOTGUN_RELOAD_S = arcade.load_sound('sound/shotgun_reload.wav')

'''menu design'''
MENU_BG_TEXTURE = 'images/main_menu_bg_2.jpg'
MENU_BTN_RECTS_BOTTOMS = (0.8, 0.68, 0.56, 0.44, 0.32, 0.2)
MENU_BTN_RECTS_ALPHAS = [0, 0, 0, 0, 0, 0]

'''objects'''
BARREL_TEXTURE = arcade.load_texture('images/barrel.png',
                                     hit_box_algorithm=arcade.hitbox.algo_detailed)
BOX_TEXTURE = arcade.load_texture('images/box.png',
                                  hit_box_algorithm=arcade.hitbox.algo_detailed)
...

'''enemies'''
ENEMY1_TEXTURE = arcade.load_texture('images/enemy1.png',
                                     hit_box_algorithm=arcade.hitbox.algo_detailed)
ENEMY2_TEXTURE = arcade.load_texture('images/enemy2.png',
                                     hit_box_algorithm=arcade.hitbox.algo_detailed)
...

'''weapons'''
...

'''textures'''
loc_1_bg = arcade.load_texture('images/bg_location1.jpg')

'''functions to value'''
#числа, на которые нужно умножить сумму сторон экрана, чтобы получить нужное
#значение (в переменной значения с 0 - проценты масштаба объектов, а не с 0 -
#размеры для сторон 1920 и 1080) это нужно для маштабирования картинки
TO_03 = 0.0001
TO_06 = 0.0002
TO_037 = 0.000123
TO_038 = 0.000127
TO_027 = 0.00009
TO_028 = 0.000093

TO_270 = 0.09
TO_290 = 0.097
TO_300 = 0.1
TO_350 = 0.117
TO_370 = 0.123
TO_380 = 0.127
TO_390 = 0.13
TO_750 = 0.25
TO_780 = 0.26
TO_800 = 0.267
TO_830 = 0.277
TO_870 = 0.29
TO_900 = 0.3
TO_930 = 0.31
TO_960 = 0.32
TO_1000 = 0.333
