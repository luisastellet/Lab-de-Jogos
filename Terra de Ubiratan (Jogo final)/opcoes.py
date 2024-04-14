#importando as bibliotecas
from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*

#importando outros arquivos
import funcao

def opcoes():
    #arrumando o tamanho da tela e o título da página
    janela = Window(815,670)
    janela.set_title("A TERRA DE UBIRATAN")
    
    fundo = Sprite("./Imagens/fundo_dificuldade.png", 1)
    
    #Inicializando botões
    botao_facil = Sprite("Imagens/botao/botão_fácil.png",1)
    botao_medio = Sprite("Imagens/botao/botão_médio.png", 1)
    botao_dificil = Sprite("Imagens/botao/botão_dificil.png",1)
    
    #criando o mouse
    mouse = janela.get_mouse()
    
    #delay do mouse
    delay = 0
    
    time.sleep(1)
    
    while True:
        
        fundo.draw()
        
        if(delay>0):
            delay-=1
        
        if mouse.is_over_area([301,172], [541,226]):
            funcao.posição(botao_facil,296,173)
            if (mouse.is_button_pressed(1) and delay == 0):
                return 1

        if mouse.is_over_area([301,249], [541,302]):
            funcao.posição(botao_medio, 296,250 )
            if (mouse.is_button_pressed(1) and delay == 0):
                return 2

        
        if mouse.is_over_area([301,327], [541,381]):
            funcao.posição(botao_dificil,296,328)
            if(mouse.is_button_pressed(1) and delay == 0):
                return 3
            
    