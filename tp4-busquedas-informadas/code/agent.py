#Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo (si es posible).

import numpy as np
class Agent:
    def __init__(self,env):
        self.env = env
        posX, posY = self.env.get_pos()
        objetiveX, objetiveY = self.env.get_objetive()
        self.pos= (posX,posY)
        self.objetive = (objetiveX,objetiveY)

    def think(self):
        path=[]
        bool=False
        #Implementa el algoritmo A* para encontrar el camino óptimo
        


        #self.env.draw_path(path)
        return len(path),bool
