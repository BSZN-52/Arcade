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
...

'''enemies'''
...

'''weapons'''
...
