from pygame import draw
from pygame.locals import *
import pygame
from sys import exit
from random import randint

pygame.init()

gameSets = {
    "largura": 640, 
    "altura": 480, 
    "relogio": pygame.time.Clock(),
    "fps" : 60,
    "points": 0,
    "font": pygame.font.SysFont('arial',22)
}

tela = pygame.display.set_mode((gameSets["largura"], gameSets["altura"]))
pygame.display.set_caption('SimpleCubeGame')


pCube = {
    "largura": 50,
    "altura": 50,
    "x": 0,
    "y": 0,
    "color": (randint(0,255),randint(0,255),randint(0,255)),
    "vel": 5
}


fruit = {
    "largura": 30,
    "altura": 30,
    "x": randint(0,gameSets["largura"]-2),
    "y": randint(0,gameSets["altura"]-2),
    "color": (255,0,0),

}

while True:
    gameSets["relogio"].tick(gameSets["fps"])
    tela.fill((0,0,0))
    text = gameSets["font"].render(str(gameSets["points"]),True,(255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_d]:
        pCube["x"] = pCube["x"] + 1 *pCube["vel"]
    elif pygame.key.get_pressed()[K_a]:
        pCube["x"] = pCube["x"] - 1 *pCube["vel"]
    elif pygame.key.get_pressed()[K_w]:
        pCube["y"] = pCube["y"] - 1 *pCube["vel"]
    elif pygame.key.get_pressed()[K_s]:
        pCube["y"] = pCube["y"] + 1 *pCube["vel"]

    drawFruit = pygame.draw.rect(tela,fruit["color"],(fruit["x"],fruit["y"],fruit["largura"],fruit["altura"]))
    drawCube = pygame.draw.rect(tela,pCube["color"],(pCube["x"],pCube["y"],pCube["largura"],pCube["altura"]))
    tela.blit(text,(0,0))

    if drawCube.colliderect(drawFruit):
        pCube["color"] = (randint(0,255),randint(0,255),randint(0,255))
        fruit["x"] = randint(0,gameSets["largura"]-2)
        fruit["y"] = randint(0,gameSets["altura"]-2)
        gameSets["points"] = gameSets["points"] + 1
        pCube["vel"] = pCube["vel"] + 0.2
    
    if pCube["x"] > gameSets["largura"]:
        pCube["x"] = 0
    elif pCube["x"] < 0:
        pCube["x"] = gameSets["largura"]
    elif pCube["y"] > gameSets["altura"]:
        pCube["y"] = 0
    elif pCube["y"] < 0:
        pCube["y"] = gameSets["altura"]


    pygame.display.update() 