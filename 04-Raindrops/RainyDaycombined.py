import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(1,5)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        self.speed *= 1.04
        # if self.speed > 50:
        #     self.speed = 50
        self.y += self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        return self.y > self.screen.get_height()

    def draw(self):
        """ Draws this sprite onto the screen. """
        pygame.draw.line(self.screen, (100,100,210),(self.x,self.y),(self.x,self.y - 5),2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen    #     - Store the screen.
        self.x = x
        self.y = y  #     - Set the initial position of this Hero to x and y.
        self.with_umbrella_filename = pygame.image.load(with_umbrella_filename)
        self.without_umbrella_filename = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0
    def draw(self):
        """ Draws this sprite onto the screen. """
      #  self.screen.blit(self.without_umbrella_filename, (self.x, self.y))
        if time.time() > self.last_hit_time + .5:
            self.screen.blit(self.without_umbrella_filename, (self.x, self.y))
        else:
            self.screen.blit(self.with_umbrella_filename, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        hit_box = pygame.Rect(self.x,self.y,self.without_umbrella_filename.get_width(),self.without_umbrella_filename.get_height())
        return hit_box.collidepoint(raindrop.x, raindrop.y)

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


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("anvil drop")
    fps = pygame.time.Clock()
    # testdrop = Raindrop(screen, 10,10)
    mike = Hero(screen,200,400, with_umbrella_filename= "Mike_umbrella.png", without_umbrella_filename= "Mike.png")
    alyssa = Hero(screen, 700,400, with_umbrella_filename= "Alyssa_umbrella.png", without_umbrella_filename= "Alyssa.png")
    cloud = Cloud(screen, 300, 50, image_filename= "cloud.png")
    #debounce = 0
    while True:
        fps.tick(60)
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # and debounce == 0:
                mouse_pos = pygame.mouse.get_pos()
                cloud.x = mouse_pos[0]-150
                cloud.y = mouse_pos[1]-50
               # debounce = 1
            # if event.type == pygame.MOUSEBUTTONUP and debounce == 1:
                #debounce = 0
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 10
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 10
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 10
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 10
        if cloud.x < 0:
            cloud.x = 0
        elif cloud.x > 700:
            cloud.x = 700
        if cloud.y < 0:
            cloud.y = 0
        if cloud.y > 300:
            cloud.y = 300

            # --- begin area of test_drop code that will be removed later

        # if mike.hit_by(testdrop):
        #     mike.last_hit_time = time.time()
        # if alyssa.hit_by(testdrop):
        #     alyssa.last_hit_time = time.time()
        cloud.draw()
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.draw()
            raindrop.move()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
               cloud.raindrops.remove(raindrop)
            if raindrop.y > 700:
                raindrop.y = 1
        alyssa.draw()
        mike.draw()
            # TODO: Make the Cloud "rain", then:
            # TODO    For each Raindrop in the Cloud's list of raindrops:
                #       - move the Raindrop.
                #       - draw the Raindrop.
                # TODO  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
                # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.

        pygame.display.update()

main()
