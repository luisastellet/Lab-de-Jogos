from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import*
import menu
import pontinhos


control = Mouse()

def rank():
    janela = Window(800, 630)

    teclado = janela.get_keyboard()

    fundo = GameImage("Imagens/fundo.png")

    # Organizo o arquivo txt em ordem decrescente
    pontuacao = pontinhos.arquivo_to_codigo('Pontuacao.txt')
        
    while (True):
        # Desenho o fundo
        limite = 0
        altura = 200
        fundo.draw()
        
        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            menu.Menu()
        
        # Desenho o texto titulo na janela
        janela.draw_text(("RANKING"), (janela.width / 2)-130, 80, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
        
        for i,conteudo in enumerate(pontuacao):
            if limite<5:
                janela.draw_text(str(i+1), 200, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
                janela.draw_text(("."), 230, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
                janela.draw_text(str(conteudo), 300, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
                altura += 50
                limite+=1
            
        
        # Defino o titulo do jogo
        janela.set_title("Space Invaders")
        
        # Atualizo o GameLoop
        janela.update()



