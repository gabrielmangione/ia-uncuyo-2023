#Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo (si es posible).

import numpy as np
class Agent:
    def __init__(self,env,use):
        self.env = env
        self.score = 0
        self.life = 1000
        posX, posY = self.env.get_pos()
        objetiveX, objetiveY = self.env.get_objetive()
        self.pos= (posX,posY)
        self.objetive = (objetiveX,objetiveY)

        if use == "A":
            self.function = self.DFS
        elif use == "B":
            self.function = self.BFS
        elif use == "C":
            self.function = self.DFSLimited
        elif use == "D":
            self.function = self.US

    def get_performance(self):
        return 
    
    def think(self):
        path,bool = self.function()
        #self.env.draw_path(path)
        return len(path),bool
    
    def DFS(self):
        visited = set()
        stack = []
        stack.append((self.pos, []))  # Tupla que incluye la posición y un camino parcial
        while len(stack) > 0:
            node, current_path = stack.pop()
            if node not in visited:
                visited.add(node)
                current_path.append(node)  
                if node[0] == self.objetive[0] and node[1] == self.objetive[1]:
                    return current_path, True  
                if self.env.accept_action(node, "up"):
                    stack.append(((node[0] - 1, node[1]), current_path.copy()))
                if self.env.accept_action(node, "down"):
                    stack.append(((node[0] + 1, node[1]), current_path.copy()))
                if self.env.accept_action(node, "left"):
                    stack.append(((node[0], node[1] - 1), current_path.copy()))
                if self.env.accept_action(node, "right"):
                    stack.append(((node[0], node[1] + 1), current_path.copy()))
        return [], False

    def BFS(self):
        visited = set()
        queue = []
        queue.append((self.pos, []))  
        while len(queue) > 0:
            current_node, current_path = queue.pop(0)
            if current_node not in visited:
                visited.add(current_node)
                current_path.append(current_node) 
                if current_node[0] == self.objetive[0] and current_node[1] == self.objetive[1]:
                    return current_path, True
                if self.env.accept_action(current_node, "up"):
                    queue.append(((current_node[0] - 1, current_node[1]), current_path.copy()))
                if self.env.accept_action(current_node, "down"):
                    queue.append(((current_node[0] + 1, current_node[1]), current_path.copy()))
                if self.env.accept_action(current_node, "left"):
                    queue.append(((current_node[0], current_node[1] - 1), current_path.copy()))
                if self.env.accept_action(current_node, "right"):
                    queue.append(((current_node[0], current_node[1] + 1), current_path.copy()))
        return [], False

    def DFSLimited(self):
        max_depth = 300
        visited = set()
        stack = []
        stack.append((self.pos, []))  
        while len(stack) > 0:
            node, current_path = stack.pop()
            if node not in visited:
                visited.add(node)
                if len(current_path) <= max_depth:
                    current_path.append(node)  
                    if node[0] == self.objetive[0] and node[1] == self.objetive[1]:
                        return current_path ,True
                    if self.env.accept_action(node, "up"):
                        stack.append(((node[0] - 1, node[1]), current_path.copy()))
                    if self.env.accept_action(node, "down"):
                        stack.append(((node[0] + 1, node[1]), current_path.copy()))
                    if self.env.accept_action(node, "left"):
                        stack.append(((node[0], node[1] - 1), current_path.copy()))
                    if self.env.accept_action(node, "right"):
                        stack.append(((node[0], node[1] + 1), current_path.copy()))
        return [],False
    
    def US(self):
        visited = set()
        queue = []
        queue.append((self.pos, []))
        while len(queue) > 0:
            current_node, current_path = queue.pop(0)
            if current_node not in visited:
                visited.add(current_node)
                current_path.append(current_node)
                if current_node[0] == self.objetive[0] and current_node[1] == self.objetive[1]:
                    return current_path,True
                if self.env.accept_action(current_node, "up"):
                    queue.append(((current_node[0] - 1, current_node[1]), current_path.copy()))
                if self.env.accept_action(current_node, "down"):
                    queue.append(((current_node[0] + 1, current_node[1]), current_path.copy()))
                if self.env.accept_action(current_node, "left"):
                    queue.append(((current_node[0], current_node[1] - 1), current_path.copy()))
                if self.env.accept_action(current_node, "right"):
                    queue.append(((current_node[0], current_node[1] + 1), current_path.copy()))
            queue.sort(key=lambda x: len(x[1]))  # Ordena la cola por el tamaño del camino parcial
        return [], False
