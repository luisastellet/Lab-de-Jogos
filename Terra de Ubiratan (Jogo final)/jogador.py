#importando outras bibliotecas
from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*

def set_player(player, playerAtual):
    playerAtual.x = player.x
    playerAtual.y = player.y
    player = playerAtual
    return player
    
    
def movimento(janela,teclado,player,movimento,check_pos, colidiu):  
    
     #se apertar A ou LEFT, o eixo x da player diminui, para ir pra esquerda      
    if (colidiu == False and (teclado.key_pressed("A") or teclado.key_pressed("LEFT"))):
        player.x -= movimento * janela.delta_time()
        check_pos = 1

    #se apertar D ou RIGHT, o eixo x da player aumenta, para ir pra direita
    elif (colidiu == False and (teclado.key_pressed("D") or teclado.key_pressed("RIGHT"))):
        player.x += movimento * janela.delta_time()
        check_pos = 2

    #se apertar W ou UP, o eixo x da player diminui, para ir pra esquerda      
    elif (colidiu == False and (teclado.key_pressed("W") or teclado.key_pressed("UP"))):
        player.y -= movimento * janela.delta_time()
        check_pos = 3

    #se apertar S ou DOWN, o eixo x da player diminui, para ir pra esquerda      
    elif (colidiu == False and (teclado.key_pressed("S") or teclado.key_pressed("DOWN"))):
        player.y += movimento * janela.delta_time()
        check_pos = 4
        
    else:
        check_pos = 0
        
    return player, check_pos
        

        


