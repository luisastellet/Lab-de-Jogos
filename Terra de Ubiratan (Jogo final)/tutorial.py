from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
import pygame


#importando outros arquivos
import funcao
import level1

def tutorial():
    
    tutorial = Sprite("Imagens/tutorial.png",28)
    tutorial.set_total_duration(6000)

    # pygame.mixer.music.load("Music/FinalBattle.wav")
    # pygame.mixer.music.set_volume(0.3)
    # pygame.mixer.music.play(-1)
    
    
    #arrumando o tamanho da tela e o título da página
    janela = Window(815,670)
    janela.set_title("A TERRA DE UBIRATAN")

    #criando os teclado de teclado
    teclado = janela.get_keyboard()
    
    while True:
        tutorial.draw()
        funcao.posiçãoAnim(tutorial, 0,0)

        if teclado.key_pressed("SPACE"):
            return
            
        janela.update()