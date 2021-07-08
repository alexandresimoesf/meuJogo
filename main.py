import sys
import pygame
import random
from itertools import cycle
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Carrinho de corrida')
cor = cycle([(102, 51, 0)])

w, h = 1000, 600
pedra = pygame.image.load('pedra.png').convert_alpha()
pedra = pygame.transform.scale(pedra, (40, 40))

carro = pygame.image.load('carro.png').convert_alpha()
carro = pygame.transform.scale(carro, (150, 150))

estrada = [(y, x) for (x, y) in zip(range(h // 2, w, 10), [h // 2] * (w // 2))]

for n, pos in enumerate(estrada):
    estrada[n] = (pos[0] - n * 4, pos[1])

clock = pygame.time.Clock()
ceu_skin = pygame.Surface((1000, h // 2))
ceu_skin.fill((0, 0, 51))
screen.blit(ceu_skin, (0, 0))
carpos = (w // 3, h - 200)
pedrapos = (estrada[0])


def movimento(click=False):
    global pedrapos
    for n, pos in enumerate(estrada):
        estrada_skin = pygame.Surface(((h // 2) + n * 8, 10))
        estrada_skin.fill(next(cor))
        screen.blit(estrada_skin, pos)
        screen.blit(ceu_skin, (0, 0))
        if click is not False:
            estrada[n] = (pos[0], pos[1] + 1)
            if estrada[0][1] > 300:
                estrada.insert(0, (304, 292))
                del estrada[-1]
                for n, pos in enumerate(estrada):
                    estrada[n] = (pos[0] - 4, pos[1] + 1)
                else:
                    pedrapos = (pedrapos[0], pedrapos[1] + 1)


while True:
    clock.tick(60)
    screen.fill((20, 50, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        movimento(click=True)
        pedrapos = pedrapos[0], pedrapos[1] + 4
        if pedrapos[1] > h:
            pedrapos = random.randint(300, 550), estrada[0][1] - 30
        if keys[pygame.K_LEFT]:
            carpos = carpos[0] - 3, carpos[1]
        if keys[pygame.K_RIGHT]:
            carpos = carpos[0] + 3, carpos[1]
    movimento()

    screen.blit(pedra, pedrapos)
    screen.blit(carro, carpos)

    pygame.display.update()
