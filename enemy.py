import arcade


class Enemy(arcade.Sprite):
    def __init__(self, shot_texture, walk_textures,
                 dead_texture, damage, damage_coof=1, shot_time=2):
        super.__init__()

        self.hp = 100
        self.damage_coof = damage_coof  # коэфицент получаемого урона
        self.damage = damage

        self.shot_texture = arcade.load_texture(shot_texture)
        self.walk_textures = []
        for t in walk_textures:
            self.walk_textures.append(arcade.load_texture(t))
        self.dead_texture = arcade.load_texture(dead_texture)

        self.texture = self.walk_textures[0]
        self.current_texture = 0
        self.texture_change_time = 0
        self.texture_change_delay = 0.3
        self.shot_time = shot_time
        self.time_to_remove = 1.5 # время исчезновения после смерти
        self.is_walking = True
        self.is_shot = False
        self.is_dead = False

    def update_animation(self, delta_time: float=1/60):
        if self.is_shot:
            return
        elif self.is_dead:
            ...
        elif self.is_walking:
            self.texture_change_time += delta_time
            if self.texture_change_time >= self.texture_change_delay:
                self.texture_change_time = 0
                self.current_texture += 1
                if self.current_texture >= len(self.walk_textures):
                    self.current_texture = 0
                    self.is_walking = False
                    self.is_shot = True
                    self.texture = self.shot_texture

    def get_damage(self, damage):
        self.hp -= damage * self.damage_coof
        if self.hp <= 0:
            self.is_shot = False
            self.is_dead = True
            self.texture = self.dead_texture


class Object(arcade.Sprite):
    def __init__(self, texture):
        super.__init__()
        self.texture = texture
