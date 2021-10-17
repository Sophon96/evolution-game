import pygame
import random
import math

pygame.init()

# ConstantFMos
FOOD_PIC = pygame.image.load("assets/food.png")
BLOB_PIC = pygame.image.load("assets/blob.png")
DAYS = 0
MUTATION_PERCENTAGE = 10.00

screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("The Evolution Game")


class Blob:
    def __init__(
            self, x, y, speed=10, num_days_without_food=1, sense=50, num_babies=1, lifespan=5
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

    def makeBaby(self, max_mutation_percentage):
        Baby_X_Cord = self.x
        Baby_Y_Cord = self.y

        # for now stay the same
        baby_num_days_without_food = self.num_days_without_food
        baby_num_babies = self.num_babies
        baby_life_span = self.lifespan

        # baby speed
        baby_speed = 10
        baby_speed_probability = random.randint(0, 2)
        if baby_speed_probability > 1:
            baby_speed = self.speed * (1 + max_mutation_percentage)
        if baby_speed_probability < 1:
            baby_speed = self.speed / (1 + max_mutation_percentage)
        baby_sense_probability = random.randint(0, 2)
        if baby_sense_probability > 1:
            baby_sense = self.sense * (1 + max_mutation_percentage)
        if baby_sense_probability < 1:
            baby_sense = self.sense / (1 + max_mutation_percentage)

        return Blob(Baby_X_Cord, Baby_Y_Cord, baby_speed, baby_num_days_without_food, baby_sense, baby_num_babies,
                    baby_life_span)

    def blit(self):
        global screen
        screen.blit(BLOB_PIC, (self.x, self.y))


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blit(self):
        global screen
        screen.blit(FOOD_PIC, (self.x, self.y))


def distance(blob_x, blob_y, food_x, food_y):
    return math.sqrt(
        (food_x - blob_x) ** 2 + (food_y - blob_y) ** 2
    )


blobs: list[Blob] = [Blob(random.randint(50, 850), random.randint(50, 750)) for _ in range(10)]
foods: list[Food] = [Food(random.randint(50, 850), random.randint(50, 750)) for _ in range(9)]

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    screen.fill((0, 0, 0))

    for a in blobs:
        a.blit()

    for b in foods:
        b.blit()

    for c in blobs:
        x_heads_tails = random.randint(0, 2)
        if x_heads_tails > 1:
            c.x += c.speed
        elif x_heads_tails < 1:
            c.x -= c.speed

        y_heads_tails = random.randint(0, 2)
        if y_heads_tails > 1:
            c.y += c.speed
        if y_heads_tails < 1:
            c.y -= c.speed

        if c.x > 850:
            c.x = 850
        if c.x < 0:
            c.x = 0
        if c.y > 750:
            c.y = 750
        if c.y < 0:
            c.y = 0

        for d in foods:
            if distance(c.x, c.y, d.x, d.y) < 150:
                foods.remove(d)
        if len(foods) == 0:
            for e in blobs:
                print(e.__repr__())
            foods: list[Food] = [Food(random.randint(50, 850), random.randint(50, 750)) for _ in range(9)]
            DAYS += 1
            print(DAYS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.display.update()
