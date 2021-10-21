import pygame
import random
import math
import logging

logging.basicConfig(filename='log_info.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

pygame.init()

# ConstantFMos
FOOD_PIC = pygame.image.load("assets/food.png")
BLOB_PIC = pygame.image.load("assets/blob.png")
DAYS = 0
GAME_TITLE = "The Evolution Game    DAY: "
MUTATION_PERCENTAGE = .10
screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("The Evolution Game")


class Blob:
    def __init__(
            self, x, y, speed=20, num_days_without_food=1, sense=30, num_babies=1, lifespan=5, food_consumed=0,
            days_alive=0
    ):
        self.num_babies = num_babies
        self.num_days_without_food = num_days_without_food
        self.sense = sense
        self.speed = speed
        self.lifespan = lifespan
        self.food_consumed = food_consumed
        self.x = x
        self.y = y
        self.days_alive = days_alive

    def setFoodConsumed(self):
        self.food_consumed += 1

    def __repr__(self):
        return (
            f"Blob({self.speed}, {self.sense})"
        )

    def makeBaby(self):
        Baby_X_Cord = self.x
        Baby_Y_Cord = self.y

        # for now stay the same
        baby_num_days_without_food = self.num_days_without_food
        baby_num_babies = self.num_babies
        baby_life_span = self.lifespan
        baby_speed = self.speed
        baby_sense = self.speed
        # baby speed
        baby_speed_probability = random.randint(0, 2)
        if baby_speed_probability > 1:
            baby_speed = self.speed * (1 + MUTATION_PERCENTAGE)
        if baby_speed_probability < 1:
            baby_speed = self.speed / (1 + MUTATION_PERCENTAGE)
        baby_sense_probability = random.randint(0, 2)
        if baby_sense_probability > 1:
            baby_sense = self.sense * (1 + MUTATION_PERCENTAGE)
        if baby_sense_probability < 1:
            baby_sense = self.sense / (1 + MUTATION_PERCENTAGE)

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
logging.info("Arrays of blobs + foods created")

clock = pygame.time.Clock()

running = True
logging.info("creating game loops")
while running:
    pygame.display.set_caption(f"{GAME_TITLE} {DAYS}")
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
            if distance(c.x, c.y, d.x, d.y) < c.sense:
                c.setFoodConsumed()
                foods.remove(d)
        if len(foods) == 0:
            for e in blobs:
                foods: list[Food] = [Food(random.randint(50, 850), random.randint(50, 750)) for _ in range(9)]
                if e.food_consumed < 1:
                    e.food_consumed = 0
                    logging.info("Killing Blob (Reason: Starvation)")
                    blobs.remove(e)
                    e.days_alive += 1
                if e.days_alive > e.lifespan:
                    logging.info("Killing Blob (Reason: Old Age)")
                    blobs.remove(e)
                if e.food_consumed == 1:
                    e.food_consumed = 0
                if e.food_consumed > 1:
                    for _ in range(e.food_consumed // 2):
                        blobs.append(e.makeBaby())
                    logging.info("Generating New Blob")
                    e.food_consumed = 0
            logging.info(DAYS)
            DAYS += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logging.info("FINAL BLOBS: ")
            for LOL in blobs:
                logging.info(LOL.__repr__())
            running = False
            break

    pygame.display.update()
