from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.sound import*


#Função para criar inimigos
def cria_monstro(linha,coluna,matrizDeInimigos):    
    for i in range(linha):
        linhas = []
        for j in range(coluna):
            
            if linha<6:
                if i==0:
                    monstro = Sprite("imagens/monstro_roxo.png",1)
                elif i==linha-1:
                    monstro = Sprite("imagens/monstro_verde.png",1)
                elif i==linha-2:
                    monstro = Sprite("imagens/monstro_rosa.png",1)
                else:
                    monstro = Sprite("imagens/monstro_agua.png",1)
                    
            if linha>=6:
                if i==0:
                    monstro = Sprite("imagens/monstro3.png",1)
                elif i==linha-2:
                    monstro = Sprite("imagens/monstro1.png",1)
                elif i==linha-1:
                    inimigoBonus = Sprite("imagens/monstro4.png",1)
                    inimigoBonus.x = 50
                    inimigoBonus.y = 50
                    break
                else:
                    monstro = Sprite("imagens/monstro2.png",1)
            monstro.x = 75 * j 
            monstro.y = 50 * i
            linhas.append((monstro,1))
            
        matrizDeInimigos.append(linhas)
    
    if linha>=6:
        return inimigoBonus
    
    
#Função de desenhar
def desenhar_inimigo(matrizDeInimigos):
    
    for linha in range(len(matrizDeInimigos)-1,-1,-1):
        for monstro in matrizDeInimigos[linha]:
            monstro[0].draw()


#Função que move os inimigos
def move_monstro(janela, matrizDeInimigos, movimentoInimigo):
    bateu = False
    
    for i in matrizDeInimigos:
        for j in i:
            j[0].x += movimentoInimigo*janela.delta_time()
            if ((j[0].x >= janela.width - j[0].width - 5) or (j[0].x<-5)):
                bateu = True
                
    if (bateu):
        movimentoInimigo *= -1
        for i in matrizDeInimigos:
            for j in i:
                j[0].x += movimentoInimigo*janela.delta_time()
                j[0].y += 20 #rapidez dos monstros
                
    return movimentoInimigo


# interseção de cada tiro com cada monstro se rolar colisão exclui o tiro e o monstro das listas 
#numero de vidas do player

#resolvendo os pontos aqui também
def matar(listaProjeteis,matrizDeInimigos,pontos,linha,movimentoInimigo):
    for k,linhaDeInimigos in enumerate(matrizDeInimigos):
        for i,inimigo in enumerate(linhaDeInimigos):
            for j,projetil in enumerate(listaProjeteis):
                
                    if (projetil.collided(inimigo[0])):
                        listaProjeteis.pop(j)
                        linhaDeInimigos[i]=(inimigo[0],inimigo[1]-1)
                        
                        if linhaDeInimigos[i][1]<=0:
                            linhaDeInimigos.pop(i)
                            if k==0:
                                pontos+=20
                                
                            elif i==linha-2:
                                pontos+= 15
                                
                            elif k==linha-1:
                                pontos+=10
                                
                            else:
                                pontos+=5
                            movimentoInimigo*=1.01
                            
    return pontos,movimentoInimigo

def bater(vidas,nave,listaDeInimigos,listaProjeteisInimigos,pontos, cont, ver_especial):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if(projetil.collided(nave) and cont % 3 == 0):
            ver_especial = True
        if (projetil.collided(nave) and cont % 3 != 0):
            listaProjeteisInimigos.pop(i)
            vidas-=1    

    return vidas, ver_especial
