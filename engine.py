"""Zona del Motor: coordinación del juego."""

from entities import Guerrero, Mago, Enemigo

class Game:
    """
    Motor principal del juego.

    Coordina la inicialización, el loop de turnos
    y la resolución final de la partida.
    No hace print() ni input()
    """
    def __init__(self, ui) -> None:
        """
        Recibe la UI como dependencia.
        El jugador y enemigo se crean en iniciar().
        """
        self.__ui = ui
        self.__jugador = None   # Todavía no existe
        self.__enemigo = None   # Se crea en iniciar()

    def iniciar(self) -> None:
        """
        Configura la partida: muestra bienvenida,
        pregunta la clase al jugador a través de la UI,
        y crea las instancias del jugador y el enemigo.
        """
        self.__ui.mostrar_bienvenida()
        eleccion = self.__ui.elegir_clase() # La UI pregunta y retorna la respuesta
        if eleccion == 'guerrero':
            self.__jugador = Guerrero()
        else:
            self.__jugador = Mago()

        self.__enemigo = Enemigo(nombre='El Guardián del Silencio', vida_maxima=100, poder_ataque=15)

    def loop_principal(self) -> None:
        """
        Ejecuta el ciclo de turnos mientras ambos estén vivos.
        Cada turno: muestra estado, el jugador ataca,
        y si el enemigo sobrevive, contraataca.
        """
        while self.__jugador.esta_vivo() and self.__enemigo.esta_vivo():
            self.__ui.mostrar_estado(self.__jugador, self.__enemigo)
            danho_jugador = self.__jugador.atacar(self.__enemigo)
            self.__ui.narrar_ataque(self.__jugador, self.__enemigo, danho_jugador)

            if self.__enemigo.esta_vivo():
                danho_enemigo = self.__enemigo.atacar(self.__jugador)
                self.__ui.narrar_ataque(self.__enemigo, self.__jugador, danho_enemigo)

    def resolver_turno(self) -> None:
        """
        Evalúa quién ganó al terminar el loop
        y le pasa el ganador a la UI para mostrarlo.
        """
        if self.__jugador.esta_vivo():
            self.__ui.mostrar_resultado(self.__jugador)
        else:
            self.__ui.mostrar_resultado(self.__enemigo)

    def ejecutar(self) -> None:
        """
        Método coordinador: ejecuta la secuencia completa
        del juego en el orden correcto.
        Es el único método que main.py necesita llamar.
        """
        self.iniciar()
        self.loop_principal()
        self.resolver_turno()