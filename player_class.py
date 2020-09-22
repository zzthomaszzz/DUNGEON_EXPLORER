from animation import *


class Player:
    def __init__(self, x, y, width, height, tick):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # ------------------------- Walk right animation ------------------------- #
        self.walking_right_animation = load_animation("Data/image/walking_right")
        self.tick_walking_right = tick
        self.count_walking_right = 0
        self.image_walking_right = 0
        # Core Stuff here. Mainly used for animate function
        self.walk_right = [self.walking_right_animation, self.tick_walking_right,
                           self.count_walking_right, self.image_walking_right]
        # ------------------------------------------------------------------------ #
        # ------------------------- Walk left animation  ------------------------- #
        self.walking_left_animation = load_animation("Data/image/walking_left")
        self.tick_walking_left = tick
        self.count_walking_left = 0
        self.image_walking_left = 0
        # Core stuff here, again.
        self.walk_left = [self.walking_left_animation, self.tick_walking_left,
                          self.count_walking_left, self.image_walking_left]
        # ------------------------------------------------------------------------ #
        # ------------------------- Standing left animation ---------------------- #
        self.standing_left_animation = load_animation("Data/image/standing_left")
        self.tick_standing_left = tick
        self.count_standing_left = 0
        self.image_standing_left = 0
        # Core
        self.stand_left = [self.standing_left_animation, self.tick_standing_left,
                           self.count_standing_left, self.image_standing_left]
        # ------------------------------------------------------------------------ #
        # ------------------------- Standing right animation --------------------- #
        self.standing_right_animation = load_animation("Data/image/standing_right")
        self.tick_standing_right = tick
        self.count_standing_right = 0
        self.image_standing_right = 0
        # Core
        self.stand_right = [self.standing_right_animation, self.tick_standing_right,
                            self.count_standing_right, self.image_standing_right]
        # ------------------------------------------------------------------------ #
        # -------------------------------- MISC ---------------------------------- #
        self.m_right = False
        self.m_left = False
        self.face_left = False
        # This value is true so the player will be facing right when the game start
        self.face_right = True
        self.coor = (self.x, self.y, self.width, self.y)

    # ----------------------------- Animation function ------------------------------- #
    def animate(self, surface, name_list):
        self.coor = (self.x, self.y, self.width, self.y)
        surface.blit(name_list[0][name_list[3]], self.coor)
        name_list[2] += 1
        if name_list[2] == name_list[1]:
            name_list[3] += 1
            name_list[2] = 0
        if name_list[3] == len(name_list[0]):
            name_list[3] = 0
