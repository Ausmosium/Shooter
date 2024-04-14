import pygame
from os import system
FoNt = 0
FoNtprint = 0
def cls():
    system("cls")
def font(face:str,size=18):
    global FoNt
    FoNt = pygame.font.SysFont(face,size)
def printpy(text:str,coords=(100,400),color=(128,128,128)):
    global FoNt,FoNtprint
    FoNtprint = FoNt.render(text,True,color)
    screen.blit(FoNtprint,coords)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    icon = pygame.image.load('assets/images/icon.png')
    pygame.display.set_caption("Shooting Game")
    pygame.display.set_icon(icon)
    cls()
    running = True
    clock = pygame.time.Clock()
    while running == True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #Code Here
        pygame.display.update()