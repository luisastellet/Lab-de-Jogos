from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
import pygame

#importando outros arquivos
import menu
import funcao
import jogador
import level3

def level2tolevel3(movimento, checkpos_player, player_colisao, colidiu, vida1, vida2, vida3, vida4, vida5, vida_player,som):
    
    transicao = Sprite("Imagens/level2tolevel3.png",1)
    transicao.set_position(0,0)
    
    # pygame.mixer.music.load("Music/FinalBattle.wav")
    # pygame.mixer.music.set_volume(0.3)
    # pygame.mixer.music.play(-1)
    
    #arrumando o tamanho da tela e o título da página
    janela = Window(815,670)
    janela.set_title("A TERRA DE UBIRATAN")

    #criando os teclado de teclado
    teclado = janela.get_keyboard()
    
    while True:
        transicao.draw()
        
        if teclado.key_pressed("SPACE"):
            level3.level3(movimento, checkpos_player, player_colisao, colidiu, vida1, vida2, vida3, vida4, vida5, vida_player,som)
            
        janela.update()