from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import*
import menu

control = Mouse()

def main():
    janela = Window(800, 630)
    janela.set_title("Space Invaders")
    menu.Menu()

main()

