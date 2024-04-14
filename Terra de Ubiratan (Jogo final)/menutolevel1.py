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
import tutorial
import level1

def menutolevel1(audio):
    
    transicao = Sprite("Imagens/menutolevel1.png",28)
    transicao.set_total_duration(4000)

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
        funcao.posiçãoAnim(transicao, 0,0)

        if teclado.key_pressed("SPACE"):
            audio.stop()
            level1.level1()
            
        janela.update()