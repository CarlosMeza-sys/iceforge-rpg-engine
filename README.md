# ❄️🔥 Iceforge — El Origen de las Clases

**Un juego de combate por turnos en consola, construido desde cero con Python puro y Programación Orientada a Objetos.**

> *El mundo ha sido devorado por una tormenta de hielo perpetua. En lo más profundo de un glaciar, late El Corazón de la Forja: la última esperanza para que la vida vuelva a brotar. Solo un héroe puede enfrentar al Guardián del Silencio y restaurar el fuego.*

---

## 📋 Tabla de Contenidos

- [Sobre el Proyecto](#sobre-el-proyecto)
- [Demo](#demo)
- [Arquitectura](#arquitectura)
- [Pilares POO Aplicados](#pilares-poo-aplicados)
- [Tecnologías](#tecnologías)
- [Cómo Ejecutarlo](#cómo-ejecutarlo)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Decisiones de Diseño](#decisiones-de-diseño)
- [Autor](#autor)

---

## Sobre el Proyecto

Iceforge es un juego de combate por turnos jugable desde la terminal. Fue diseñado como un ejercicio de **ingeniería de software**, no solo de programación: el objetivo no era que el código "funcione", sino que fuera **escalable, documentado y reproducible**.

El jugador elige entre dos clases de héroe, cada una con mecánicas de combate distintas, y se enfrenta a un enemigo controlado por el sistema con comportamiento autónomo (ataque o defensa).

### Características principales

- Sistema de combate por turnos con narrativa inmersiva en consola.
- Tres clases de personaje con comportamiento polimórfico diferenciado.
- Enemigo con IA básica que decide entre atacar y defenderse (curación).
- Arquitectura modular de 4 archivos con separación estricta de responsabilidades.
- Código completamente documentado con docstrings y type hints.

---

## Demo

```
❄️❄️❄️❄️❄️       I C E F O R G E       ❄️❄️❄️❄️❄️

  🧊  El templo resuena con una pregunta ancestral...
      ¿Quién desafiará al Guardián del Silencio?

  ⚔️  [1] EL ROMPEHIELOS
  🔮  [2] EL MAGO DE LA CHISPA

  📊  ESTADO DEL COMBATE
  🛡️  El Rompehielos: 85/100 ❤️
  🧊  El Guardián del Silencio: 70/100 ❤️

  💥  El Rompehielos ataca a El Guardián del Silencio
      infligiendo 15 puntos de daño. 🔥

  🌟  ¡El Mago de la Chispa canaliza toda su energía!
      ¡GOLPE CRÍTICO! 40 puntos de daño. 🔥🔥🔥

  🧊  El Guardián del Silencio se cubre con una barrera de hielo.
      Se regenera en silencio... ❄️
```

---

## Arquitectura

El proyecto sigue una arquitectura de **3 zonas lógicas** separadas en 4 archivos, donde cada módulo tiene una responsabilidad única:

```
main.py  →  Punto de entrada. Instancia el motor y ejecuta.
   │
   ▼
engine.py (Motor)  →  Coordina el flujo: inicio, turnos, resultado.
   │
   ├──→  entities.py (Dominio)  →  Clases, reglas y comportamiento.
   │
   └──→  ui.py (UI Consola)  →  Todo print() e input() vive aquí.
```

**Flujo de datos:**
- `engine.py` le pide datos a `ui.py` (elección del jugador) y le envía datos para mostrar (estado, ataques, resultado).
- `engine.py` crea y coordina las entidades de `entities.py`.
- `entities.py` y `ui.py` no se conocen entre sí — toda comunicación pasa por el motor.

---

## Pilares POO Aplicados

| Pilar | Implementación |
|---|---|
| **Abstracción** | `Personaje` es una clase abstracta (ABC) que define el contrato `atacar()`. No se puede instanciar directamente. |
| **Herencia** | `Guerrero`, `Mago` y `Enemigo` heredan de `Personaje`, reutilizando lógica compartida (`recibir_danho`, `esta_vivo`, getters). |
| **Polimorfismo** | Cada clase hija implementa `atacar()` con comportamiento distinto: daño fijo, aleatorio con crítico/fallo, o decisión ataque/defensa. |
| **Encapsulamiento** | Atributos privados (`__`) en todas las clases. Acceso solo por getters. Setter protegido (`_set_vida_actual`) para la jerarquía interna. |

---

## Tecnologías

- **Lenguaje:** Python 3.14
- **Módulos estándar:** `abc` (clases abstractas), `random` (mecánicas de probabilidad)
- **Dependencias externas:** Ninguna

---

## Cómo Ejecutarlo

### Prerrequisitos

- Python 3.10 o superior instalado en tu sistema.
- Una terminal con soporte para emojis (la mayoría de terminales modernas los soportan).

### Verificar versión de Python

```bash
python --version
```

Si muestra `Python 3.10.x` o superior, estás listo.

### Instalación y ejecución

```bash
# 1. Clona el repositorio
git clone https://github.com/CarlosMeza-sys/iceforge.git

# 2. Entra a la carpeta del proyecto
cd iceforge

# 3. Ejecuta el juego
python main.py
```

No requiere instalación de dependencias. El proyecto usa únicamente la librería estándar de Python.

### Cómo jugar

1. Al iniciar, verás la narrativa de bienvenida.
2. Elige tu héroe: **[1] El Rompehielos** (daño constante) o **[2] El Mago de la Chispa** (daño variable con críticos).
3. El combate es automático por turnos: atacas, el enemigo responde.
4. El juego termina cuando la vida de alguno de los dos llega a 0.

---

## Estructura del Proyecto

```
iceforge/
├── main.py          # Punto de entrada (5 líneas)
├── engine.py        # Motor del juego — clase Game
├── entities.py      # Dominio — Personaje, Guerrero, Mago, Enemigo
├── ui.py            # Interfaz de consola — clase Consola
└── README.md
```

| Archivo | Responsabilidad | Clases |
|---|---|---|
| `entities.py` | Reglas del juego y comportamiento de los personajes | `Personaje` (ABC), `Guerrero`, `Mago`, `Enemigo` |
| `engine.py` | Coordinación del flujo: inicio → turnos → resultado | `Game` |
| `ui.py` | Toda interacción con el usuario (print/input) | `Consola` |
| `main.py` | Instanciar y ejecutar | — |

---

## Decisiones de Diseño

**¿Por qué `recibir_danho()` retorna el daño real?**
Si un personaje tiene 5 de vida y recibe 20 de daño, el daño real fue 5. Retornar este valor permite que la UI narre con precisión sin tener que calcular nada por su cuenta.

**¿Por qué el Enemigo recibe stats variables pero el Guerrero y el Mago no?**
Solo hay un jugador (elige su clase), pero podrían existir múltiples enemigos con stats diferentes. Hacer el constructor flexible permite crear enemigos variados sin necesidad de crear subclases.

**¿Por qué existe `_set_vida_actual()` como método protegido?**
El Enemigo necesita modificar su vida cuando se cura. En vez de acceder directamente al atributo privado del padre (name mangling), se usa un setter protegido — visible para las clases hijas pero no para el exterior.

**¿Por qué la UI no importa nada de entities.py?**
La UI recibe objetos como parámetros y usa sus getters. No necesita saber si es un `Guerrero` o un `Mago` — solo llama `get_nombre()`, `get_vida_actual()`, etc. Esto desacopla las capas y permite cambiar la UI sin tocar el dominio.

---

## Autor

**Carlos Meza**

Proyecto desarrollado como parte del challenge *Iceforge: El Origen de las Clases* — Penguin Academy, The Huddle.