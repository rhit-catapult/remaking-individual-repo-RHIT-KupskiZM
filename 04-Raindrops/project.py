import pygame
import sys
import time
import hero_module
import cloud_module


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("anvil drop")
    fps = pygame.time.Clock()
    mike = hero_module.Hero(screen,200,400, with_umbrella_filename= "Mike_umbrella.png", without_umbrella_filename= "Mike.png")
    alyssa = hero_module.Hero(screen, 700,400, with_umbrella_filename= "Alyssa_umbrella.png", without_umbrella_filename= "Alyssa.png")
    cloud = cloud_module.Cloud(screen, 300, 50, image_filename= "cloud.png")
    while True:
        fps.tick(60)
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                cloud.x = mouse_pos[0]-150
                cloud.y = mouse_pos[1]-50
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
        pygame.display.update()

main()