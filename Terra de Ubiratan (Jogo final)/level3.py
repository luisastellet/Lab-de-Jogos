from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
import pygame
from PPlay.sound import*

#importando outros arquivos
import menu
import jogador
import finalfeliz
import gameover                                                       
import tiro

def level3(movimento, checkpos_player, player_colisao, colidiu, vida1, vida2, vida3, vida4, vida5, vida_player,som):
    checkpos_player = 0
    player_colisao.y = 105
    
    #arrumando o tamanho da tela e o título da página
    janela = Window(815,670)
    janela.set_title("A TERRA DE UBIRATAN")

    #criando os comandos de comandos
    comandos = janela.get_keyboard()

    #criando o fundo
    fundo = Sprite("./Imagens/level3/fundo.png",56)
    fundo.set_total_duration(4000)

    
    # Criando array de tiros
    tiro1 = []
    tiro2 = []
    tiro3 = []
    velBalas = 400
    timerchefao1 = 0
    timerchefao2 = 0
    timerchefao3 = 0
    vida_chefao1 = 4
    vida_chefao2 = 4
    vida_chefao3 = 4
    
    #Definição da posição do player
    player_parado = Sprite("./Imagens/player/parados.png",4)
    player_parado.set_position(402,105) #o player colisao guarda só 1 imagem
    player_parado.set_total_duration(1000)
    player = player_parado
    player.x = 280
    player.y = 339
    
    player_esquerda = Sprite("./Imagens/player/left.png",4)
    player_esquerda.set_position(402,105) #o player colisao guarda só 1 imagem
    player_esquerda.set_total_duration(1000)
    
    player_direita = Sprite("./Imagens/player/right.png",4)
    player_direita.set_position(402,105) #o player colisao guarda só 1 imagem
    player_direita.set_total_duration(1000)
    
    player_up = Sprite("./Imagens/player/up.png",4)
    player_up.set_position(402,105) #o player colisao guarda só 1 imagem
    player_up.set_total_duration(1000)
    
    player_down = Sprite("./Imagens/player/down.png",4)
    player_down.set_position(402,105) #o player colisao guarda só 1 imagem
    player_down.set_total_duration(1000)
    
    
    ##########################   CHEFÃO 1  DIREITA  ############################### 
    chefao1_parado = Sprite("./Imagens/chefao/parado_esquerda.png",1)
    chefao1_parado.set_position(549,145) #o player colisao guarda só 1 imagem
    chefao1_parado.set_total_duration(1000)
    chefao1 = chefao1_parado
        
    
    ##########################   CHEFÃO 2 ESQUERDA  ############################### 
    chefao2_parado = Sprite("./Imagens/chefao/parado.png",1)
    chefao2_parado.set_position(11,506) #o player colisao guarda só 1 imagem
    chefao2_parado.set_total_duration(1000)
    chefao2 = chefao2_parado
    
    
    ##########################   CHEFÃO 3 BAIXO  ############################### 
    chefao3_parado = Sprite("./Imagens/chefao/up.png",4)
    chefao3_parado.set_position(463,592) #o player colisao guarda só 1 imagem
    chefao3_parado.set_total_duration(1000)
    chefao3 = chefao3_parado
    
        
    #Ajustando a cabana e a colisão
    FPS = 60
    clock = pygame.time.Clock()
    
    inverteu_chefao = False

    player_colisao = Sprite('./Imagens/player/parado.png',1)

    lancas_esq=[]
    lancas_dir =[]
    lancas_down = []
    lancas_up =[]
    recarga = 1
    vellanca = 800
        
    while True:
        #desenhando a colisão dos objetos para uso do collided_perfect
        player_colisao.draw()
    
        #desenha fundo
        fundo.update()
        fundo.draw()
        
        clock.tick(FPS)
    
        # condição de voltar pro menu principal
        if comandos.key_pressed("esc"):
            menu.menu()
            
        #chamando a função pro personagem andar
        player,checkpos_player = jogador.movimento(janela, comandos, player, movimento,checkpos_player, colidiu)
    
        #criando as condições pra player não sair da tela
        #se a player sair da tela na esquerda, ela fica grudada na cerca pela esquerda
        if (player.x < 132):
            player.x = 132
        #se a player sair da tela na direta, ela fica grudada na cerca pela direira
        if (player.x + player.width > 505): 
            player.x = 505 - player.width   
        #se a player sair da tela em cima, ela fica grudada na cerca em cima
        if (player.y < 177):
            player.y = 177
        #se a player sair da tela embaixo, ela fica grudada na cerca em baixo
        if (player.y + player.height > 555): 
            player.y = 555 - player.height
                    
        if checkpos_player == 1: player = jogador.set_player(player,player_esquerda)
        if checkpos_player == 2: player = jogador.set_player(player,player_direita)
        if checkpos_player == 3: player = jogador.set_player(player,player_up)
        if checkpos_player == 4: player = jogador.set_player(player,player_down)
        if checkpos_player == 0: player = jogador.set_player(player,player_parado)
        player.update()
                
        #checando a colisão do personagem
        player_colisao.x = player.x
        player_colisao.y = player.y
        
        #as vidas
        if(vida_player == 9):
            vida5 = Sprite("./Imagens/meia_vida.png", 1)
            vida5.set_position(239,19)
        elif(vida_player == 8):
            vida5 = Sprite("./Imagens/sem_vida.png", 1)
            vida5.set_position(239,19)
        elif(vida_player == 7):
            vida4 = Sprite("Imagens/meia_vida.png", 1)
            vida4.set_position(184, 19)
        elif(vida_player == 6):
            vida4 = Sprite("Imagens/sem_vida.png", 1)
            vida4.set_position(184, 19)
        elif(vida_player == 5):
            vida3 = Sprite("./Imagens/meia_vida.png", 1)
            vida3.set_position(129,19)
        elif(vida_player == 4):
            vida3 = Sprite("./Imagens/sem_vida.png", 1)
            vida3.set_position(129,19)
        elif(vida_player == 3):
            vida2 = Sprite("./Imagens/meia_vida.png", 1)
            vida2.set_position(74,19)
        elif(vida_player == 2):
            vida2 = Sprite("./Imagens/sem_vida.png", 1)
            vida2.set_position(74,19)
        elif(vida_player == 1):
            vida1 = Sprite("./Imagens/meia_vida.png", 1)
            vida1.set_position(19,19)
        elif(vida_player <= 0):
            vida1 = Sprite("./Imagens/sem_vida.png", 1)
            vida1.set_position(19,19)
            som.stop()
            gameover.gameover()


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

        if (vida_chefao1>0):
            for i,lanca in enumerate(lancas_dir):
                if lanca.collided_perfect(chefao1):
                    vida_chefao1-=1
                    timerchefao1=60
                    lancas_dir.pop(i)
        if (vida_chefao2>0):
            for i,lanca in enumerate(lancas_esq):
                if lanca.collided_perfect(chefao2):
                    vida_chefao2-=1
                    timerchefao2=60
                    lancas_esq.pop(i)
        if (vida_chefao3>0):
            for i,lanca in enumerate(lancas_down):
                if lanca.collided_perfect(chefao3):
                    vida_chefao3-=1
                    timerchefao3=60
                    lancas_down.pop(i)
        
        if (timerchefao1 > 0):
            timerchefao1-=1
        if (timerchefao2 > 0):
            timerchefao2-=1
        if (timerchefao3 > 0):
            timerchefao3-=1           
        #fazendo o tiro dos chefões
        if (vida_chefao1>0):
            tiro.novo_tiro_chefao(chefao1, tiro1)
            vida_player = tiro.tiro_chefao(janela,tiro1,velBalas, player, vida_player, chefao1)
        if (vida_chefao2>0):
            tiro.novo_tiro_chefao(chefao2, tiro2)
            vida_player = tiro.tiro_chefao(janela,tiro2,velBalas, player, vida_player, chefao2)
        if (vida_chefao3>0):
            tiro.novo_tiro_chefao(chefao3, tiro3)
            vida_player = tiro.tiro_chefao(janela,tiro3,velBalas, player, vida_player, chefao3)
        
        #movimento do chefão 1 (direita)
        if(chefao1.y <= 145):
            inverteu_chefao = False
        elif(chefao1.y >= 515 ):
            inverteu_chefao = True
        if(inverteu_chefao == False):
            chefao1.y += 2
        else:
            chefao1.y -= 2
            
        #movimento do chefão 2 (esquerda)
        if(chefao2.y <= 145):
            inverteu_chefao = True
        elif(chefao2.y >= 515 ):
            inverteu_chefao = False
        if(inverteu_chefao == False):
            chefao2.y -= 2
        else:
            chefao2.y += 2
        
        #movimento do chefão 3 (embaixo)
        if(chefao3.x >= 465):
            inverteu_chefao = False
        elif(chefao3.x <= 107 ):
            inverteu_chefao = True
        if(inverteu_chefao == False):
            chefao3.x -= 2
        else:
            chefao3.x += 2

        if(vida_chefao1==0 and vida_chefao2==0 and vida_chefao3==0):
            som.stop()
            finalfeliz.finalfeliz()
            
        #desenhando o player
        player.draw()
        if(vida_chefao1 > 0 and timerchefao1%2==0):
            chefao1.draw()
        if(vida_chefao2 > 0 and timerchefao2%2==0):
            chefao2.draw()
        if(vida_chefao3 > 0 and timerchefao3%2==0):
            chefao3.draw()
            
        vida1.draw()
        vida2.draw()
        vida3.draw()
        vida4.draw()
        vida5.draw()
                
        janela.update()