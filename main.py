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

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def setX(self, newX):
        self.X = newX

    def setY(self, newY):
        self.Y = newY

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
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def setX(self, newFoodX):
        X = newFoodX
    def setY(self, newFoodY):
        Y = newFoodY

# MAIN VARIABLES

Movement = 5.00

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


def distance(theblobX, theblobY, thefoodX, thefoodY):
    return math.sqrt(math.pow(thefoodX - theblobX, 2) + math.pow(thefoodY - theblobY, 2))


def makeFood():
    for x in range(9):
        xPosition = random.randint(50, 850)
        yPosition = random.randint(50, 750)
        TheFoods.append(Food(xPosition, yPosition))


makeFood()
makeBlobs()
running = True
while running:
    Screen.fill((0, 0, 0))

    for a in TheBlobs:
        makeBlobPic(a.X, a.Y)
    for b in TheFoods:
        makeFoodPic(b.X, b.Y)

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
