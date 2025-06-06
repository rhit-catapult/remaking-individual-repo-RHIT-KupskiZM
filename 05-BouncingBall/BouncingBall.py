import pygame
import sys
import random

class Ballspawn:
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.balls = []
    def ballspawn(self):
        new_ball = Ball(self.screen,self.x,self.y,random.randint(3,10),random.randint(-5,5),random.randint(-5,5),(random.randint(0,200),random.randint(0,200),random.randint(0,200)))
        self.balls.append(new_ball)
class Ball:
    def __init__(self,screen,x,y,radius,speed_x,speed_y,color):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.radius)
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x - self.radius <= 0:
            self.speed_x *= -1
        if self.x + self.radius >= self.screen.get_width():
            self.speed_x *= -1
        if self.y - self.radius <= 0:
            self.speed_y *= -1
        if self.y + self.radius >= self.screen.get_height():
            self.speed_y *= -1
class Ball2:
    def __init__(self,screen):
        self.screen = screen
        self.radius = random.randint(3,10)
        self.x = random.randint(self.radius,self.screen.get_width()-self.radius)
        self.y = random.randint(self.radius,self.screen.get_height()-self.radius)
        self.speed_x = random.randint(-10,10)
        self.speed_y = random.randint(-10,10)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.radius)
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x - self.radius <= 0:
            self.speed_x *= -1
        if self.x + self.radius >= self.screen.get_width():
            self.speed_x *= -1
        if self.y - self.radius <= 0:
            self.speed_y *= -1
        if self.y + self.radius >= self.screen.get_height():
            self.speed_y *= -1
# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ballspawner = Ballspawn(screen,150,150)
    balls = []
    for k in range(50):
        k = Ball2(screen)
        balls.append(k)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 ballspawner.x = mouse_pos[0]
                 ballspawner.y = mouse_pos[1]
                 ballspawner.ballspawn()
                 print(len(ballspawner.balls))
        clock.tick(60)
        screen.fill((255,255,255))
        for ball in balls:
            ball.draw()
            ball.move()
            if ball.speed_x == 0:
                ball.speed_x = random.randint(-5,5)
            if ball.speed_y == 0:
                ball.speed_y = random.randint(-5,5)
        for ball in ballspawner.balls:
            ball.draw()
            ball.move()
            if ball.speed_x == 0:
                ball.speed_x = random.randint(-5,5)
            if ball.speed_y == 0:
                ball.speed_y = random.randint(-5,5)
        pygame.display.update()



main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
