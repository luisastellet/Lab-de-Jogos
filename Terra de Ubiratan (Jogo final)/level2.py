from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*

#importando outros arquivos
import menu
import funcao
import jogador
import tiro
import level2tolevel3
import gameover

#caçador 4 e 1 inverter
#caçador 3 atira para cima

def level2(movimento, checkpos_player, player_colisao, colidiu, vida1, vida2, vida3, vida4, vida5,som):
    
    #arrumando o tamanho da tela e o título da página
    janela = Window(815,670)
    janela.set_title("A TERRA DE UBIRATAN")

    #criando os comandos de comandos
    comandos = janela.get_keyboard()

    #criando o fundo
    fundo = Sprite("./Imagens/level2/fundo.png",54)
    fundo.set_total_duration(4000)

    n_cacadores = 0
    # Criando array de tiros
    bala1 = []
    bala2 = []
    bala3 = []
    bala4 = []
    bala5 = []
    bala6 = []

    #definindo as configurações dos tiros
    velBalas = 200
    contador = 0
    
        
    #checkpos dos caçadores
    checkpos_cacador1 = 0
    checkpos_cacador2 = 0
    checkpos_cacador3 = 0
    checkpos_cacador4 = 0
    checkpos_cacador5 = 0
    checkpos_cacador6 = 0
    
    #colidiu dos caçadores
    colidiu_cacador1 = False
    colidiu_cacador2 = False
    colidiu_cacador3 = False
    colidiu_cacador4 = False
    colidiu_cacador5 = False
    colidiu_cacador6 = False

    #vida dos personagens
    vida_player = 10
    
    vida_cacador1 = 3
    vida_cacador2 = 3
    vida_cacador3 = 3
    vida_cacador4 = 3
    vida_cacador5 = 3
    vida_cacador6 = 3

    cont_cacador = 7
    
    popup = Sprite("./Imagens/level2/pop_up.png",1)
    popup.set_position(637,45)

    ##########################   PLAYER   ############################### 
    player_parado = Sprite("./Imagens/player/parados.png",4)
    player_parado.set_position(402,105) #o player colisao guarda só 1 imagem
    player_parado.set_total_duration(1000)
    player = player_parado
    
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

    
    ##########################   CAÇADOR 1   ############################### 
    cacador1_parado = Sprite("./Imagens/cacador/parado_left.png",1)
    cacador1_parado.set_position(616,536) #o player colisao guarda só 1 imagem
    cacador1_parado.set_total_duration(1000)
    cacador1 = cacador1_parado
        
    cacador1_colisao = Sprite('./Imagens/cacador/parado.png',1)
    
    
    ##########################   CAÇADOR 2   ############################### 
    cacador2_parado = Sprite("./Imagens/cacador/parado.png",1)
    cacador2_parado.set_position(151,509) #o player colisao guarda só 1 imagem
    cacador2_parado.set_total_duration(1000)
    cacador2 = cacador2_parado
    
    cacador2_colisao = Sprite('./Imagens/cacador/parado.png',1)
    
    ##########################   CAÇADOR 3   ############################### 
    cacador3_parado = Sprite("./Imagens/cacador/parado_up.png",1)
    cacador3_parado.set_position(335,575) #o player colisao guarda só 1 imagem
    cacador3_parado.set_total_duration(1000)
    cacador3 = cacador3_parado
    
    cacador3_colisao = Sprite('./Imagens/cacador/parado.png',1)
    
    ##########################   CAÇADOR 4   ############################### 
    cacador4_parado = Sprite("./Imagens/cacador/parado_left.png",1)
    cacador4_parado.set_position(616,212) #o player colisao guarda só 1 imagem
    cacador4_parado.set_total_duration(1000)
    cacador4 = cacador4_parado
        
    cacador4_colisao = Sprite('./Imagens/cacador/parado.png',1)

