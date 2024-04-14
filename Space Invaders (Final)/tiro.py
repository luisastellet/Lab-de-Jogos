from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import*
import random


largura = 800
altura = 630

control = Mouse()

        
#Criando os tiros
def novo_tiro(nave, lista_de_tiros):

    tiro = GameImage("./imagens/tiro.png")

    tiro.x = nave.x + 42
    tiro.y = nave.y - tiro.height

    lista_de_tiros.append(tiro)

    return lista_de_tiros


def limitando_tiro(tiro, lista_de_tiros):

    if (tiro.y <= 0 - tiro.height):
        lista_de_tiros.remove(tiro)
        
def novo_tiro_inimigo(inimigo,listaProjeteisInimigos, cont):
    if(cont % 3 == 0):
        tiro_inimigo = Sprite("imagens/tiro_especial.png",1)
    else:
        tiro_inimigo = Sprite("imagens/tiro.png",1)
        
    tiro_inimigo.x = inimigo[0].x + 50
    tiro_inimigo.y = inimigo[0].y + tiro_inimigo.height + 50
    if (random.random() < 0.3 and len(listaProjeteisInimigos)==0):
        listaProjeteisInimigos.append(tiro_inimigo)

def tiro_inimigo(janela,listaProjeteisInimigos,vel_tiro_inimigo,cont):        
    for i,projetil in enumerate(listaProjeteisInimigos):            
        projetil.y += vel_tiro_inimigo*janela.delta_time()
        projetil.draw()
        if (projetil.y>janela.height):
            listaProjeteisInimigos.pop(i)
    
            
            
def delay(delay,linha):
    if linha==4:    
        delay = 40
    if linha==5:
        delay = 35
    if linha>=6:
        delay = 25
    return delay

def delay_inimigo(delayInimigo,linha):
    if linha==4:
        delayInimigo = 100
    if linha==5:
        delayInimigo = 110
    if linha>=6:
         delayInimigo = 120
    return delayInimigo