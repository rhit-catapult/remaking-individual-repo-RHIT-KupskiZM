import pygame
import random
class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(1,2)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        self.speed *= 1.04
        if self.speed > 50:
            self.speed = 50
        self.y += self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        return self.y > self.screen.get_height()

    def draw(self):
        """ Draws this sprite onto the screen. """
        pygame.draw.line(self.screen, (100,100,210),(self.x,self.y),(self.x,self.y - 5),2)
if __name__ == "__main__":
    print("rain_module is being run")