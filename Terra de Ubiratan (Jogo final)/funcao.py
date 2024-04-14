#Este arquivo foi criado para conter todas as funções criadas ao longo de todos os outros arquivos, para tornar mais legivel e organizado os códigos!!!

#Importando
from PPlay.sprite import*
from PPlay.collision import*

#Desenhnado 
def posição(sprite, x, y):

    sprite.x = x
    sprite.y = y
    sprite.draw()
    
def posiçãoAnim(sprite, x, y):
    
    sprite.x = x
    sprite.y = y
    sprite.update()
    sprite.draw()

def colisao_cenario(player, player_colisao, objeto_colisao, colidiu, check_pos):
    if(player_colisao.collided_perfect(objeto_colisao)):
        colidiu = True
    else:
        colidiu = False
    if (colidiu):
        #colidindo pela esquerda
        if(check_pos == 2):
            colidiu = False
            player.x -= 7
        #colidindo pela direita
        if(check_pos == 1):
            colidiu = False
            player.x += 7
        #colidindo em cima
        if(check_pos == 4):
            colidiu = False
            player.y -= 7
        #colidindo em baixo
        if(check_pos == 3):
            colidiu = False
            player.y += 7

    return player, colidiu

