from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.collision import*
import tiro
import menu
import inimigo
import pontinhos

control = Mouse()

def Game(dificuldade):
    janela_game = Window(800, 630)
    janela_game.set_title("Space Invaders")
    
    teclado = janela_game.get_keyboard()
    
    #Criando a nave
    nave = Sprite("./imagens/spaceship.png")
    invencivel = Sprite("./imagens/invencivel.png",1)
    nave.x = (janela_game.width - janela_game.height) / 2
    nave.y = janela_game.height - nave.height
    velnave = 200
    
    background = Sprite("./imagens/fundo.png")
    # background = Sprite("./imagens/noite_estrelada.jpg")
    background.set_position((janela_game.width-background.width)/2,(janela_game.height-background.height))
    

    #CRIAÇÃO DOS DISPAROS
    disparos = []
    disparos_inimigos = []
    recarga = 1
    veltiro = 300
    veltiro_inimigo = 400
    
    # Defino o frame per second
    FPS = 60
    clock = pygame.time.Clock()
    
    # Crio o vetor de inimigos
    matrizDeInimigos = []
    movimentoInimigo = 50 * dificuldade
    movimentoInimigoBase = movimentoInimigo
    linha = 4
    coluna = 10
    
    vidas = 3
    pontos = 0
    delay = 0
    delay_invencivel = 0
    delay_inimigo = 100
    TomeiDano = False
    ver_especial = False
    estatico = 0
    
    cont = 0
     
    while True:
        background.draw()
        
        #Contando o fps
        clock.tick(FPS)
          
        #Se o esc for apertado, retorna para o menu
        if teclado.key_pressed('esc'):
            menu.Menu()
        
        #COMANDOS RELACIONADOS A NAVE:

        #Movimentação
        if (teclado.key_pressed("A") or teclado.key_pressed("LEFT")):
            nave.x -= velnave * janela_game.delta_time()
        if (teclado.key_pressed("D") or teclado.key_pressed("RIGHT")):
            nave.x += velnave * janela_game.delta_time()

        #Limitando a nave na tela
        if (nave.x <= 0):
            nave.x = 0
        if (nave.x >= janela_game.width - nave.width):
            nave.x = janela_game.width - nave.width
           
        #Criando os inimigos
        if (len(matrizDeInimigos)==0):
            inimigo.cria_monstro(linha,coluna,matrizDeInimigos)
        
        # Recrio a matriz apos matar todos os aliens
        for i in matrizDeInimigos:
            if (len(i)==0):
                vazio = True
            else:
                vazio = False
                break
        if vazio:    
            matrizDeInimigos.clear()
            movimentoInimigo = movimentoInimigoBase
            nave.x = janela_game.width/2-nave.width/2
            delay_invencivel = 180
            if linha<5:
                linha+=1
                movimentoInimigo *= 1.5 * dificuldade
                movimentoInimigoBase *= 1.5 * dificuldade
                inimigo.cria_monstro(linha,coluna,matrizDeInimigos)
            
        #Fazendo os inimigos andarem
        movimentoInimigo = inimigo.move_monstro(janela_game, matrizDeInimigos, movimentoInimigo)

        #COMANDOS RELACIONADOS A TIROS:
        recarga += janela_game.delta_time()

        #ativar o tiro assim que o espaço for pressionado e respeitando o tempo de recarga
        if (teclado.key_pressed("space")) and (recarga >= 1/2) and (estatico <= 0):
            disparos = tiro.novo_tiro(nave,disparos)
            recarga = 0

        #desenha, controla e limita o disparo
        if (disparos != []):
            for d in disparos:
                d.draw()
                d.y -= veltiro * janela_game.delta_time()
                d = tiro.limitando_tiro(d, disparos)
                
        if (delay_inimigo == 0):
            for i in matrizDeInimigos:
                cont += 1
                for j in i:
                    tiro.novo_tiro_inimigo(j,disparos_inimigos, cont)
            delay_inimigo = tiro.delay_inimigo(delay_inimigo,linha)
        
        # Faço o movimento dos tiros
        tiro.tiro_inimigo(janela_game,disparos_inimigos,veltiro_inimigo, cont)
        
        if delay>0:
            delay-=1
        if delay_inimigo>0:
            delay_inimigo-=1
        
        if delay_invencivel>0:
            delay_invencivel-=1
            invencivel.x = nave.x
            invencivel.y = nave.y
            invencivel.draw()
        else:
            nave.draw()
            
        if(ver_especial):
            posX = nave.x
            posY = nave.y
            estatico = 120
            ver_especial = False

        if(estatico > 0):
            estatico -= 1
            nave.x = posX
            nave.y = posY
            
            
            
        vidasAntes = vidas
        #Matando os inimigos
        pontos, movimentoInimigo = inimigo.matar(disparos,matrizDeInimigos,pontos,linha,movimentoInimigo)
        
        if (vidas>0 and delay_invencivel==0):
            for i in matrizDeInimigos:
                vidas, ver_especial = inimigo.bater(vidas, nave, i, disparos_inimigos,pontos, cont, ver_especial)
                if vidas != vidasAntes:
                    TomeiDano=True
        if TomeiDano:
            nave.x= janela_game.width/2-nave.width/2
            delay_invencivel = 90
            TomeiDano = False
            
        # Desenho os inimigos
        inimigo.desenhar_inimigo(matrizDeInimigos)
        
        # nave.draw()
        
        #Perco do jogo
        if (vidas <= 0):
            pontinhos.fim_de_jogo(pontos)
        for i in range(len(matrizDeInimigos)-1,-1,-1):
            for j in matrizDeInimigos[i]:
                if j[0].collided(nave) or j[0].y >= (nave.y-nave.height/2):
                    pontinhos.fim_de_jogo(pontos)        
        
        #escrevendo na tela o placar
        # janela_game.draw_text("{}".format(clock), janela_game.width/2-60, 50, size=25, color=(255,255,255), font_name="Arial", bold=True, italic=True)
        # Desenho a pontuação
        janela_game.draw_text(("Pontos: "), janela_game.width-150, 0, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela_game.draw_text(str(pontos), janela_game.width-58, 0, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Desenho a vida
        janela_game.draw_text(("Vidas: "), 35, 0, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela_game.draw_text(str(vidas), 110, 0, size=24, font_name="Arial", bold=True,color=[186,85,211])
        
        janela_game.update()