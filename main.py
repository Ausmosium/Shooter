import pygame
from os import system
from random import random
import time
FoNt = 0
FoNtprint = 0
screenRes = [800, 800]
cell_side = (min(screenRes))*(3/32)
MIN_SIZE = [400, 400]
window = "homeScreen"


images = {
    "aim" : [pygame.image.load("assets/images/aim.png"),  0.5],
    "ammo" : [pygame.image.load("assets/images/ammo.png"),  0.5],
    "home" : [pygame.image.load("assets/images/home.png"),  0.5],
    "retry" : [pygame.image.load("assets/images/retry.png"),  0.5],
    "start" : [pygame.image.load("assets/images/start.png"),  0.5],
    "soundOn" : [pygame.image.load("assets/images/soundOn.png"),  0.5],
    "soundOff" : [pygame.image.load("assets/images/soundOff.png"),  0.5],
    "target" : [pygame.image.load("assets/images/target.png"), 0.5]
}

curImages = dict()

def imagesResize(screenRes):
    for k in images:
        curImages[k] = pygame.transform.scale(images[k][0], (min(screenRes)*images[k][1], min(screenRes)*images[k][1]))

def cls():
    system("cls")

def font(face:str, size=18, Bold = False, Italic = False):
    global FoNt
    FoNt = pygame.font.SysFont(face,size,Bold,Italic)

def printpy(text:str,coords=(100,400),color=(128,128,128), center = False, size = False):
    global FoNt,FoNtprint
    FoNtprint = FoNt.render(text, True, color)
    if size == True:
        return [FoNtprint.get_width(), FoNtprint.get_height()]
    if center == True:
        screen.blit(FoNtprint, [coords[0]-FoNtprint.get_width()/2, coords[1]-FoNtprint.get_height()/2])
    else:
        screen.blit(FoNtprint, coords)


if __name__ == "__main__":
    frameRate = 1000
    dt = 1/1000
    pygame.init()
    screen = pygame.display.set_mode(screenRes, pygame.RESIZABLE)
    icon = pygame.image.load('assets/images/icon.png')
    pygame.display.set_caption("Shooter")
    pygame.display.set_icon(icon)
    cls()
    running = True
    clock = pygame.time.Clock()
    while running == True:
        initTime = time.time()
        clock.tick(frameRate*1.5)
        screenRes = list(screen.get_size())
        tempScreen_res = list(screenRes)
        screenRes[0] = MIN_SIZE[0] if screenRes[0] < MIN_SIZE[0] else screenRes[0]
        screenRes[1] = MIN_SIZE[1] if screenRes[1] < MIN_SIZE[1] else screenRes[1]
        if tempScreen_res != screenRes:
            screen = pygame.display.set_mode(screenRes, pygame.RESIZABLE)
            imagesResize(screenRes)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if window == "homeScreen":
            pass

        pygame.display.update()
        endTime = time.time()
        dt = endTime-initTime
        if dt != 0:
            frameRate = 1/dt
        else:
            frameRate = 1000
