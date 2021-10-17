import pygame
import random
import math


class Blob:
    def __init__(
            self,
            x,
            y,
            speed=4,
            num_days_without_food=1,
            sense=3,
            num_babies=1,
            lifespan=5):
        self.num_babies = num_babies
        self.num_days_without_food = num_days_without_food
        self.sense = sense
        self.speed = speed
        self.lifespan = lifespan
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Blob({self.x}, {self.y}, {self.speed}, {self.num_days_without_food}, {self.sense},' \
               f'{self.num_babies}, {self.lifespan})'


class Food:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


# MAIN VARIABLES
Movement = 5.00

pygame.init()
pygame.display.init()
Screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("The Evolution Game")
FoodPic = pygame.image.load('food - Copy.png')
BlobPic = pygame.image.load('blob - Copy.png')


def make_blob_pic(x, y):
    Screen.blit(BlobPic, (x, y))


def make_food_pic(x, y):
    Screen.blit(FoodPic, (x, y))


TheBlobs = []


def make_blobs():
    for x in range(1, 10):
        x_position = random.randint(50, 850)
        y_position = random.randint(50, 750)
        TheBlobs.append(Blob(x_position, y_position))


TheFoods = []


def distance(theblobX, theblobY, thefoodX, thefoodY):
    return math.sqrt(math.pow(thefoodX - theblobX, 2) + math.pow(thefoodY - theblobY, 2))


def make_food():
    for x in range(9):
        x_position = random.randint(50, 850)
        y_position = random.randint(50, 750)
        TheFoods.append(Food(x_position, y_position))


make_food()
make_blobs()
running = True
while running:
    Screen.fill((0, 0, 0))

    Screen.blit(BlobPic, (0, 0))
    for a in TheBlobs:
        make_blob_pic(a.X, a.Y)
    for b in TheFoods:
        make_food_pic(b.X, b.Y)

    for c in TheBlobs:
        xPosition2 = c.getX()
        yPosition2 = c.getY()

        XheadsTails = random.randint(0, 2)
        YheadsTails = random.randint(0, 2)
        if XheadsTails > 1:
            xPosition2 += Movement
        if XheadsTails < 1:
            xPosition2 -= Movement
        if YheadsTails > 1:
            yPosition2 += Movement
        if YheadsTails < 1:
            yPosition2 -= Movement
        if xPosition2 > 850:
            xPosition2 = 850
        if xPosition2 < 0:
            xPosition2 = 0
        if yPosition2 > 750:
            yPosition2 = 750
        if yPosition2 < 0:
            yPosition2 = 0
        for d in TheFoods:
            i = 0
            if distance(xPosition2, yPosition2, d.getX(),d.getY()) < 8:
                TheFoods.pop(i)
        c.setX(xPosition2)
        c.setY(yPosition2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        continue
    pygame.display.update()
