#Implementar un simulador que determine la medida de rendimiento para el entorno del mundo de la aspiradora según las siguientes especificaciones:
# La medida de rendimiento premia con un punto al agente por cada recuadro que limpia (aspira) en un período de tiempo concreto,
# a lo largo de una «vida» de 1000 acciones. La «dimensión» de la grilla se conoce a priori pero la distribución de la suciedad y
# la localización inicial del agente no se conocen (aleatorio). Las cuadrículas se mantienen limpias y aspirando se limpia la cuadrícula
#en que se encuentra el agente Las acciones Izquierda, Derecha, Arriba, Abajo mueven al agente en dichas direcciones, excepto en el caso
#en que lo pueda llevar fuera de la grilla. Las acciones permitidas son: Arriba Abajo Izquierda Derecha Limpiar (aspirar) NoHacerNada
#El agente percibe su locación y si esta contiene suciedad

import numpy as np

class Enviroment:
    def __init__(self, sizeX,sizeY,init_posX,inti_posY,dirt_rate):

        self.sizeX = sizeX
        self.sizeY = sizeY
        self.agent_posX = init_posX
        self.agent_posY = inti_posY
        self.dirt_rate = dirt_rate
        
        #Create the grid with the given size and a probability of dirt in each cell 
        self.grid = np.random.choice([0, 1], size=(sizeX, sizeY), p=[1 - dirt_rate, dirt_rate])

        while self.get_dirtness() == 0:
            self.grid = np.random.choice([0, 1], size=(sizeX, sizeY), p=[1 - dirt_rate, dirt_rate])

    def print_grid(self):
    # Print the grid with the agent position
        print("Agent pos: ", self.agent_posX, self.agent_posY)
        for i in range(0,self.sizeX):
            for j in range(0,self.sizeY):
                if i == self.agent_posX and j == self.agent_posY:
                    print("A", end=" ")
                else:
                    print(self.grid[i][j], end=" ")
            print("")
        print("") 

    #Check if the action is posible 
    def accept_action(self, action):
        if action == "up":
            return self.agent_posX-1 >= 0
        elif action == "down":
            return self.agent_posX+1 < self.sizeX
        elif action == "left":
            return self.agent_posY-1 >= 0
        elif action == "right":
            return self.agent_posY+1 < self.sizeY
        elif action =="idle":
            return True
        else:
            return False
    
    def refreshPos(self, action):
        if action == "up":
            self.agent_posX -= 1
        elif action == "down":
            self.agent_posX += 1
        elif action == "left":
            self.agent_posY -= 1
        elif action == "right":
            self.agent_posY += 1
        else:
            return False
        return True

    def cleanCell(self):
        self.grid[self.agent_posX][self.agent_posY] = 0
        return True

    def is_dirty(self):
        return self.grid[self.agent_posX][self.agent_posY] == 1
    
    def get_dirtness(self):
        return np.sum(self.grid == 1)