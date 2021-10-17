import pygame
import random
import math

pygame.init()

# Constants
FOOD_PIC = pygame.image.load("food - Copy.png")
BLOB_PIC = pygame.image.load("blob - Copy.png")
MOVEMENT = 5.00

screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("The Evolution Game")


class Blob:
    def __init__(
        self, x, y, speed=4, num_days_without_food=1, sense=3, num_babies=1, lifespan=5
    ):
        self.num_babies = num_babies
        self.num_days_without_food = num_days_without_food
        self.sense = sense
        self.speed = speed
        self.lifespan = lifespan
        self.x = x
        self.y = y

    def __repr__(self):
        return (
            f"Blob({self.x}, {self.y}, {self.speed}, {self.num_days_without_food}, {self.sense},"
            f"{self.num_babies}, {self.lifespan})"
        )


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_blob_pic(x, y):
    screen.blit(BLOB_PIC, (x, y))


def make_food_pic(x, y):
    screen.blit(FOOD_PIC, (x, y))


blobs: list[Blob] = []


def make_blobs():
    for x in range(1, 10):
        x_position = random.randint(50, 850)
        y_position = random.randint(50, 750)
        blobs.append(Blob(x_position, y_position))


foods: list[Food] = []


def distance(theblob_x, theblob_y, thefood_x, thefood_y):
    return math.sqrt(
        (thefood_x - theblob_x)**2 + (thefood_y - theblob_y)**2
    )


def make_food():
    for x in range(9):
        x_position = random.randint(50, 850)
        y_position = random.randint(50, 750)
        foods.append(Food(x_position, y_position))


make_food()
make_blobs()
running = True
while running:
    screen.fill((0, 0, 0))

    for a in blobs:
        make_blob_pic(a.x, a.y)
    for b in foods:
        make_food_pic(b.x, b.y)

    for c in blobs:
        x_position_2 = c.x
        y_position_2 = c.y

        x_heads_tails = random.randint(0, 2)
        y_heads_tails = random.randint(0, 2)
        if x_heads_tails > 1:
            x_position_2 += MOVEMENT
        if x_heads_tails < 1:
            x_position_2 -= MOVEMENT
        if y_heads_tails > 1:
            y_position_2 += MOVEMENT
        if y_heads_tails < 1:
            y_position_2 -= MOVEMENT
        if x_position_2 > 850:
            x_position_2 = 850
        if x_position_2 < 0:
            x_position_2 = 0
        if y_position_2 > 750:
            y_position_2 = 750
        if y_position_2 < 0:
            y_position_2 = 0

        for d in foods:
            i = 0
            if distance(x_position_2, y_position_2, d.x, d.y) < 8:
                foods.pop(i)

        c.x = x_position_2
        c.y = y_position_2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.display.update()
