from engine import Game
from ui import Consola

if __name__ == "__main__":
    ui = Consola()
    juego = Game(ui)
    juego.ejecutar()