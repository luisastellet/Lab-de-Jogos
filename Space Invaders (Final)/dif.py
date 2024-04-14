from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *

control = Mouse()

def Dif():
    janela_dif = Window(800, 630)
    teclado = janela_dif.get_keyboard()
    
    easy_button = Sprite("./imagens/facil.png")
    easy_button.set_position(janela_dif.width / 2 - (easy_button.width / 2), 120)
    
    med_button = Sprite("./imagens/medio.png")
    med_button.set_position(janela_dif.width/ 2 - (easy_button.width / 2), 270)
    
    dificil_button = Sprite("./imagens/dificil.png")
    dificil_button.set_position(janela_dif.width / 2 - (easy_button.width / 2), 420)
    
    dif_background = Sprite("./imagens/van-gogh-girassois.jpg")
    
    while not teclado.key_pressed("esc"):
        if control.is_over_object(easy_button) and control.is_button_pressed(1):
            return 1
        if control.is_over_object(med_button) and control.is_button_pressed(1):
            return 2
        if control.is_over_object(dificil_button) and control.is_button_pressed(1):
            return 3
        
        dif_background.draw()
        easy_button.draw()
        med_button.draw()
        dificil_button.draw()
        janela_dif.update()