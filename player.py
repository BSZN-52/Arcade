import sqlite3

class Profile:
    def __init__(self, name, difficulty, guns_list, money):
        self.name = name
        self.difficulty = difficulty
        self.guns_list = guns_list
        self.money = money


class Player(Profile):
    def __init__(self, name, difficulty, guns_list, money,
                 left_gun, right_gun, two_hands_gun, rifle_patrons=0,
                 revolve_patrons=0, shotgun_patrons=0):
        super().__init__(name, difficulty, guns_list, money)
        self.left_gun = left_gun
        self.right_gun = right_gun
        self.two_hands_gun = two_hands_gun
        self.rifle_patrons = rifle_patrons
        self.revolve_patrons = revolve_patrons
        self.shotgun_patrons = shotgun_patrons
        self.left_hand = None
        self.right_hand = self.left_gun


class ProfilesManager:
    def __init__(self):
        ...

    def add_profile(self):
        ...

    def del_profile(self):
        ...

    def change_profile(self):
        ...
