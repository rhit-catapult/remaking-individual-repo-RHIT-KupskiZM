import pygame
import time
class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
        self.x = x
        self.y = y
        self.with_umbrella_filename = pygame.image.load(with_umbrella_filename)
        self.without_umbrella_filename = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0
    def draw(self):
        """ Draws this sprite onto the screen. """
        if time.time() > self.last_hit_time + .5:
            self.screen.blit(self.without_umbrella_filename, (self.x, self.y))
        else:
            self.screen.blit(self.with_umbrella_filename, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        hit_box = pygame.Rect(self.x,self.y,self.without_umbrella_filename.get_width(),self.without_umbrella_filename.get_height())
        return hit_box.collidepoint(raindrop.x, raindrop.y)

if __name__ == "__main__":
    print("hero_module is being run")