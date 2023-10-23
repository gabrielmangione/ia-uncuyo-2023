#Inteligencia artificial 
#Trabajo practico 5
#Busquedas locales
import random
import math

def inicializar_estado(n):
    """Genera un estado inicial aleatorio."""
    estado = list(range(n))
    random.shuffle(estado)
    return estado

def evaluar_estado(estado):
    """Al definirse el tablero como una lista de n donde cada estado es la posición de la reina en la fila i 
    solo debemos evaluar la cantidad de amenazas que se tienen en las diagonales."""
    n = len(estado)
    conflictos = 0
    for i in range(n):
        for j in range(n):   
            if abs(i - j) == abs(estado[i] - estado[j]):
                conflictos += 1
    return conflictos

def generar_vecinos(estado):
    """Genera todos los estados vecinos al intercambiar las posiciones de dos reinas."""
    vecinos = []
    n = len(estado)
    for i in range(n):
        for j in range(i + 1, n):
            vecino = estado[:]
            vecino[i], vecino[j] = vecino[j], vecino[i]
            vecinos.append(vecino)
    return vecinos

def hill_climbing_n_queens(n, inicios_previos, max_iter=1000):
    estado_inicial = inicializar_estado(n)
    
    while estado_inicial in inicios_previos:
        estado_inicial = inicializar_estado(n)

    estado_actual = estado_inicial
    valor_actual = evaluar_estado(estado_actual)

    for _ in range(max_iter):
        vecinos = generar_vecinos(estado_actual)
        mejor_vecino = min(vecinos, key=evaluar_estado)
        valor_mejor_vecino = evaluar_estado(mejor_vecino)

        if valor_mejor_vecino >= valor_actual:
            return False, estado_inicial,estado_actual

        estado_actual = mejor_vecino
        valor_actual = valor_mejor_vecino

        if valor_actual == 0:
            return True, estado_inicial, estado_actual

    return False, estado_inicial,estado_actual

def generar_vecino(estado):
    """Genera un estado vecino al intercambiar dos reinas aleatorias."""
    n = len(estado)
    vecino = estado[:]
    i, j = random.sample(range(n), 2)
    vecino[i], vecino[j] = vecino[j], vecino[i]
    return vecino

def temple_simulado_n_queens(n, max_iter=10000, temperatura_inicial=1.0, enfriamiento=0.99):
    estado_actual = inicializar_estado(n)
    valor_actual = evaluar_estado(estado_actual)
    mejor_solucion = estado_actual
    mejor_valor = valor_actual

    for _ in range(max_iter):
        vecino = generar_vecino(estado_actual)
        valor_vecino = evaluar_estado(vecino)

        # Calcular la diferencia en la función de evaluación
        delta_valor = valor_vecino - valor_actual

        # Aceptar el vecino si mejora la solución o con una probabilidad de acuerdo a la temperatura
        if delta_valor < 0 or random.random() < math.exp(-delta_valor / temperatura_inicial):
            estado_actual = vecino
            valor_actual = valor_vecino

        # Actualizar la mejor solución encontrada
        if valor_actual < mejor_valor:
            mejor_solucion = estado_actual
            mejor_valor = valor_actual

        # Enfriar la temperatura
        temperatura_inicial *= enfriamiento

    return mejor_solucion

# Ejemplo de uso
n = 5  # Tamaño del tablero y cantidad de reinas

#Ejecutar 100 veces y mostrar los datos en formato
#  n, cantidad de iteraciones, cantidad de conflictos
inicios = []
for i in range(1000):
    encontrado , inicio, solucion = hill_climbing_n_queens(n,inicios)
    inicios = inicios + [inicio]
    print(n, i, encontrado, " ",evaluar_estado(solucion)," ",solucion) 

#Ejecutar 100 veces y mostrar los datos en formato 
#  n, cantidad de iteraciones, cantidad de conflictos
for i in range(1000):
    solucion = temple_simulado_n_queens(n)
    print(n, i, evaluar_estado(solucion)," ",solucion)