##########################   CAÇADOR 5   ############################### 
    cacador5_parado = Sprite("./Imagens/cacador/parado.png",1)
    cacador5_parado.set_position(98,287) #o player colisao guarda só 1 imagem
    cacador5_parado.set_total_duration(1000)
    cacador5 = cacador5_parado
    
    cacador5_colisao = Sprite('./Imagens/cacador/parado.png',1)
    
    ##########################   CAÇADOR 6   ############################### 
    cacador6_parado = Sprite("./Imagens/cacador/parado.png",1)
    cacador6_parado.set_position(151,133) #o player colisao guarda só 1 imagem
    cacador6_parado.set_total_duration(1000)
    cacador6 = cacador6_parado
    
    cacador6_colisao = Sprite('./Imagens/cacador/parado.png',1)
        
    #timer draw
    timer_cacador1 = 0
    timer_cacador2 = 0
    timer_cacador3 = 0
    timer_cacador4 = 0
    timer_cacador5 = 0
    timer_cacador6 = 0    

    #Ajustando a cabana e a colisão
    cabana = Sprite("./Imagens/level2/cabana.png", 1)
    cabana.set_total_duration(1000)
    cabana_colisao = Sprite("./Imagens/level2/cabana_colisao.png",1)
    cabana_colisao.set_position(516,404)
    
    tonel1_colisao = Sprite("./Imagens/level2/tonel_colisao.png",1)
    tonel1_colisao.set_position(6,148)
    
    tonel2_colisao = Sprite("./Imagens/level2/tonel_colisao.png",1)
    tonel2_colisao.set_position(6,330)
    
    tonel3_colisao = Sprite("./Imagens/level2/tonel_colisao.png",1)
    tonel3_colisao.set_position(6,590)

    FPS = 60
    clock = pygame.time.Clock()
    
    player_colisao = Sprite('./Imagens/player/parado.png',1)
    cacador1_colisao = Sprite("./Imagens/cacador/parado.png", 1)
    cacador2_colisao = Sprite("./Imagens/cacador/parado.png", 1)
    cacador3_colisao = Sprite("./Imagens/cacador/parado.png", 1)
    cacador4_colisao = Sprite("./Imagens/cacador/parado.png", 1)
    cacador5_colisao = Sprite("./Imagens/cacador/parado.png", 1)
    cacador6_colisao = Sprite("./Imagens/cacador/parado.png", 1)

    lancas_esq=[]
    lancas_dir =[]
    lancas_down = []
    lancas_up =[]
    recarga = 1
    vellanca = 800

        
    while True:
        #desenhando a colisão dos objetos para uso do collided_perfect
        player_colisao.draw()
        if (vida_cacador1>0):
            cacador1_colisao.draw()
        if (vida_cacador2>0):
            cacador2_colisao.draw()
        if (vida_cacador3>0):
            cacador3_colisao.draw()
        if (vida_cacador4>0):
            cacador4_colisao.draw()
        if (vida_cacador5>0):
            cacador5_colisao.draw()
        if (vida_cacador6>0):
            cacador6_colisao.draw()

        cabana_colisao.draw()

        #desenha fundo
        fundo.update()
        fundo.draw()
        
        clock.tick(FPS)
    
        # condição de voltar pro menu principal
        if comandos.key_pressed("esc"):
            menu.menu()
            
        #chamando a função pro personagem andar
        player,checkpos_player = jogador.movimento(janela, comandos, player, movimento,checkpos_player, colidiu)
        
        
        #fazendo o tiro dos caçadores
        if (vida_cacador1>0):
            tiro.novo_tiro_inimigo(cacador1, bala1)
            vida_player = tiro.tiro_inimigo(janela,bala1,velBalas, player, vida_player, cacador1)
        if (vida_cacador2>0):
            tiro.novo_tiro_inimigo(cacador2, bala2)
            vida_player = tiro.tiro_inimigo(janela,bala2,velBalas, player, vida_player, cacador2)
        if (vida_cacador3>0):
            tiro.novo_tiro_inimigo(cacador3, bala3)
            vida_player = tiro.tiro_inimigo(janela,bala3,velBalas, player, vida_player, cacador3)
        if (vida_cacador4>0):
            tiro.novo_tiro_inimigo(cacador4, bala4)
            vida_player = tiro.tiro_inimigo(janela,bala4,velBalas, player, vida_player, cacador4)
        if (vida_cacador5>0):  
            tiro.novo_tiro_inimigo(cacador5, bala5)
            vida_player = tiro.tiro_inimigo(janela,bala5,velBalas, player, vida_player, cacador5)
        if (vida_cacador6>0):
            tiro.novo_tiro_inimigo(cacador6, bala6)
            vida_player = tiro.tiro_inimigo(janela,bala6,velBalas, player, vida_player, cacador6)
        
        
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
        

        ##########################   PLAYER   ############################### 
        #se a player sair da tela na esquerda, ela fica grudada na borda esquerda
        if (player.x <0):
            player.x = 0
        #se a player sair da tela na direta, ela fica grudada na borda direira
        if vida_cacador1 > 0 and vida_cacador2 > 0 and vida_cacador3 > 0 and vida_cacador4 > 0 and vida_cacador5 > 0 and vida_cacador6 > 0 and player.x + player.width > janela.width: 
            player.x = janela.width - player.width
            
        if(vida_cacador1 <= 0 and vida_cacador2 <= 0 and vida_cacador3 <= 0 and vida_cacador4 <= 0 and vida_cacador5 <= 0 and vida_cacador6 <= 0 and player.x + player.width > janela.width):
            x = level2tolevel3.level2tolevel3(movimento, checkpos_player, player_colisao, colidiu, vida1, vida2, vida3, vida4, vida5, vida_player,som)

        if vida_cacador1 <= 0 and vida_cacador2 <= 0 and vida_cacador3 <= 0 and vida_cacador4 <= 0 and vida_cacador5 <= 0 and vida_cacador6 <= 0:
            popup.draw()


        #se a player sair da tela em cima, ela fica grudada na borda de cima
        if (player.y < 67):
            player.y = 67
            
        #se a player sair da tela embaixo, ela fica grudada na borda de baixo
        if (player.y + player.height > janela.height): 
            player.y = janela.height - player.height
            
        if checkpos_player == 1: player = jogador.set_player(player,player_esquerda)
        if checkpos_player == 2: player = jogador.set_player(player,player_direita)
        if checkpos_player == 3: player = jogador.set_player(player,player_up)
        if checkpos_player == 4: player = jogador.set_player(player,player_down)
        if checkpos_player == 0: player = jogador.set_player(player,player_parado)
        player.update()
            
        #checando a colisão do personagem
        player_colisao.x = player.x
        player_colisao.y = player.y
        player, colidiu = funcao.colisao_cenario(player, player_colisao, cabana_colisao, colidiu, checkpos_player)
        player, colidiu = funcao.colisao_cenario(player, player_colisao, tonel1_colisao, colidiu, checkpos_player)
        player, colidiu = funcao.colisao_cenario(player, player_colisao, tonel2_colisao, colidiu, checkpos_player)
        player, colidiu = funcao.colisao_cenario(player, player_colisao, tonel3_colisao, colidiu, checkpos_player)

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
        
        timer_cacador1,vida_cacador1 = tiro.colisaocacador(cacador1,vida_cacador1,lancas_dir,lancas_esq,lancas_up,lancas_down)
        timer_cacador2,vida_cacador2 = tiro.colisaocacador(cacador2,vida_cacador2,lancas_dir,lancas_esq,lancas_up,lancas_down)
        timer_cacador3,vida_cacador3 = tiro.colisaocacador(cacador3,vida_cacador3,lancas_dir,lancas_esq,lancas_up,lancas_down)
        timer_cacador4,vida_cacador4 = tiro.colisaocacador(cacador4,vida_cacador4,lancas_dir,lancas_esq,lancas_up,lancas_down)
        timer_cacador5,vida_cacador5 = tiro.colisaocacador(cacador5,vida_cacador5,lancas_dir,lancas_esq,lancas_up,lancas_down)
        timer_cacador6,vida_cacador6 = tiro.colisaocacador(cacador6,vida_cacador6,lancas_dir,lancas_esq,lancas_up,lancas_down)
                 
        if (timer_cacador1>0):
            timer_cacador1-=1
        if (timer_cacador2>0):
            timer_cacador2-=1
        if (timer_cacador3>0):
            timer_cacador3-=1
        if (timer_cacador4>0):
            timer_cacador4-=1
        if (timer_cacador5>0):
            timer_cacador5-=1
        if (timer_cacador6>0):
            timer_cacador6-=1   
            
    ##########################   CAÇADOR 1   ############################### 
        #se a cacador sair da tela na esquerda, ela fica grudada na borda esquerda
        if (cacador1.x <0):
            cacador1.x = 0
        #se a cacador sair da tela na direta, ela fica grudada na borda direira
        if (cacador1.x + cacador1.width > janela.width): 
            cacador1.x = janela.width - cacador1.width
                
        #se a cacador sair da tela em cima, ela fica grudada na borda de cima
        if (cacador1.y < 67):
            cacador1.y = 67
            
        #se a cacador sair da tela embaixo, ela fica grudada na borda de baixo
        if (cacador1.y + cacador1.height > janela.height): 
            cacador1.y = janela.height - cacador1.height
  
        if checkpos_cacador1 == 1: cacador1 = jogador.set_player(cacador1,cacador1_esquerda)
        if checkpos_cacador1 == 2: cacador1 = jogador.set_player(cacador1,cacador1_direita)
        if checkpos_cacador1 == 3: cacador1 = jogador.set_player(cacador1,cacador1_up)
        if checkpos_cacador1 == 4: cacador1 = jogador.set_player(cacador1,cacador1_down)
        if checkpos_cacador1 == 0: cacador1 = jogador.set_player(cacador1,cacador1_parado)
        cacador1.update()
        
        #checando a colisao dos soldados
        cacador1_colisao.x = cacador1.x
        cacador1_colisao.y = cacador1.y
        cacador1, colidiu_cacador1 = funcao.colisao_cenario(cacador1, cacador1_colisao, cabana_colisao, colidiu_cacador1, checkpos_cacador1)
        cacador1, colidiu_cacador1 = funcao.colisao_cenario(cacador1, cacador1_colisao, tonel1_colisao, colidiu_cacador1, checkpos_cacador1)
        cacador1, colidiu_cacador1 = funcao.colisao_cenario(cacador1, cacador1_colisao, tonel2_colisao, colidiu_cacador1, checkpos_cacador1)
        cacador1, colidiu_cacador1 = funcao.colisao_cenario(cacador1, cacador1_colisao, tonel3_colisao, colidiu_cacador1, checkpos_cacador1)
        
    ##########################   CAÇADOR 2   ############################### 
        #se a cacador sair da tela na esquerda, ela fica grudada na borda esquerda
        if (cacador2.x <0):
            cacador2.x = 0
        #se a cacador sair da tela na direta, ela fica grudada na borda direira
        if (cacador2.x + cacador2.width > janela.width): 
            cacador2.x = janela.width - cacador2.width
                
        #se a cacador sair da tela em cima, ela fica grudada na borda de cima
        if (cacador2.y < 67):
            cacador2.y = 67
            
        #se a cacador sair da tela embaixo, ela fica grudada na borda de baixo
        if (cacador2.y + cacador2.height > janela.height): 
            cacador2.y = janela.height - cacador2.height
  
        if checkpos_cacador2 == 1: cacador2 = jogador.set_player(cacador2,cacador2_esquerda)
        if checkpos_cacador2 == 2: cacador2 = jogador.set_player(cacador2,cacador2_direita)
        if checkpos_cacador2 == 3: cacador2 = jogador.set_player(cacador2,cacador2_up)
        if checkpos_cacador2 == 4: cacador2 = jogador.set_player(cacador2,cacador2_down)
        if checkpos_cacador2 == 0: cacador2 = jogador.set_player(cacador2,cacador2_parado)
        cacador2.update()
        
        #checando a colisao dos soldados
        cacador2_colisao.x = cacador2.x
        cacador2_colisao.y = cacador2.y
        cacador2, colidiu_cacador2 = funcao.colisao_cenario(cacador2, cacador2_colisao, cabana_colisao, colidiu_cacador2, checkpos_cacador2)
        cacador2, colidiu_cacador2 = funcao.colisao_cenario(cacador2, cacador2_colisao, tonel1_colisao, colidiu_cacador2, checkpos_cacador2)
        cacador2, colidiu_cacador2 = funcao.colisao_cenario(cacador2, cacador2_colisao, tonel2_colisao, colidiu_cacador2, checkpos_cacador2)
        cacador2, colidiu_cacador2 = funcao.colisao_cenario(cacador2, cacador2_colisao, tonel3_colisao, colidiu_cacador2, checkpos_cacador2)
        
    ##########################   CAÇADOR 3   ############################### 
        #se a cacador sair da tela na esquerda, ela fica grudada na borda esquerda
        if (cacador3.x <0):
            cacador3.x = 0
        #se a cacador sair da tela na direta, ela fica grudada na borda direira
        if (cacador3.x + cacador3.width > janela.width): 
            cacador3.x = janela.width - cacador3.width
                
        #se a cacador sair da tela em cima, ela fica grudada na borda de cima
        if (cacador3.y < 67):
            cacador3.y = 67
            
        #se a cacador sair da tela embaixo, ela fica grudada na borda de baixo
        if (cacador3.y + cacador3.height > janela.height): 
            cacador3.y = janela.height - cacador3.height
  
        if checkpos_cacador3 == 1: cacador3 = jogador.set_player(cacador3,cacador3_esquerda)
        if checkpos_cacador3 == 2: cacador3 = jogador.set_player(cacador3,cacador3_direita)
        if checkpos_cacador3 == 3: cacador3 = jogador.set_player(cacador3,cacador3_up)
        if checkpos_cacador3 == 4: cacador3 = jogador.set_player(cacador3,cacador3_down)
        if checkpos_cacador3 == 0: cacador3 = jogador.set_player(cacador3,cacador3_parado)
        cacador3.update()
        
        #checando a colisao dos soldados
        cacador3_colisao.x = cacador3.x
        cacador3_colisao.y = cacador3.y
        cacador3, colidiu_cacador3 = funcao.colisao_cenario(cacador3, cacador3_colisao, cabana_colisao, colidiu_cacador3, checkpos_cacador3)
        cacador3, colidiu_cacador3 = funcao.colisao_cenario(cacador3, cacador3_colisao, tonel1_colisao, colidiu_cacador3, checkpos_cacador3)
        cacador3, colidiu_cacador3 = funcao.colisao_cenario(cacador3, cacador3_colisao, tonel2_colisao, colidiu_cacador3, checkpos_cacador3)
        cacador3, colidiu_cacador3 = funcao.colisao_cenario(cacador3, cacador3_colisao, tonel3_colisao, colidiu_cacador3, checkpos_cacador3)
        
    ##########################   CAÇADOR 4   ############################### 
        #se a cacador sair da tela na esquerda, ela fica grudada na borda esquerda
        if (cacador4.x <0):
            cacador4.x = 0
        #se a cacador sair da tela na direta, ela fica grudada na borda direira
        if (cacador4.x + cacador4.width > janela.width): 
            cacador4.x = janela.width - cacador4.width
                
        #se a cacador sair da tela em cima, ela fica grudada na borda de cima
        if (cacador4.y < 67):
            cacador4.y = 67
            
        #se a cacador sair da tela embaixo, ela fica grudada na borda de baixo
        if (cacador4.y + cacador4.height > janela.height): 
            cacador4.y = janela.height - cacador4.height
  
        if checkpos_cacador4 == 1: cacador4 = jogador.set_player(cacador4,cacador4_esquerda)
        if checkpos_cacador4 == 2: cacador4 = jogador.set_player(cacador4,cacador4_direita)
        if checkpos_cacador4 == 3: cacador4 = jogador.set_player(cacador4,cacador4_up)
        if checkpos_cacador4 == 4: cacador4 = jogador.set_player(cacador4,cacador4_down)
        if checkpos_cacador4 == 0: cacador4 = jogador.set_player(cacador4,cacador4_parado)
        cacador4.update()
        
        #checando a colisao dos soldados
        cacador4_colisao.x = cacador4.x
        cacador4_colisao.y = cacador4.y
        cacador4, colidiu_cacador4 = funcao.colisao_cenario(cacador4, cacador4_colisao, cabana_colisao, colidiu_cacador4, checkpos_cacador4)
        cacador4, colidiu_cacador4 = funcao.colisao_cenario(cacador4, cacador4_colisao, tonel1_colisao, colidiu_cacador4, checkpos_cacador4)
        cacador4, colidiu_cacador4 = funcao.colisao_cenario(cacador4, cacador4_colisao, tonel2_colisao, colidiu_cacador4, checkpos_cacador4)
        cacador4, colidiu_cacador4 = funcao.colisao_cenario(cacador4, cacador4_colisao, tonel3_colisao, colidiu_cacador4, checkpos_cacador4)
        
        ##########################   CAÇADOR 5   ############################### 
        #se a cacador sair da tela na esquerda, ela fica grudada na borda esquerda
        if (cacador5.x <0):
            cacador5.x = 0
        #se a cacador sair da tela na direta, ela fica grudada na borda direira
        if (cacador5.x + cacador5.width > janela.width): 
            cacador5.x = janela.width - cacador5.width
                
        #se a cacador sair da tela em cima, ela fica grudada na borda de cima
        if (cacador5.y < 67):
            cacador5.y = 67
            
        #se a cacador sair da tela embaixo, ela fica grudada na borda de baixo
        if (cacador5.y + cacador5.height > janela.height): 
            cacador5.y = janela.height - cacador5.height
  
        if checkpos_cacador5 == 1: cacador5 = jogador.set_player(cacador5,cacador5_esquerda)
        if checkpos_cacador5 == 2: cacador5 = jogador.set_player(cacador5,cacador5_direita)
        if checkpos_cacador5 == 3: cacador5 = jogador.set_player(cacador5,cacador5_up)
        if checkpos_cacador5 == 4: cacador5 = jogador.set_player(cacador5,cacador5_down)
        if checkpos_cacador5 == 0: cacador5 = jogador.set_player(cacador5,cacador5_parado)
        cacador5.update()
        
        #checando a colisao dos soldados
        cacador5_colisao.x = cacador5.x
        cacador5_colisao.y = cacador5.y
        cacador5, colidiu_cacador5 = funcao.colisao_cenario(cacador5, cacador5_colisao, cabana_colisao, colidiu_cacador5, checkpos_cacador5)
        cacador5, colidiu_cacador5 = funcao.colisao_cenario(cacador5, cacador5_colisao, tonel1_colisao, colidiu_cacador5, checkpos_cacador5)
        cacador5, colidiu_cacador5 = funcao.colisao_cenario(cacador5, cacador5_colisao, tonel2_colisao, colidiu_cacador5, checkpos_cacador5)
        cacador5, colidiu_cacador5 = funcao.colisao_cenario(cacador5, cacador5_colisao, tonel3_colisao, colidiu_cacador5, checkpos_cacador5)
        
        ##########################   CAÇADOR 6   ############################### 
        #se a cacador sair da tela na esquerda, ela fica grudada na borda esquerda
        if (cacador6.x <0):
            cacador6.x = 0
        #se a cacador sair da tela na direta, ela fica grudada na borda direira
        if (cacador6.x + cacador6.width > janela.width): 
            cacador6.x = janela.width - cacador6.width
                
        #se a cacador sair da tela em cima, ela fica grudada na borda de cima
        if (cacador6.y < 67):
            cacador6.y = 67
            
        #se a cacador sair da tela embaixo, ela fica grudada na borda de baixo
        if (cacador6.y + cacador6.height > janela.height): 
            cacador6.y = janela.height - cacador6.height
  
        if checkpos_cacador6 == 1: cacador6 = jogador.set_player(cacador6,cacador6_esquerda)
        if checkpos_cacador6 == 2: cacador6 = jogador.set_player(cacador6,cacador6_direita)
        if checkpos_cacador6 == 3: cacador6 = jogador.set_player(cacador6,cacador6_up)
        if checkpos_cacador6 == 4: cacador6 = jogador.set_player(cacador6,cacador6_down)
        if checkpos_cacador6 == 0: cacador6 = jogador.set_player(cacador6,cacador6_parado)
        cacador6.update()
        
        #checando a colisao dos soldados
        cacador6_colisao.x = cacador6.x
        cacador6_colisao.y = cacador6.y
        cacador6, colidiu_cacador6 = funcao.colisao_cenario(cacador6, cacador6_colisao, cabana_colisao, colidiu_cacador6, checkpos_cacador6)
        cacador6, colidiu_cacador6 = funcao.colisao_cenario(cacador6, cacador6_colisao, tonel1_colisao, colidiu_cacador6, checkpos_cacador6)
        cacador6, colidiu_cacador6 = funcao.colisao_cenario(cacador6, cacador6_colisao, tonel2_colisao, colidiu_cacador6, checkpos_cacador6)
        cacador6, colidiu_cacador6 = funcao.colisao_cenario(cacador6, cacador6_colisao, tonel3_colisao, colidiu_cacador6, checkpos_cacador6)

        if (vida_cacador1>0):
            player, colidiu = funcao.colisao_cenario(player, player_colisao, cacador1, colidiu, checkpos_player)
        if (vida_cacador2>0):
            player, colidiu = funcao.colisao_cenario(player, player_colisao, cacador2, colidiu, checkpos_player)
        if (vida_cacador3>0):
            player, colidiu = funcao.colisao_cenario(player, player_colisao, cacador3, colidiu, checkpos_player)
        if (vida_cacador4>0):
            player, colidiu = funcao.colisao_cenario(player, player_colisao, cacador4, colidiu, checkpos_player)
        if (vida_cacador5>0):
            player, colidiu = funcao.colisao_cenario(player, player_colisao, cacador5, colidiu, checkpos_player)
        if (vida_cacador6>0):
            player, colidiu = funcao.colisao_cenario(player, player_colisao, cacador6, colidiu, checkpos_player)

        if (vida_cacador1 > 0 or vida_cacador2 > 0 or vida_cacador3 > 0 or vida_cacador4 > 0 or vida_cacador5 > 0 or vida_cacador6 > 0 ):
            if(player.x + player.width == janela.width):
                player.x = janela.width - player.width

        #desenhando o player
        player.draw()
        if(vida_cacador1 > 0 and timer_cacador1 % 2 == 0):
            cacador1.draw()
        if(vida_cacador2 > 0 and timer_cacador2 % 2 == 0):
            cacador2.draw()
        if(vida_cacador3 > 0 and timer_cacador3 % 2 == 0):
            cacador3.draw()
        if(vida_cacador4 > 0 and timer_cacador4 % 2 == 0):
            cacador4.draw()
        if(vida_cacador5 > 0 and timer_cacador5 % 2 == 0):
            cacador5.draw()
        if(vida_cacador6 > 0 and timer_cacador6 % 2 == 0):
            cacador6.draw()
        vida1.draw()
        vida2.draw()
        vida3.draw()
        vida4.draw()
        vida5.draw()
        
        funcao.posição(cabana, 481, 348)
        
        janela.update()