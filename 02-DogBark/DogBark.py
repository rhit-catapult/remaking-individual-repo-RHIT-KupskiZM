import pygame
import sys
import time
def main():
    debounce = 0
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    dog2_image = pygame.image.load("2dogs.JPG")
    dog2_image = pygame.transform.scale(dog2_image, (470,500))
    # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)

    font1 = pygame.font.SysFont("wingdings2",28)
    font2 = pygame.font.SysFont("segoeuiemoji",90)
    print(pygame.font.get_fonts())
    # TODO 4: Create a font object with a size 28 font.
    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption1 = font1.render("Two Dogs",True,(255,255,255))
    caption2 = font2.render("🐒",True,(255,255,255))
    sound1 = pygame.mixer.Sound("bark.wav")
    # TODO 8: Create a Sound object from the "bark.wav" file.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sound1.play()
                    print("brk")
            # TODO 9: Play the music (bark) if there's a mouse click.

        # Clear the screen and set the screen background
        screen.fill(WHITE)
        # Draw the image onto the screen
        screen.blit(dog2_image,(0,0))
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)
        xloc = screen.get_width() / 2 - caption1.get_width() / 2
        yloc = screen.get_height() - 35
        screen.blit(caption1,(xloc, yloc))
        screen.blit(caption2,(xloc, yloc/2))
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
