from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
import game
import dif
import rank

control = Mouse()

def Menu():
    dificuldade = 1
    janela_menu = Window(800, 630)
    
    play_button = Sprite("./imagens/Jogar(1).png")
    janela_menu.set_title("Space Invaders")
    
    play_button.set_position(janela_menu.width / 2 - (play_button.width / 2), 80)
    dif_button = Sprite("./imagens/dif(1).png")
    
    dif_button.set_position(janela_menu.width/ 2 - (play_button.width / 2), 210)
    rank_button = Sprite("./imagens/Jogar(2)(1).png")
    
    rank_button.set_position(janela_menu.width / 2 - (play_button.width / 2), 340)
    exit_button = Sprite("./imagens/Jogar(3)(1).png")
    
    exit_button.set_position(janela_menu.width / 2 - (play_button.width / 2), 470)
    menu_background = Sprite("./imagens/menuvangogh.jpg")
    
    while True:
        menu_background.draw()
        if control.is_over_object(play_button) and control.is_button_pressed(1):
            game.Game(dificuldade)
        if control.is_over_object(dif_button) and control.is_button_pressed(1):
            dificuldade = dif.Dif()
        if control.is_over_object(rank_button) and control.is_button_pressed(1):
            rank.rank()
        if control.is_over_object(exit_button) and control.is_button_pressed(1):
            exit(1)
        play_button.draw()
        dif_button.draw()
        rank_button.draw()
        exit_button.draw()
        janela_menu.update()