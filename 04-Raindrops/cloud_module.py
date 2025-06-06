import pygame
import random
from rain_module import Raindrop
class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        self.screen = screen
        self.x = x
        self.y = y
        self.cloudimage = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        self.screen.blit(self.cloudimage, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        a = random.randint(0,self.cloudimage.get_width())
        new_drop = Raindrop(self.screen, self.x + a, self.y+ self.cloudimage.get_height()-5)
        self.raindrops.append(new_drop)

if __name__ == "__main__":
    print("cloud_module is being run")