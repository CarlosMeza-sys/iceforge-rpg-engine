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
    
    # ----- Setter -----

    def _set_vida_actual(self, nueva_vida: int) -> None:
        """
        Método protegido: permite a las clases hijas modificar la vida
        de forma controlada, sin exponer el atributo directamente.
        """
        self.__vida_actual = nueva_vida
    
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

class Guerrero(Personaje):
    """
    Clase tanque: daño constante y predecible.
    Su atacar() siempre hace el mismo daño.
    """
    def __init__(self):
        # El Guerrero SIEMPRE tiene estos stats base.
        super().__init__(nombre='El Rompehielos', vida_maxima=100, poder_ataque=15)
    
    def atacar(self, objetivo: 'Personaje') -> int:
        """Ataque directo: daño constante basado en poder_ataque."""
        danho_base = self.get_poder_ataque()
        danho_real = objetivo.recibir_danho(danho_base)
        return danho_real
    
class Mago(Personaje):
    """
    Clase de alto riesgo / alta recompensa.

    Su atacar() tiene probabilidad de golpe crítico (x2),
    golpe normal o fallar. Usa random para decidir.
 
    Atributos adicionales (privados):
        __probabilidad_critico: Chance de hacer mas daño.
        __probabilidad_fallo: Chance de fallar el ataque.
    """
    def __init__(self):

        super().__init__(nombre='El Mago de la Chispa', vida_maxima=80, poder_ataque=20)
        self.__probabilidad_critico = 0.3   # 30% de chance de crítico
        self.__probabilidad_fallo = 0.2     # 20% de chance de fallar

    def atacar(self, objetivo: "Personaje") -> int:
        """
        Ataque mágico con chances de crítico y fallo.

        Tira un número entre 0 y 1:
        Si cae dentro de la probabilidad de fallo,
        el daño es 0.
        Si cae dentro del rango de la probabilidad
        del golpe critico, el daño se duplica.
        Si no, hace daño normal.
        """
        danho_base = self.get_poder_ataque()
        probabilidad = random.random()
        if probabilidad <= self.__probabilidad_fallo:
            danho = 0
        elif probabilidad >= 1.0 - self.__probabilidad_critico:
            danho = danho_base * 2  # Golpe crítico
        else:
            danho = danho_base
        
        return objetivo.recibir_danho(danho)

class Enemigo(Personaje):
    """
    Entidad hostil controlada por el sistema (no por el jugador).
 
    Su atacar() incluye una decisión interna: puede atacar normal
    o defenderse (no hacer daño pero recuperar algo de vida).

    Atributos adicionales (privados):
        __probabilidad_defensa: Chance de que elija defenderse (0.0 a 1.0).
    """
    def __init__(self, nombre: str, vida_maxima: int, poder_ataque: int):
        # El Enemigo recibe stats variables.
        # Esto hace la clase más extensible sin necesidad de crear subclases.
        super().__init__(nombre=nombre, vida_maxima=vida_maxima, poder_ataque=poder_ataque)
        self.__probabilidad_defensa = 0.25  # 25% de chance de defenderse

    def atacar(self, objetivo: 'Personaje') -> int:
        """
        Decisión interna del enemigo: atacar o defenderse.
 
        Si se defiende, no hace daño pero recupera vida.
        Retorna 0 cuando se defiende.
        """
        if self.__decidir_accion() == 'defender':
            self.__defender()
            return 0    # No hizo daño - señal para la UI
        
        danho = self.get_poder_ataque()
        danho_real = objetivo.recibir_danho(danho)
        return danho_real
    
    def __decidir_accion(self) -> str:
        """
        Método privado: la lógica de decisión del Enemigo.
        """
        if random.random() <= self.__probabilidad_defensa:
            return 'defender'
        return 'atacar'
    
    def __defender(self) -> None:
        """
        Método privado: el enemigo se cura un poco en vez de atacar.
        """
        curacion = 10
        vida_nueva = self.get_vida_actual() + curacion

        # No curar mas alla del máximo
        if vida_nueva > self.get_vida_maxima():
            vida_nueva = self.get_vida_maxima()

        # Acceso controlado al atributo del padre via name mangling
        # Trade-off: rompemos un poco el encapsulamiento.
        self._set_vida_actual(vida_nueva)