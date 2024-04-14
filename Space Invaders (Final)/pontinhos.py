from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import*
import menu


control = Mouse()

def chave_ordenacao(item):
    return int(item.split(' - ')[0])  # Obtém a pontuação convertida para inteiro


def fim_de_jogo(score):
    janela = Window(800,630)
    
    teclado = janela.get_keyboard()
    
    fundo = GameImage("Imagens/fundo.png")
    
    nome = input("Entre com o seu nome: ")
    
    # Abro o arquivo (leitura)
    arquivo = open('Pontuacao.txt', 'r')
    conteudo = arquivo.readlines()

    # Insiro o conteúdo
    if len(conteudo) > 0: conteudo.append(".")
    
    conteudo.append(str(score) + " - " + nome)
    arquivo.close()
    
    # Abre novamente o arquivo (escrita)
    arquivo = open('Pontuacao.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
    
    while (True):
        #Desenho o fundo
        fundo.draw()

            
        janela.draw_text(("Você foi derrotado! Boa sorte na proxima vez!"), 136, 239, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Aperte 'ESC' para voltar ao menu"), 204, 334, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Instancio o titulo da janela  
        janela.set_title("Space Invaders")
        
        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            menu.Menu()
            
        # Atualizo o GameLoop
        janela.update()
        
def chave_ordenacao(item):
    parts = item.split(' - ')
    if len(parts) > 0 and parts[0].isdigit():
        return int(parts[0])
    return 0  # Retorna 0 ou outro valor padrão se a conversão f  # Obtém a pontuação convertida para inteiro

def arquivo_to_codigo(file):
    arquivo = open(file)
    pontuacao = []
    for elemento in arquivo:
        temp = elemento.split(".")
        for i in temp:
            if i != '':
                pontuacao.append(i)
    arquivo.close()
    
# Ordena a lista com base na pontuação
    print(pontuacao)
    pontuacao.sort(key=chave_ordenacao, reverse=True)
    print(pontuacao)

    return pontuacao
