import pygame


class animation:
    # x y of 1 image of the animations
    def __init__(self, time_next_frame, x, y, number_image):
        self.time_next_frame = time_next_frame
        self.time = time_next_frame

        self.number_image = number_image

        self.x = x
        self.y = y

        self.frame = 0


    def get_mask(self, clock):

        self.time -= clock
        if self.time < 0:
            self.time += self.time_next_frame
            self.frame = (self.frame + 1) % self.number_image

        return pygame.Rect(self.frame * self.x, 0, self.x, self.y)


    def set_time(self, clock):
        self.time -= clock


    def get_mask_for_multiple_states(self, y):

        if self.time < 0:
            self.time += self.time_next_frame
            self.frame = (self.frame + 1) % self.number_image

        return pygame.Rect(self.frame * self.x, y * self.y, self.x, self.y)


"""
# exemple de code
# animation d'un nuage :

image_nuage = pygame.image.load("image/nuage.png").convert_alpha()
test_nuage = animation("image/nuage.png", 100, 340, 142, 4)

fenetre.blit(image_nuage, (800 + biais_x / 2, 50), test_nuage.get_mask(dt))
"""
