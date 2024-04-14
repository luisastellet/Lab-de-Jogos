#importando as bibliotecas
from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from PPlay.sound import*
import pygame
import time

import funcao
import tutorial
import opcoes
import menutolevel1

#importando outros arquivos

def menu():
    #arrumando o tamanho da tela e o título da página
    janela = Window(815,670)
    janela.set_title("A TERRA DE UBIRATAN")

    #criando o mouse
    mouse = janela.get_mouse()

    #criando o fundo
    fundo = GameImage("imagens/fundo_menu.png")

    audio = Sound("./Som/musica_calma.mp3")
    audio.set_repeat(True)
    audio.set_volume(30)
    audio.play()

    #Inicializando botões
    botao_jogar = Sprite("imagens/botao/botão_jogar.png",1)
    botao_opcoes = Sprite("imagens/botao/botão_opções.png", 1)
    botao_sair = Sprite("imagens/botao/botão_sair.png",1)

    dificuldade = 1
    
    while True:
        #desenhando as gameimages
        fundo.draw()

        #criando as condições para o mouse selecionar as áreas dos botões e mudar de imagem ao pressionar
        #botao jogar
         #Se o mouse estiver sobre a area da imagem do falso botão, o botão interativo será desenhado e se ele for clicado, irá para a tela respectiva
        if mouse.is_over_area([301,172], [541,226]):
            funcao.posição(botao_jogar,296,173)
            if (mouse.is_button_pressed(1)):
                menutolevel1.menutolevel1(audio)
                

        if mouse.is_over_area([301,249], [541,302]):
            funcao.posição(botao_opcoes, 296,250 )
            if (mouse.is_button_pressed(1)):
                tutorial.tutorial()
        
        if mouse.is_over_area([301,327], [541,381]):
            funcao.posição(botao_sair,296,328)
            if(mouse.is_button_pressed(1)):
                janela.close()


        
        
        janela.update()
