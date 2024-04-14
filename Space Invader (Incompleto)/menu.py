#importando as bibliotecas
from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*

#importando outros arquivos
import jogar
import dificuldade

def menu():
    #arrumando o tamanho da tela e o título da página
    janela = Window(800,514)
    janela.set_title("Space Invaders")

    #criando o mouse
    mouse = janela.get_mouse()

    #criando o fundo
    fundo = GameImage("imagens/fundo.png")

    #sprites dos botões (as alturas ajustei no chute, pensando em ficar organizadinho na tela)
    titulo = GameImage("imagens/titulo.png")
    titulo.set_position((janela.width/2)-113, 45)

    botao_jogar = GameImage("botoes/jogar_antes.png")
    botao_jogar.set_position((janela.width/2)-70,160)

    botao_dificuldade = GameImage("botoes/dificuldade_antes.png")
    botao_dificuldade.set_position((janela.width/2)-70,240)

    botao_ranking = GameImage("botoes/ranking_antes.png")
    botao_ranking.set_position((janela.width/2)-70,320)

    botao_sair = GameImage("botoes/sair_antes.png")
    botao_sair.set_position((janela.width/2)-70,400)



    while True:

        #criando as condições para o mouse selecionar as áreas dos botões e mudar de imagem ao pressionar
        #botao jogar
        if mouse.is_over_object(botao_jogar):
            botao_jogar = GameImage("botoes/jogar_depois.png")
            botao_jogar.set_position((janela.width/2)-70,160)
            #se pressionar o mouse na área, abre uma tela nova
            if (mouse.is_button_pressed(1)): 
                jogar.jogar()
        else:
            botao_jogar = GameImage("botoes/jogar_antes.png")
            botao_jogar.set_position((janela.width/2)-70,160)

        #botao dificuldade
        if mouse.is_over_object(botao_dificuldade):
            botao_dificuldade = GameImage("botoes/dificuldade_depois.png")
            botao_dificuldade.set_position((janela.width/2)-70,240)
            #se pressionar o mouse na área, abre uma tela nova
            if (mouse.is_button_pressed(1)):
                dificuldade.dificuldade()
        else:
            botao_dificuldade = GameImage("botoes/dificuldade_antes.png")
            botao_dificuldade.set_position((janela.width/2)-70,240)

        #botao ranking
        if mouse.is_over_object(botao_ranking):
            botao_ranking = GameImage("botoes/ranking_depois.png")
            botao_ranking.set_position((janela.width/2)-70,320)
        else:
            botao_ranking = GameImage("botoes/ranking_antes.png")
            botao_ranking.set_position((janela.width/2)-70,320) 

        #botao sair
        if mouse.is_over_object(botao_sair):
            botao_sair = GameImage("botoes/sair_depois.png")
            botao_sair.set_position((janela.width/2)-70,400)
            #se pressionar o mouse na área, abre uma tela nova
            if (mouse.is_button_pressed(1)):
                janela.close()
        else:
            botao_sair = GameImage("botoes/sair_antes.png")
            botao_sair.set_position((janela.width/2)-70,400)

        #desenhando as gameimages
        fundo.draw()
        titulo.draw()
        botao_jogar.draw()
        botao_dificuldade.draw()
        botao_ranking.draw()
        botao_sair.draw()
        
        janela.update()
