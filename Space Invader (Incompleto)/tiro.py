#importando as bibliotecas
from PPlay.sprite import*
from PPlay.collision import*

#criando a função de criar tiro
def cria_tiro(nave,listaProjeteis):
    
    #Crio o projetil
    projetil = Sprite("imagens/projetil.png")
    
    #definindo a posição da nave
    projetil.x = nave.x + 20
    projetil.y = nave.y - projetil.height
    
    #appendando na lista o projétil a cada vez que aciona a barra SPACE
    listaProjeteis.append(projetil)

#criando a função de desenhar o tiro
def tiro(janela,listaProjeteis,velProjetil):
    
    #criando um for para ler o vetor de tiros
    for i in listaProjeteis:
        #ajustando para os tiros saírem na vertical
        i.y -= velProjetil*janela.delta_time()
        
        #desenhando os tiros
        i.draw()
        
        #se o tiro sair da tela, remover da lista
        if (i.y<-50):
            listaProjeteis.remove(i)