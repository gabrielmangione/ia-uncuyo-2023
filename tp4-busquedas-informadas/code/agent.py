#Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo (si es posible).

import numpy as np
import math

class Agent:
    def __init__(self,env):
        self.env = env
        posX, posY = self.env.get_pos()
        objetiveX, objetiveY = self.env.get_objetive()
        self.pos= (posX,posY)
        self.objetive = (objetiveX,objetiveY)

    def think(self):
        open_list = [([self.pos], 0)]  # Cada elemento de open_list es una tupla con el camino y el costo total.
        closed_set = set()

        while open_list:
            open_list.sort(key=lambda x: x[1])  # Ordenar la lista por el costo total.
            current_path, current_cost = open_list.pop(0)
            current_node = current_path[-1]

            if current_node == self.objetive:
                #self.env.draw_path(current_path)
                return len(current_path), True

            if current_node in closed_set:
                continue

            closed_set.add(current_node)

            for neighbor in self.env.get_neighbours(current_node[0], current_node[1]):
                if neighbor not in closed_set:
                    new_path = current_path + [neighbor]
                    new_cost = current_cost + 1  # Puedes ajustar esto dependiendo de tus costos reales.

                    open_list.append((new_path, new_cost))
        return 0, False

    def h(self, x, y):
        return math.sqrt((x - self.objetive[0]) ** 2 + (y - self.objetive[1]) ** 2)