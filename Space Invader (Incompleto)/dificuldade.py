#importando as bibliotecas
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

#importando outros arquivos
import menu

def dificuldade():
    #arrumando o tamanho da tela e o título da página
    janela = Window(800,514)
    janela.set_title("Space Invaders")

    #criando variável dificuldade padrão como 2
    dificuldade = 2
    
    #criando o fundo
    fundo = GameImage("imagens/fundo.png")

    #criando o mouse
    mouse = janela.get_mouse()
    #criando os comandos de teclado
    comandos = janela.get_keyboard()

    #criando os botões de dificuldade (escolhi os tamanhos no chute pra ficar direitinho na tela)
    #colocando o "escolha seu nível"
    escolha = GameImage("imagens/escolhanivel.png")
    escolha.set_position((janela.width/2)-113,55)  

    #colocando o botão "fácil"
    facil = GameImage("botoes/facil_antes.png")
    facil.set_position((janela.width/2)-70,180)   

    #colocando o botão "médio"
    medio = GameImage("botoes/medio_antes.png")
    medio.set_position((janela.width/2)-70,270)

    #colocando o botão "difícil"
    dificil = GameImage("botoes/dificil_antes.png")
    dificil.set_position((janela.width/2)-70,360)


    while True:
        fundo.draw()
        #criando as condições para o mouse selecionar as áreas dos botões e mudar de imagem ao pressionar
        
        #botao facil
        if mouse.is_over_object(facil):
            #se passar o mouse em cima, a imagem do botão muda
            facil = GameImage("botoes/facil_depois.png")
            facil.set_position((janela.width/2)-70,180)
            #ajustando a variável dificuldade apenas quando clicar no botão
            if (mouse.is_button_pressed(1)): 
                dificuldade = 1
        else:
            #voltar o botão pra foto original quando tira o mouse
            facil = GameImage("botoes/facil_antes.png")
            facil.set_position((janela.width/2)-70,180)

        #botao medio
        if mouse.is_over_object(medio):
            #se passar o mouse em cima, a imagem do botão muda
            medio = GameImage("botoes/medio_depois.png")
            medio.set_position((janela.width/2)-70,270)
            #ajustando a variável dificuldade apenas quando clicar no botão
            if (mouse.is_button_pressed(1)): 
                dificuldade = 2
        else:
            #voltar o botão pra foto original quando tira o mouse
            medio = GameImage("botoes/medio_antes.png")
            medio.set_position((janela.width/2)-70,270)

        #botao dificil
        if mouse.is_over_object(dificil):
            #se passar o mouse em cima, a imagem do botão muda
            dificil = GameImage("botoes/dificil_depois.png")
            dificil.set_position((janela.width/2)-70,360)
            #ajustando a variável dificuldade apenas quando clicar no botão
            if (mouse.is_button_pressed(1)): 
                dificuldade = 3
        else:
            #voltar o botão pra foto original quando tira o mouse
            dificil = GameImage("botoes/dificil_antes.png")
            dificil.set_position((janela.width/2)-70,360)
        
        #condição de voltar pro menu principal
        if comandos.key_pressed("esc"):
            menu.menu()
            
        #desenhando as gameimages
        escolha.draw()
        facil.draw()
        medio.draw()
        dificil.draw()
   
        janela.update()