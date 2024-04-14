from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import*
import random

largura = 815
altura = 670

control = Mouse()
        
def novo_tiro_inimigo(cacador,listaProjeteisInimigos):    
    #atira pra esquerda
    if (cacador.y == 212 or cacador.y == 536):
        tiro_inimigo = Sprite("Imagens/tiro.png",1)
        tiro_inimigo.x = cacador.x - cacador.width - 2
        tiro_inimigo.y = cacador.y + cacador.height/2 + 17
    
    #atira pra cima
    elif (cacador.y == 575):
        tiro_inimigo = Sprite("Imagens/tiro_cima.png",1)
        tiro_inimigo.x = cacador.x + cacador.width - 30
        tiro_inimigo.y = cacador.y + cacador.height/2 - 20
        
    #atira pra direita
    else:
        tiro_inimigo = Sprite("Imagens/tiro.png",1)
        tiro_inimigo.x = cacador.x + cacador.width + 2
        tiro_inimigo.y = cacador.y + cacador.height/2 + 17
    
    if (random.randint(1,60) == 60 and len(listaProjeteisInimigos) == 0):
        listaProjeteisInimigos.append(tiro_inimigo)
    
def tiro_inimigo(janela,listaProjeteisInimigos,vel_tiro_inimigo, player, vida_player, cacador):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if (cacador.y == 212 or cacador.y == 536):
            projetil.x -= vel_tiro_inimigo*janela.delta_time()
        elif (cacador.y == 575):
            projetil.y -= vel_tiro_inimigo*janela.delta_time()
        else:
            projetil.x += vel_tiro_inimigo*janela.delta_time()
        projetil.draw()
        
        if (projetil.x>janela.width) or (projetil.y<0) or (projetil.x <0):
            listaProjeteisInimigos.pop(i)
        elif (projetil.collided(player)):
            listaProjeteisInimigos.pop(i)
            vida_player -= 1
            
    return vida_player

def novo_tiro_chefao(chefao,listaProjeteisInimigos):    
    #atira pra esquerda
    if (chefao.x == 549):
        tiro_inimigo = Sprite("Imagens/tiro.png",1)
        tiro_inimigo.x = chefao.x - chefao.width - 2
        tiro_inimigo.y = chefao.y + chefao.height/2 + 17
    
    #atira pra cima
    elif (chefao.y == 592):
        tiro_inimigo = Sprite("Imagens/tiro_cima.png",1)
        tiro_inimigo.x = chefao.x + chefao.width - 30
        tiro_inimigo.y = chefao.y + chefao.height/2 - 20
        
    #atira pra direita
    elif(chefao.x == 11):
        tiro_inimigo = Sprite("Imagens/tiro.png",1)
        tiro_inimigo.x = chefao.x + chefao.width + 2
        tiro_inimigo.y = chefao.y + chefao.height/2 + 17
    
    if (random.randint(1,30) == 30 and len(listaProjeteisInimigos) == 0):
        listaProjeteisInimigos.append(tiro_inimigo)

def tiro_chefao(janela,listaProjeteisInimigos,vel_tiro_inimigo, player, vida_player, chefao):
    for i,projetil in enumerate(listaProjeteisInimigos):
        projetil.draw()
        if (chefao.x == 549):
            projetil.x -= vel_tiro_inimigo*janela.delta_time()
        elif (chefao.y == 592):
            projetil.y -= vel_tiro_inimigo*janela.delta_time()
        elif(chefao.x == 11):
            projetil.x += vel_tiro_inimigo*janela.delta_time()
        
        if (projetil.x>janela.width) or (projetil.y<0) or (projetil.x <0):
            listaProjeteisInimigos.pop(i)
        elif (projetil.collided(player)):
            listaProjeteisInimigos.pop(i)
            vida_player -= 1
            
    return vida_player

#Criando os tiros
def novo_tiro(player,lancas_esquerda,lancas_dir,lancas_up,lancas_down,checkpos):

    if(checkpos == 1):
        lanca = Sprite("Imagens/player/lanca_esquerda.png")
        lanca.set_sequence_time(0, 4, 300, True)
        lanca.x = player.x - 2
        lanca.y = player.y + player.height/2
        lancas_esquerda.append(lanca)
        return lancas_esquerda, lancas_dir,lancas_up,lancas_down
    
    if(checkpos == 2):
        lanca = Sprite("Imagens/player/lanca_direita.png")
        lanca.set_sequence_time(0, 4, 300, True)
        lanca.x = player.x + player.width + 2
        lanca.y = player.y + player.height/2
        lancas_dir.append(lanca)
        return lancas_esquerda, lancas_dir,lancas_up,lancas_down
    
    if(checkpos == 3):
        lanca = Sprite("Imagens/player/lanca_up.png")
        lanca.set_sequence_time(0, 4, 300, True)
        lanca.x = player.x + player.width/2
        lanca.y = player.y - 2
        lancas_up.append(lanca)
        return lancas_esquerda, lancas_dir,lancas_up,lancas_down
    
    if(checkpos == 4 or checkpos == 0):
        lanca = Sprite("Imagens/player/lanca_down.png")
        lanca.set_sequence_time(0, 4, 300, True)
        lanca.x = player.x + player.width/2 
        lanca.y = player.y + player.height + 2
        lancas_down.append(lanca)
        return lancas_esquerda, lancas_dir,lancas_up,lancas_down


def limitando_tiro(tiro, lista_de_tiros,janela):

    if (tiro.y <= 0 or tiro.y >= janela.height or tiro.x <= 0 or tiro.x >= janela.width):
        lista_de_tiros.remove(tiro)
            
def colisaocacador(cacador,vida_cacador,lancas_dir,lancas_esq,lancas_up,lancas_down):
    if(vida_cacador>0):
        for i,lanca in enumerate(lancas_dir):
            if lanca.collided_perfect(cacador):
                vida_cacador-=1
                lancas_dir.pop(i)
                return 180, vida_cacador
        for i,lanca in enumerate(lancas_esq):
            if lanca.collided_perfect(cacador):
                vida_cacador-=1
                lancas_esq.pop(i)
                return 180, vida_cacador
        for i,lanca in enumerate(lancas_up):
            if lanca.collided_perfect(cacador):
                vida_cacador-=1
                lancas_up.pop(i)
                return 180, vida_cacador
        for i,lanca in enumerate(lancas_down):
            if lanca.collided_perfect(cacador):
                vida_cacador-=1
                lancas_down.pop(i)
                return 180, vida_cacador
    return 0,vida_cacador