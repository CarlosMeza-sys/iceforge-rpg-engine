"""Zona de dominio."""

from abc import ABC, abstractmethod
import random

class Personaje(ABC):
    """
    Clase base abstracta para toda entidad combatiente del juego.

    No se puede instanciar directamente (es un contrato).
    Toda clase hija DEBE implementar el método atacar().

    Atributos (privados):
        __nombre: Identificador del personaje.
        __vida_maxima: Tope de vida (útil si luego se quiere curar sin pasarte).
        __vida_actual: Vida en tiempo real, arranca igual a vida_maxima.
        __poder_ataque: Base numérica que cada clase hija usa a su manera.
    """
    def __init__(self, nombre: str, vida_maxima: int, poder_ataque: int):
        self.__nombre = nombre
        self.__vida_maxima = vida_maxima
        self.__vida_actual = vida_maxima
        self.__poder_ataque = poder_ataque

    # ----- Getters -----

    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_vida_actual(self) -> int:
        return self.__vida_actual
    
    def get_vida_maxima(self) -> int:
        return self.__vida_maxima
    
    def get_poder_ataque(self) -> int:
        """
        Las clases hijas necesitan este getter para implementar atacar().
        Sin él, no pueden acceder a __poder_ataque (es privado del padre).
        """
        return self.__poder_ataque
    
    # ----- Logica de comportamiento compartido -----
    
    def esta_vivo(self) -> bool:
        """Determina si el personaje sigue en combate."""
        return self.__vida_actual > 0
    
    def recibir_danho(self, cantidad: int) -> int:
        """
        Aplica daño al personaje. Garantiza que la vida no baje de 0.
 
        Args:
            cantidad: Puntos de daño a recibir.
 
        Returns:
            El daño efectivamente aplicado a la vida actual.
            Ejemplo: si tiene 5 de vida y recibe 20, el daño real fue 5.
        """
        vida_antes = self.__vida_actual
        self.__vida_actual = max(0, self.__vida_actual - cantidad)
        # Retornar el daño real.
        return vida_antes - self.__vida_actual
    
    # ----- Contrato Abstracto -----
    @abstractmethod
    def atacar(self, objetivo: 'Personaje') -> int:
        """
        Define como ataca este personaje a otro.

        Cada clase hija implementa su propia versión.
        El motor (engine.py) llama atacar() sin importar si es
        Guerrero, Mago o Enemigo — eso es el poder del polimorfismo.

        Args:
            objetivo: El personaje que recibe el ataque.
 
        Returns:
            El daño infligido (para que la UI pueda narrarlo).
        """
        pass