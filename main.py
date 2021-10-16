import pygame
import random
import math


class Blob:
    def __init__(self, X, Y, Speed=4, NumDaysWithoutFood=1, Sense=3, NumBabies=1, Lifespan=5):
        self.NumBabies = 1
        self.NumDaysWithoutFood = 1
        self.Sense = 3
        self.Speed = 5
        self.Lifespan = 5
        self.X = X
        self.Y = Y

    # getters
    def getSpeed(self):
        return self.Speed

    def getNumdaysWithoutFood(self):
        return self.NumDaysWithoutFood

    def getSense(self):
        return self.Sense

    def getNumBabies(self):
        return self.NumBabies

    def getLifeSpan(self):
        return self.Lifespan

    def toString(self):
        print(self.getSense())
        print(self.getSpeed())
        print(self.getNumBabies())
        print(self.getNumdaysWithoutFood())
        print(self.getLifeSpan())

class Food:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
pygame.init()
pygame.display.init()
Screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("The Evolution Game")
FoodPic = pygame.image.load('food - Copy.png')
BlobPic = pygame.image.load('blob - Copy.png')


def makeBlobPic(x, y):
    Screen.blit(BlobPic, (x, y))


def makeFoodPic(x, y):
    Screen.blit(FoodPic, (x, y))

TheBlobs = []
def makeBlobs():

    for x in range(1, 10):
        xPosition = random.randint(50, 850)
        yPosition = random.randint(50, 750)
        TheBlobs.append(Blob(xPosition, yPosition))

TheFoods = []
def makeFood():

    for x in range(9):
        xPosition = random.randint(50, 850)
        yPosition = random.randint(50, 750)
        TheFoods.append(Food(xPosition,yPosition))
makeFood()
makeBlobs()
running = True
while running:
    Screen.fill((0, 0, 0))

    Screen.blit(BlobPic, (0, 0))
    for a in TheBlobs:
        makeBlobPic(a.X, a.Y)
    for b in TheFoods:
        makeFoodPic(b.X, b.Y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        continue
    pygame.display.update()
