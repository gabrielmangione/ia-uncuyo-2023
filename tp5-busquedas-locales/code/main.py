#Inteligencia artificial 
#Trabajo practico 5
#Busquedas locales
import random
import math
import numpy as np
import bisect
import time

def inicializar_estado(n):
    """Genera un estado inicial aleatorio."""
    estado = list(range(n))
    random.shuffle(estado)
    return estado

def evaluar_estado(estado):
    n = len(estado)
    conflictos = 0
    for i in range(n):
        for j in range(i+1,n):   
            if abs(i - j) == abs(estado[i] - estado[j]):
                conflictos += 1
    return conflictos

def print_tablero(estado):
    n = len(estado)
    for i in range(n):
        print(" ---" * n)
        for j in range(n):
            if estado[i] == j:
                print("| Q ", end="")
            else:
                print("|   ", end="")
        print("|")
    print(" ---" * n)

#------------------------------------------------------------------------------
### Hill climbing

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

def hill_climbing_n_queens(estado_inicial, max_iter=1000):
    
    estado_actual = estado_inicial
    valor_actual = evaluar_estado(estado_actual)

    for i in range(max_iter):
        vecinos = generar_vecinos(estado_actual)
        mejor_vecino = min(vecinos, key=evaluar_estado)
        valor_mejor_vecino = evaluar_estado(mejor_vecino)
        
        if valor_mejor_vecino <= valor_actual:
            estado_actual = mejor_vecino
            valor_actual = valor_mejor_vecino

            if valor_actual == 0:
                return True, i, estado_actual
        else: return False, i, estado_actual

    return False, max_iter,estado_actual

#------------------------------------------------------------------------------
### Temple simulado

def generar_vecino(estado):
    """Genera un estado vecino al intercambiar dos reinas aleatorias."""
    n = len(estado)
    vecino = estado[:]
    i, j = random.sample(range(n), 2)
    vecino[i], vecino[j] = vecino[j], vecino[i]
    return vecino

def temple_simulado_n_queens(estado_inicial, max_iter=1000, temperatura_inicial=1.0, enfriamiento=0.99):
    estado_actual = estado_inicial
    valor_actual = evaluar_estado(estado_actual)
    mejor_solucion = estado_actual
    mejor_valor = valor_actual

    for i in range(max_iter):
        vecino = generar_vecino(estado_actual)
        valor_vecino = evaluar_estado(vecino)

        if valor_vecino == 0:
            return True, i, vecino

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

    return evaluar_estado(mejor_solucion)==0,max_iter,mejor_solucion

#------------------------------------------------------------------------------
### Algoritmo genetico

'''C)  Implementar un algoritmo genético para resolver el problema del punto A.  
Ademas de la implementación en código del mismo, se deberán incluir detalles respecto a
1. Definición de los individuos de la población
2. Estrategia de selección
3. Estrategia de reemplazo
4. Operadores.'''

'''
Definición de los Individuos de la Población:
El individuo de la población se define como una permutación de los números del 0 al N-1, donde cada 
número indica la fila en la que se coloca una reina en la columna correspondiente.
'''
def generar_poblacion_inicial(n, tam_poblacion):
    poblacion = []
    for i in range(tam_poblacion):
        solucion = list(range(n))
        random.shuffle(solucion)
        poblacion.append(solucion)
    return poblacion

def evaluar_aptitud(solucion):
    n = len(solucion)
    amenazas = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(solucion[i]-solucion[j]) == j-i or solucion[i] == solucion[j]:
                amenazas += 1
    return 1 / (amenazas + 1)

'''
Estrategia de Selección:
Se eligen dos padres de la población actual, con una probabilidad de seleccion tal que los 
individuos con menos conflictos tienen una mayor probabilidad de ser seleccionados como padres.'''
def seleccionar_padres(poblacion):
    aptitudes = [evaluar_aptitud(solucion) for solucion in poblacion]
    total_aptitudes = sum(aptitudes)
    ruleta = [sum(aptitudes[:i+1]) / total_aptitudes for i in range(len(poblacion))]
    padre1_idx = bisect.bisect_left(ruleta, random.random())
    padre2_idx = bisect.bisect_left(ruleta, random.random())
    return poblacion[padre1_idx], poblacion[padre2_idx]

'''
Estrategia de Reemplazo:
En cada generación, la población anterior se reemplaza completamente por una nueva población de descendientes.'''
def generar_nueva_poblacion(poblacion, prob_mutacion):
    """Genera una nueva población mediante la selección y reproducción de los padres."""
    nueva_poblacion = []
    while len(nueva_poblacion) < len(poblacion):
        padre1, padre2 = seleccionar_padres(poblacion)
        hijo = cruzar_padres(padre1, padre2)
        mutar_solucion(hijo, prob_mutacion)
        nueva_poblacion.append(hijo)
    return nueva_poblacion

