#importando outras bibliotecas
from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*

#criando a função pro jogador andar
def jogador(janela,teclado,nave,movimento):  
    #se apertar A ou LEFT, o eixo x da nave diminui, para ir pra esquerda      
    if (teclado.key_pressed("A") or teclado.key_pressed("LEFT")):
        nave.x -= movimento * janela.delta_time()

    #se apertar D ou RIGHT, o eixo x da nave aumenta, para ir pra direita
    if (teclado.key_pressed("D") or teclado.key_pressed("RIGHT")):
        nave.x += movimento * janela.delta_time()

    #criando as condições pra nave não sair da tela
    #se a nave sair da tela na esquerda, ela fica grudada na borda esquerda
    if (nave.x <0):
        nave.x = 0
    #se a nave sair da tela na direta, ela fica grudada na borda direira
    if (nave.x + nave.width > janela.width): 
        nave.x = janela.width - nave.width
    