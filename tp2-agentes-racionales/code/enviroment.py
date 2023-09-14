#B) Implementar un simulador que determine la medida de rendimiento para el entorno del mundo de la aspiradora según las siguientes especificaciones:
# La medida de rendimiento premia con un punto al agente por cada recuadro que limpia (aspira) en un período de tiempo concreto,
# a lo largo de una «vida» de 1000 acciones. La «dimensión» de la grilla se conoce a priori pero la distribución de la suciedad y
# la localización inicial del agente no se conocen (aleatorio). Las cuadrículas se mantienen limpias y aspirando se limpia la cuadrícula
#en que se encuentra el agente Las acciones Izquierda, Derecha, Arriba, Abajo mueven al agente en dichas direcciones, excepto en el caso
#en que lo pueda llevar fuera de la grilla. Las acciones permitidas son: Arriba Abajo Izquierda Derecha Limpiar (aspirar) NoHacerNada
#El agente percibe su locación y si esta contiene suciedad

import random

class Environment:
    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.agent_posX = init_posX
        self.agent_posY = init_posY
        self.dirt_rate = dirt_rate
        self.grid = [[random.random() < dirt_rate for _ in range(sizeY)] for _ in range(sizeX)]

    def accept_action(self, action):
        if action == 'Izquierda' and self.agent_posY > 0:
            self.agent_posY -= 1
        elif action == 'Derecha' and self.agent_posY < self.sizeY - 1:
            self.agent_posY += 1
        elif action == 'Arriba' and self.agent_posX > 0:
            self.agent_posX -= 1
        elif action == 'Abajo' and self.agent_posX < self.sizeX - 1:
            self.agent_posX += 1
        elif action == 'Limpiar':
            self.clean()
        
    def is_dirty(self):
        return self.grid[self.agent_posX][self.agent_posY]

    def clean(self):
        if self.is_dirty():
            self.grid[self.agent_posX][self.agent_posY] = False

    def get_performance(self):
        return sum(row.count(False) for row in self.grid)  # Count clean cells

    def print_environment(self):
        for row in self.grid:
            print(' '.join(['D' if cell else 'L' for cell in row]))  # D for dirty, L for clean