'''
Operadores:

Cruce (Crossover): El cruce se realiza dividiendo a los padres en un punto de cruce aleatorio y combinando las mitades para crear dos descendientes. 

'''
def cruzar_padres(padre1, padre2):
    """Cruza dos padres para generar un hijo."""
    n = len(padre1)
    punto_cruce = random.randint(1, n-1)
    hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
    return hijo
'''
Mutación: La mutación se realiza cambiando aleatoriamente las posiciones de dos reinas en un individuo con una probabilidad dada. 
'''
def mutar_solucion(solucion, prob_mutacion):
    """Aplica una mutación aleatoria a una solución."""
    if random.random() < prob_mutacion:
        n = len(solucion)
        i, j = random.sample(range(n), 2)
        solucion[i], solucion[j] = solucion[j], solucion[i]

def algoritmo_genetico_n_queens(n, tam_poblacion=50, prob_mutacion=0.1, max_iter=1000):
    poblacion = generar_poblacion_inicial(n, tam_poblacion)
    for i in range(max_iter):
        aptitudes = [evaluar_aptitud(solucion) for solucion in poblacion]
        mejor_solucion = poblacion[np.argmax(aptitudes)]
        if evaluar_aptitud(mejor_solucion) == 1:
            return True, i, mejor_solucion

        poblacion = generar_nueva_poblacion(poblacion, prob_mutacion)

    return False, max_iter, mejor_solucion

#------------------------------------------------------------------------------
### main

#Ejecuta 30 veces cada algoritmo y guarda los datos en un csv con cantidad de reinas, metodo, tiempo, pasos, solucionado

import random
import math
import time

# Inicializa los encabezados del archivo CSV
with open('resultados_nreinas.csv', 'w') as f:
    f.write("Reinas,Algoritmo,Tiempo Promedio,Desviación Estándar de Tiempo,Pasos Promedio,Desviación Estándar de Pasos,Porcentaje Solucionado\n")

for n in range(4, 11, 2):
    print("Reinas: ", n)
    estado_inicial = inicializar_estado(n)
    solucionados = [0] * 3
    pasos_prom = [0] * 3
    times_prom = [0] * 3
    desviaciones_estandar_pasos = [0] * 3
    desviaciones_estandar_tiempo = [0] * 3

    f = open('resultados_nreinas_it.csv', 'a')
    f.write("Reinas,Algoritmo,Solucionado,Tiempo,Pasos\n")
    for method in range(3):
        times = []
        pasos = []
        for i in range(30):
            times.append(time.time())
            if method == 0:
                solucionado, paso, solucion = hill_climbing_n_queens(estado_inicial)
            elif method == 1:
                solucionado, paso, solucion = temple_simulado_n_queens(estado_inicial)
            else:
                solucionado, paso, solucion = algoritmo_genetico_n_queens(n)
            f.write(f"{n},{method},{solucionado},{time.time() - times[len(times) - 1]},{paso}\n")
            if solucionado:
                pasos_prom[method] += paso
                pasos.append(paso)
                solucionados[method] += 1
                times[len(times) - 1] = time.time() - times[len(times) - 1] 
            else: times.pop()          

        if solucionados[method] > 0: 
            times_prom[method] = sum(times) / len(times)
        else: times_prom[method] = 0
        # Calcular la desviacion estandar
        if solucionados[method] > 1:
            for i in range(solucionados[method]):
                desviaciones_estandar_pasos[method] += (pasos[i] - pasos_prom[method] / solucionados[method]) ** 2
                desviaciones_estandar_tiempo[method] += (times[i] - times_prom[method]) ** 2
            desviaciones_estandar_pasos[method] = math.sqrt(desviaciones_estandar_pasos[method] / (solucionados[method] - 1))
            desviaciones_estandar_tiempo[method] = math.sqrt(desviaciones_estandar_tiempo[method] / (solucionados[method] - 1))
        else:
            desviaciones_estandar_pasos[method] = 0
            desviaciones_estandar_tiempo[method] = 0
    f.close()
    for method, method_name in enumerate(["Hill Climbing", "Simulated Annealing", "Genetic Algorithm"]):
        print(f"{method_name}: Solucionados: {solucionados[method]}, Porcentaje solucionados: {100 * solucionados[method] / 30}%, Promedio de pasos en solucionados: {pasos_prom[method] / solucionados[method] if solucionados[method] != 0 else 'No hay promedio de solucionados'}, Desviación Estándar de Pasos: {desviaciones_estandar_pasos[method]}, Tiempo promedio de ejecución: {times_prom[method]} segundos, Desviación Estándar de Tiempo: {desviaciones_estandar_tiempo[method]} segundos")

    # Guarda los datos en el CSV
    with open('resultados_nreinas.csv', 'a') as f:
        for method in range(3):
            f.write(f"{n},{method},{times_prom[method]},{desviaciones_estandar_tiempo[method]},{pasos_prom[method]},{desviaciones_estandar_pasos[method]},{100 * solucionados[method] / 30}\n")
