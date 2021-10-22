import pygame
import random
import numpy as np

pygame.init()

# Constants
FOOD_PIC = pygame.image.load("assets/food.png")
BLOB_PIC = pygame.image.load("assets/blob.png")
MUTATION_PERCENTAGE = 0.10

screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("The Evolution Game")


class Blob(pygame.sprite.Sprite):
    def __init__(
        self,
        x,
        y,
        speed=20,
        num_days_without_food=1,
        sense=30,
        num_babies=1,
        lifespan=5,
        food_consumed=0,
        *groups: pygame.sprite.AbstractGroup,
    ):
        super().__init__(*groups)
        self.image = BLOB_PIC
        self.rect = BLOB_PIC.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(BLOB_PIC)
        self.mask_outline = self.mask.outline()

        self.num_babies = num_babies
        self.num_days_without_food = num_days_without_food
        self.sense = sense
        self.speed = speed
        self.lifespan = lifespan
        self.food_consumed = food_consumed

    def __repr__(self):
        return (
            f"Blob({self.rect.centerx}, {self.rect.centery}, {self.speed}, {self.num_days_without_food}, {self.sense}, "
            f"{self.num_babies}, {self.lifespan})"
        )

    def make_baby(self):
        baby_x_cord = self.rect.centerx
        baby_y_cord = self.rect.centery

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

        # baby sense
        baby_sense_probability = random.randint(0, 2)
        if baby_sense_probability > 1:
            baby_sense = self.sense * (1 + MUTATION_PERCENTAGE)
        if baby_sense_probability < 1:
            baby_sense = self.sense / (1 + MUTATION_PERCENTAGE)

        return Blob(
            baby_x_cord,
            baby_y_cord,
            baby_speed,
            baby_num_days_without_food,
            baby_sense,
            baby_num_babies,
            baby_life_span,
        )

    def update(self):
        x_heads_tails = random.randint(0, 2)
        if x_heads_tails > 1:
            self.rect.centerx += self.speed
        elif x_heads_tails < 1:
            self.rect.centerx -= self.speed

        y_heads_tails = random.randint(0, 2)
        if y_heads_tails > 1:
            self.rect.centery += self.speed
        if y_heads_tails < 1:
            self.rect.centery -= self.speed

        if self.rect.centerx > 850:
            self.rect.centerx = 850
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.centery > 750:
            self.rect.centery = 750
        if self.rect.centery < 0:
            self.rect.centery = 0


class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups: pygame.sprite.AbstractGroup):
        super().__init__(*groups)
        self.image = FOOD_PIC
        self.rect = FOOD_PIC.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(FOOD_PIC)


def the_dumb(g, dblob: Blob):
    f = list(g)
    f[0] += dblob.rect.topleft[0]
    f[1] += dblob.rect.topleft[1]
    return f


if __name__ == "__main__":
    blobs = pygame.sprite.RenderUpdates(
        *[Blob(random.randint(50, 850), random.randint(50, 750)) for _ in range(10)]
    )
    foods = pygame.sprite.Group(
        *[Food(random.randint(50, 850), random.randint(50, 750)) for _ in range(9)]
    )

    clock = pygame.time.Clock()
    days = 0
    running = True
    while running:
        clock.tick(60)

        screen.fill((0, 0, 0))

        blobs_updates = blobs.draw(screen)

        foods.draw(screen)

        blobs.update()

        for blob in blobs:
            for food in foods:
                blob_outline = list(
                    map(
                        the_dumb,
                        blob.mask_outline,
                        [blob for i in range(len(blob.mask_outline))],
                    )
                )
                distances = np.subtract(blob_outline, food.rect.center)
                split_distances = np.transpose(distances)
                hyps = np.hypot(split_distances[0], split_distances[1])
                if min(hyps) <= blob.sense:
                    food.kill()
                    blob.food_consumed += 1

        if len(foods) == 0:
            for e in blobs:
                if e.food_consumed < 1:
                    e.food_consumed = 0
                    e.kill()
                    continue
                elif e.food_consumed == 1:
                    e.food_consumed = 0
                elif e.food_consumed > 1:
                    baby_blob = e.make_baby()
                    blobs.add(baby_blob)
                e.food_consumed = 0

            foods = pygame.sprite.Group(
                *[
                    Food(random.randint(50, 850), random.randint(50, 750))
                    for _ in range(9)
                ]
            )
            days += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for LOL in blobs:
                    print(LOL)
                running = False
                break

        pygame.display.update()
