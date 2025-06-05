import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640,480))
    screenwidth = screen.get_width()
    screenheight = screen.get_height()
    clock = pygame.time.Clock()
    eyeLimit = 11
    eyeX = 0
    eyeY = 0
    eyeSpeed = 1
    while True:
        clock.tick(60)
        # TODO 4: Set the clock speed to 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 3: Make the eye pupils move with Up, Down, Left, and Right keys
        if event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_DOWN]:
                eyeY = eyeY + eyeSpeed
                if eyeY > eyeLimit:
                    eyeY = eyeLimit
            if pressed_keys[pygame.K_UP]:
                eyeY = eyeY - eyeSpeed
                if eyeY < -eyeLimit:
                    eyeY = -eyeLimit
            if pressed_keys[pygame.K_RIGHT]:
                eyeX = eyeX + eyeSpeed
                if eyeX > eyeLimit:
                    eyeX = eyeLimit
            if pressed_keys[pygame.K_LEFT]:
                eyeX = eyeX - eyeSpeed
                if eyeX < -eyeLimit:
                    eyeX = -eyeLimit
        screen.fill((255, 255, 255))  # white
        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (screenwidth/2, screenheight/2), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (screenwidth/2, screenheight/2), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + eyeX, 162 + eyeY), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + eyeX, 162 + eyeY), 7)  # black pupil

        # TODO 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)
        pygame.draw.circle(screen, (0,0,0), (screenwidth/2,screenheight/2), 15)
        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
        pygame.draw.rect(screen, (0,0,0), (screenwidth/4,screenheight/1.75,screenwidth/2,25))
        pygame.display.update()


main()
