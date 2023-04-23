import pygame
from services import acoes
from pygame.locals import *

BD = acoes.action()
BD.criarHero("iron Man", "Inteligência e uma armadura motorizada", "Fonte de energia para o seu traje")
BD.criarHero("Hulk", "Força física", "Raiva")
BD.criarHero("Spider Man", "Gerar teiasi, escalar paredes, reflexos", "Escassez dp flúido de teias")
BD.criarHero("Thor", "Força, velocidade sobre-humana, controlar os elemntos da tempestade", "Sua fúria o reduz a uma besta sem inteligência")
BD.criarHero("Baby Groot", "Regeneração e durabilidade", "Comunicação")

pygame.init()

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Heroes")

objectGroup = pygame.sprite.Group()

color_light = (170,170,170)
color = (255,255,255)
preto = (0,0,0,)

width = display.get_width()
height = display.get_height()
smallfont = pygame.font.SysFont('Corbel',35)

listabt = []
def nomesButoes():
    for i in BD.listaHeroes:
        bt = smallfont.render(i.name, True, preto)
        listabt.append(bt)
nomesButoes()

def exiba_msg(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    menssagem = f'{msg}'
    txt_formatado = fonte.render(menssagem, True, cor)

    return txt_formatado

def dadoHero(name):
    personagem = exiba_msg(name, 62, color)
    display.blit(personagem, (250, 30))
    dados = exiba_msg(BD.bdHero("name", name), 20, color)
    display.blit(dados, (0, 120))
    dados = exiba_msg(BD.bdHero("power", name), 20, color)
    display.blit(dados, (0, 155))
    dados = exiba_msg(BD.bdHero("weakness", name), 20, color)
    display.blit(dados, (0, 190))

def Butoes():
    x = 7
    for i in range(0,2):
        display.blit(listabt[i], (x, 432))
        x +=190

def Imagem(nome):
    img = pygame.image.load(nome +'.jpeg')
    img = pygame.transform.scale(img, [840, 480])
    return img

display.blit(Imagem("MARVEL"), (0, 0))

gameloop = True
gameOver= False
clock = pygame.time.Clock()
if __name__ == '__main__':
    while gameloop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] > 0 and mouse[0] <140 and mouse[1] >430 and mouse[1] < 470:
                    display.fill([19, 173, 135])
                    display.blit(Imagem("IronMan"), (0, 0))
                    dadoHero("iron Man")
                elif mouse[0] > 160 and mouse[0] <310 and mouse[1] >430 and mouse[1] < 470:
                    display.fill([19, 173, 135])
                    display.blit(Imagem("Hulk"), (0, 0))
                    dadoHero("Hulk")
                elif mouse[0] > 320 and mouse[0] < 500 and mouse[1] > 430 and mouse[1] < 470:
                    display.fill([19, 173, 135])
                    display.blit(Imagem("SpiderMan"), (0, 0))
                    dadoHero("Spider Man")
                elif mouse[0] > 510 and mouse[0] < 660 and mouse[1] > 430 and mouse[1] < 470:
                    display.fill([19, 173, 135])
                    display.blit(Imagem("Thor"), (0, 0))
                    dadoHero("Thor")
                elif mouse[0] > 670 and mouse[0] < 840 and mouse[1] > 430 and mouse[1] < 470:
                    display.fill([19, 173, 135])
                    display.blit(Imagem("BabyGroot"), (0, 0))

                    dadoHero("Baby Groot")


        pygame.draw.rect(display,color_light, [0,430, 150, 40])
        pygame.draw.rect(display, color_light, [160, 430, 150, 40])
        pygame.draw.rect(display, color_light, [320, 430, 180, 40])
        display.blit(listabt[2], (330, 432))
        pygame.draw.rect(display, color_light, [510, 430, 150, 40])
        display.blit(listabt[3], (550, 432))
        pygame.draw.rect(display, color_light, [670, 430, 170, 40])
        display.blit(listabt[4], (675, 432))
        Butoes()

        if not gameOver:
            objectGroup.update()
        pygame.display.update()
