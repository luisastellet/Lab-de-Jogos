#importando as bibliotecas
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import*
from PPlay.sound import*
import pygame


#importando outros arquivos
import menu
import funcao
import jogador
import level1tolevel2
import tiro


#criando a função principal com retorno inteiro
def level1():

    #arrumando o tamanho da tela e o título da página
    janela = Window(815,670)
    janela.set_title("A TERRA DE UBIRATAN")

    som = Sound("Som/musica_aventura.mp3")
    som.set_repeat(True)
    som.set_volume(30)
    som.play()

    #criando os comandos de teclado
    comandos = janela.get_keyboard()

    #criando o fundo
    fundo = Sprite("./Imagens/fundo_jogar/fundo_jogar1.png",54)
    fundo.set_total_duration(4000)
    
    vida1 = Sprite("./Imagens/vida_cheia.png", 1)
    vida1.set_position(19,19)
    vida2 = Sprite("./Imagens/vida_cheia.png", 1)
    vida2.set_position(74,19)
    vida3 = Sprite("./Imagens/vida_cheia.png", 1)
    vida3.set_position(129,19)
    vida4 = Sprite("./Imagens/vida_cheia.png", 1)
    vida4.set_position(184,19)
    vida5 = Sprite("./Imagens/vida_cheia.png", 1)
    vida5.set_position(239,19)
    
    
    arv_chamas = Sprite("./Imagens/fundo_jogar/arvores_chamas_spritesheet.png", 50)
    arv_chamas.set_total_duration(4000)
    arvore_colisao = Sprite("./Imagens/fundo_jogar/arvore_colisao.png",1)
    arvore_colisao.set_position(136,276)

    casa_chamas = Sprite("./Imagens/fundo_jogar/casa em chamas.png", 50)
    casa_chamas.set_total_duration(4000)
    casa_colisao = Sprite("./Imagens/fundo_jogar/casa_colisao.png",1)
    casa_colisao.set_position(583,333)
    
    #desenhando os detalhes pro personagem passar atrás
    arv_direita = Sprite("./Imagens/fundo_jogar/arvores_direita.png",1)
    arv_esquerda = Sprite("./Imagens/fundo_jogar/arvores_esquerda.png", 1)

    #Definição da posição do player
    player_parado = Sprite("./Imagens/player/parados.png",4)
    player_parado.x = janela.width/2 - player_parado.width/2
    player_parado.y = janela.height/2 - player_parado.height
    player_parado.set_total_duration(1000)
    player = player_parado
    
    player_esquerda = Sprite("./Imagens/player/left.png",4)
    player_esquerda.x = janela.width/2 - player_esquerda.width/2
    player_esquerda.y = janela.height/2 - player_esquerda.height 
    player_esquerda.set_total_duration(1000)
    
    player_direita = Sprite("./Imagens/player/right.png",4)
    player_direita.x = janela.width/2 - player_direita.width/2
    player_direita.y = janela.height/2 - player_direita.height
    player_direita.set_total_duration(1000)
    
    player_up = Sprite("./Imagens/player/up.png",4)
    player_up.x = janela.width/2 -player_up.width/2
    player_up.y = janela.height/2 - player_up.height - 20 
    player_up.set_total_duration(1000)
    
    player_down = Sprite("./Imagens/player/down.png",4)
    player_down.x = janela.width/2 - player_down.width/2
    player_down.y = janela.height/2 - player_down.height - 20
    player_down.set_total_duration(1000)
    
    
    player_colisao = Sprite('./Imagens/player/parado.png',1)
    
    
    movimento = 200
    checkpos_player = 0
    colidiu = False
    
    FPS = 60
    clock = pygame.time.Clock()

    lancas_esq=[]
    lancas_dir =[]
    lancas_down = []
    lancas_up =[]
    recarga = 1
    vellanca = 800
    
    #loop
    while True:
        
        #desenhando a colisão dos objetos para uso do collided_perfect
        player_colisao.draw()
        arvore_colisao.draw()
        casa_colisao.draw()
        
        # Desenha fundo
        fundo.update()
        fundo.draw()
        
        clock.tick(FPS)
        
        # condição de voltar pro menu principal
        if comandos.key_pressed("esc"):
            menu.menu()
        
        #chamando a função pro personagem andar
        player,checkpos_player = jogador.movimento(janela, comandos, player, movimento,checkpos_player,colidiu)
        
        #criando as condições pra player não sair da tela
        #se a player sair da tela na esquerda, ela fica grudada na borda esquerda
        if (player.x <0):
            player.x = 0
        #se a player sair da tela na direta, ela fica grudada na borda direira
        if (player.x + player.width > janela.width): 
            player.x = janela.width - player.width
        #se a player sair da tela em cima, ela fica grudada na borda de cima
        if (player.y <0):
            player.y = 0
        #se a player sair da tela embaixo, ela fica grudada na borda de baixo
        if (player.y + player.height > janela.height and not (player.x >= 299 and player.x + player.width <= 527)): 
            player.y = janela.height - player.height
        
        if(player.x >= 299 and player.x + player.width <= 527 and player.y > janela.height+2):
            x = level1tolevel2.level1tolevel2(movimento, checkpos_player, player_colisao, colidiu, vida1, vida2, vida3, vida4, vida5,som)

            
        if checkpos_player == 1: player = jogador.set_player(player,player_esquerda)
        if checkpos_player == 2: player = jogador.set_player(player,player_direita)
        if checkpos_player == 3: player = jogador.set_player(player,player_up)
        if checkpos_player == 4: player = jogador.set_player(player,player_down)
        if checkpos_player == 0: player = jogador.set_player(player,player_parado)
        player.update()
        
        #checando a colisão do personagem
        player_colisao.x = player.x
        player_colisao.y = player.y
        player, colidiu = funcao.colisao_cenario(player, player_colisao, casa_colisao, colidiu, checkpos_player)
        player, colidiu = funcao.colisao_cenario(player, player_colisao, arvore_colisao, colidiu, checkpos_player)

        #Comandos relacionados as lanças
        recarga += janela.delta_time()
        if (comandos.key_pressed("K")) and (recarga >= 1/2):
            lancas_esq,lancas_dir,lancas_up,lancas_down = tiro.novo_tiro(player,lancas_esq,lancas_dir,lancas_up,lancas_down,checkpos_player)
            recarga = 0

        #desenha, controla e limita o disparo
        if (lancas_esq != []):
            for d in lancas_esq:
                d.draw()
                d.x -= vellanca * janela.delta_time()
                d = tiro.limitando_tiro(d, lancas_esq,janela)

        elif (lancas_dir != []):
            for d in lancas_dir:
                d.draw()
                d.x += vellanca * janela.delta_time()
                d = tiro.limitando_tiro(d, lancas_dir,janela)
        
        elif (lancas_up != []):
            for d in lancas_up:
                d.draw()
                d.y -= vellanca * janela.delta_time()
                d = tiro.limitando_tiro(d, lancas_up,janela)

        elif (lancas_down != []):
            for d in lancas_down:
                d.draw()
                d.y += vellanca * janela.delta_time()
                d = tiro.limitando_tiro(d, lancas_down,janela)
        

        #desenhando o player
        player.draw()
        vida1.draw()
        vida2.draw()
        vida3.draw()
        vida4.draw()
        vida5.draw()
        
        
        funcao.posição(arv_direita, 492, 538)
        funcao.posição(arv_esquerda, -30, 538)
        funcao.posiçãoAnim(casa_chamas, 573, 161)
        funcao.posiçãoAnim(arv_chamas, 56,147)
        
        janela.update()