#importando as bibliotecas
from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
import pygame
from PPlay.sound import*

import funcao
import tutorial
import opcoes
import menu

#importando outros arquivos

def finalfeliz():
    #arrumando o tamanho da tela e o título da página
    janela = Window(815,670)
    janela.set_title("A TERRA DE UBIRATAN")
    
    #criando os comandos de teclado
    comandos = janela.get_keyboard()
    
    #criando o mouse
    mouse = janela.get_mouse()

    audio = Sound("./Som/musica_calma.mp3")
    audio.set_repeat(True)
    audio.set_volume(30)
    audio.play()


    #criando o fundo
    fundo = Sprite("imagens/final_feliz.png", 56)
    fundo.set_total_duration(4000)

    
    while True:
        
        if(comandos.key_pressed("esc")):
            menu.menu()
        
        funcao.posiçãoAnim(fundo, 0,0)

        fundo.draw()
        janela.update()