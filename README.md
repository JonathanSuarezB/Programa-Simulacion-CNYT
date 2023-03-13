# Programa-Simulacion-CNYT
Retos de programación del capítulo 3 del libro "Quantum computing for computer scientists" de Noson S. Yanofsky y Mirco A. Mannucci.

### Instalación 🔧

_Para la instalación y ejecución del entorno de desarrollo se necesita una consola que maneje codigo Python 3_

_Para ello se pueden descargar los siguientes programas_

```
[Python Idle](https://www.python.org/downloads/) - IDLE de Python
[Pycharm](https://www.jetbrains.com/es-es/pycharm/) - IDE de Python
```

_Después, se necesita instalado numpy y matlibraryplot para el procesamiento de algunas funciones, para finalizar, se pueden ejecutar los archivos del repositorio llamando a la función e ingresando los datos._

## Funcionalidad ⚙️

_El programa cuenta con 4 funciones que realizan las siguientes operaciones relacionadas al mundo clásico y cuántico:
## 1.Los experimentos de la canicas con coeficiente booleanos
## 2.Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
## 3.Experimento de las múltiples rendijas cuántico.
## 4.Función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados.


 
## Ejemplo:

    def deterministic_system(matrix,state,clicks):
    "Funcion para determinar un sistema dada una matriz Booleana, estado inicial y clicks transcurridos"
    new_state = state
    array = []
    for i in range (0,clicks):
        new_state = np.dot(matrix,new_state)
    return np.array(new_state).tolist()

```
La función de un sistema determinista: cuenta con tres parametros(a, b, c), una matriz, un estado y cantidad de clicks
```

### Las pruebas se pueden encontrar en el archivo **pruebas_simulacion.py** ⌨️

## Autores ✒️

* **Jonathan Yesid Suarez Bernal** - *Trabajo y documentación* 
