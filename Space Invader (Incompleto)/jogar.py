#importando as bibliotecas
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

#importando outros arquivos
import jogador
import tiro
import menu

#criando a função principal com retorno inteiro
def jogar():

    #arrumando o tamanho da tela e o título da página
    janela = Window(800,514)
    janela.set_title("Space Invaders")

    #criando os comandos de teclado
    comandos = janela.get_keyboard()

    #criando o fundo
    fundo = GameImage("imagens/fundo.png")

    #Definição da posição do player
    nave = Sprite("imagens/nave1.png",1)
    nave.x = janela.width/2
    nave.y = janela.height - nave.height - 20 #20 foi no chute pra ficar bonitinho

    #criando a velocidade da nave = movimento
    movimento = 200
    # Criando array de tiros
    balas = []
    #definindo as configurações dos tiros
    velBalas = 600
    contador = 0

    #loop
    while True:
        # Desenha fundo
        fundo.draw()
        
        # condição de voltar pro menu principal
        if comandos.key_pressed("esc"):
            menu.menu()
        
        #chamando a função pra nave andar
        jogador.jogador(janela, comandos, nave, movimento)

        #criando a condição de apertar SPACE para chamar a função dos tiros
        if(comandos.key_pressed("SPACE") and (contador>0.5)): #esse 0.5 é ajustável e quanto menor ele fica, mais tiros ficam na tela
            #chama a função de criar os tiros
            tiro.cria_tiro(nave,balas)
            contador = 0
        
        #chamando a função de atirar mesmo    
        tiro.tiro(janela,balas,velBalas)
        contador += janela.delta_time()

        #desenhando a nave
        nave.draw()

        janela.update()