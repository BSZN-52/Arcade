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

'''menu design'''
MENU_BG_TEXTURE = 'images/main_menu_bg_2.jpg'
MENU_BTN_RECTS_LEFT = 150
MENU_BTN_TEXT_X = 400
MENU_BTN_RECTS_BOTTOMS = (0.8, 0.68, 0.56, 0.44, 0.32, 0.2)
MENU_BTN_RECTS_ALPHAS = [0, 0, 0, 0, 0, 0]
