"""Zona de UI Consola: se encarga exclusivamente de imprimir y leer inputs."""

class Consola:
    """
    Interfaz de usuario por consola.

    Es la única clase del proyecto con permiso de usar print() e input().
    Recibe datos de Game y los presenta al jugador de forma narrativa.
    """
    def __init__(self):
        pass

    def mostrar_bienvenida(self) -> None:
        print("\n")
        print("=" * 60)
        print("❄️❄️❄️❄️❄️       I C E F O R G E       ❄️❄️❄️❄️❄️")
        print("=" * 60)
        print()
        print("  🌨️  El mundo ha sido devorado por una tormenta")
        print("      de hielo perpetua. El silencio lo consume todo.")
        print()
        print("  🏔️  En medio del desierto blanco, un antiguo templo")
        print("      tallado en el interior de un glaciar aguarda...")
        print()
        print("  🔥  En lo más profundo, late una reliquia legendaria:")
        print("      EL CORAZÓN DE LA FORJA")
        print("      Un núcleo de calor infinito. La última esperanza.")
        print()
        print("  ⚔️  Solo un héroe puede atravesar al guardián")
        print("      y devolver el fuego al mundo.")
        print()
        print("=" * 60)

    def elegir_clase(self) -> str:
        """
        Muestra las opciones de héroe y espera la elección del jugador.
        Valida el input hasta recibir una opción válida.

        Returns:
            'guerrero' o 'mago' según la elección del jugador.
        """
        print("\n")
        print("-" * 60)
        print("  🧊  El templo resuena con una pregunta ancestral...")
        print("      ¿Quién desafiará al Guardián del Silencio?")
        print("-" * 60)
        print()
        print("  ⚔️  [1] EL ROMPEHIELOS")
        print("      Martillo térmico en mano. Daño constante y seguro.")
        print("      Motivación: salvar a su pueblo del frío letal.")
        print()
        print("  🔮  [2] EL MAGO DE LA CHISPA")
        print("      Último portador del fuego antiguo. Poder inestable.")
        print("      Motivación: preservar el conocimiento antes de que")
        print("      el frío lo consuma todo.")
        print()
        print("-" * 60)

        while True:
            eleccion = input("  👉  Elige tu héroe (1 o 2): ").strip()
            if eleccion == '1':
                print("\n  🔨  El Rompehielos avanza hacia el templo...\n")
                return 'guerrero'
            elif eleccion == '2':
                print("\n  ✨  El Mago de la Chispa enciende su llama...\n")
                return 'mago'
            else:
                print("  ⚠️  El templo no reconoce esa elección. Intenta de nuevo.")

    def mostrar_estado(self, jugador, enemigo) -> None:        
        """Imprime la vida actual y máxima de ambos combatientes."""
        print("\n")
        print("-" * 60)
        print("  📊  ESTADO DEL COMBATE")
        print("-" * 60)
        print(f"  🛡️  {jugador.get_nombre()}: {jugador.get_vida_actual()}/{jugador.get_vida_maxima()} ❤️")
        print(f"  🧊  {enemigo.get_nombre()}: {enemigo.get_vida_actual()}/{enemigo.get_vida_maxima()} ❤️")
        print("-" * 60)

    def narrar_ataque(self, atacante, defensor, danho) -> None:
        """
        Narra el resultado de un ataque según el daño recibido.
        Distingue entre: defensa del guardián, fallo del mago,
        golpe crítico y ataque normal.
        """
        nombre_atacante = atacante.get_nombre()
        nombre_defensor = defensor.get_nombre()

        if danho == 0 and nombre_atacante == 'El Guardián del Silencio':
            print(f"  🧊  {nombre_atacante} se cubre con una barrera de hielo.")
            print("      Se regenera en silencio... ❄️")
        elif danho == 0:
            print(f"  💨  {nombre_atacante} intenta atacar, pero el frío")
            print("      sofoca su chispa por completo. Sin daño. 🌑")
        elif danho > atacante.get_poder_ataque():
            print(f"  🌟  ¡{nombre_atacante} canaliza toda su energía!")
            print(f"      Una llamarada inmensa golpea a {nombre_defensor}")
            print(f"      ¡GOLPE CRÍTICO! {danho} puntos de daño. 🔥🔥🔥")
        else:
            print(f"  💥  {nombre_atacante} ataca a {nombre_defensor}")
            print(f"      infligiendo {danho} puntos de daño. 🔥")

    def mostrar_resultado(self, ganador) -> None:

        """Narra el desenlace de la partida según quién ganó."""
        nombre = ganador.get_nombre()
        print("\n")
        print("=" * 60)

        if nombre == 'El Guardián del Silencio':
            print("  💀  EL SILENCIO ETERNO PREVALECE  💀")
            print("=" * 60)
            print()
            print("  ❄️  El Guardián del Silencio ha cumplido su deber.")
            print("      El templo vuelve a sumirse en la calma gélida.")
            print()
            print("  🌑  El Corazón de la Forja permanece inalcanzable.")
            print("      El mundo se congela... para siempre.")
            print()
            print("  🪦  Tu héroe cae ante el peso del invierno eterno.")
        else:
            print("  🔥  ¡EL FUEGO RENACE!  🔥")
            print("=" * 60)
            print()
            print(f"  ⚔️  {nombre} ha derrotado al Guardián del Silencio.")
            print()
            print("  💎  El Corazón de la Forja late con fuerza.")
            print("      Su calor se expande por el templo...")
            print()
            print("  🌅  El hielo comienza a derretirse. El mundo respira")
            print("      de nuevo. La vida volverá a brotar.")
            print()
            print("  👑  ¡Victoria! El fuego ha sido restaurado.")

        print()
        print("=" * 60)
        print("        Gracias por jugar ICEFORGE ❄️🔥")
        print()
        print("        Creador: Carlos Meza")
        print("=" * 60)