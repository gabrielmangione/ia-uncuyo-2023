#Implementar un entorno con obstaculos para un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo (si es posible).
import numpy as np

from PIL import Image, ImageDraw

class Enviroment:
    def __init__(self, size,init_posX,inti_posY,target_posX,target_posY,rate):

        self.size = size
        self.agent_pos = (init_posX,inti_posY)
        self.target_pos = (target_posX,target_posY)

        #Create the grid with a percentage of obstacles equal to rate
        self.grid = np.random.choice([0,1], size=(size,size), p=[1-rate, rate])
        while self.get_obstacle_percentage() != rate:
            self.grid = np.random.choice([0,1], size=(size,size), p=[1-rate, rate])
        self.grid[init_posX][inti_posY] = 0
        self.grid[target_posX][target_posY] = 0
        self.image = self.get_grid_img()
        
    def get_grid_img(self):
        # Generate an image of the grid
        cell_size = 20  # Tamaño de cada celda
        line_color = "gray"  # Color de las líneas de separación

        img = Image.new('RGB', (self.size * cell_size, self.size * cell_size), color='white')
        draw = ImageDraw.Draw(img)

        # Dibujar líneas horizontales
        for i in range(self.size + 1):
            y = i * cell_size
            draw.line([(0, y), (self.size * cell_size, y)], fill=line_color)

        # Dibujar líneas verticales
        for j in range(self.size + 1):
            x = j * cell_size
            draw.line([(x, 0), (x, self.size * cell_size)], fill=line_color)

        # Dibujar celdas y posición del agente
        for i in range(self.size):
            for j in range(self.size):
                cell_x = i * cell_size
                cell_y = j * cell_size

                if self.grid[i][j] == 1:
                    draw.rectangle([(cell_x, cell_y), (cell_x + cell_size, cell_y + cell_size)], fill="black")
                elif i == self.agent_pos[0] and j == self.agent_pos[1]:
                    draw.rectangle([(cell_x, cell_y), (cell_x + cell_size, cell_y + cell_size)], fill="red")
                elif i== self.target_pos[0] and j == self.target_pos[1]:
                    draw.rectangle([(cell_x, cell_y), (cell_x + cell_size, cell_y + cell_size)], fill="green")

        return img

    def draw_path(self, path):
        path_image = self.image.copy()
        draw = ImageDraw.Draw(path_image)
        cell_size = 20  # Tamaño de cada celda
        for pos in path:
            cell_x = pos[0] * 20
            cell_y = pos[1] * 20
            draw.rectangle([(cell_x, cell_y), (cell_x + 20, cell_y + 20)], fill="blue")
        # Dibujar celdas y posición del agente
        draw.rectangle([(self.agent_pos[0] * cell_size, self.agent_pos[1] * cell_size), (self.agent_pos[0] * cell_size + cell_size, self.agent_pos[1] * cell_size + cell_size)], fill="red")
        draw.rectangle([(self.target_pos[0] * cell_size, self.target_pos[1] * cell_size), (self.target_pos[0] * cell_size + cell_size, self.target_pos[1] * cell_size + cell_size)], fill="green")

        path_image.show()

    #Check if the action is posible 
    def accept_action(self,agent_pos, action):
        if action == "up":
            return agent_pos[0]-1 >= 0 and self.grid[agent_pos[0]-1][agent_pos[1]] != 1
        elif action == "down":
            return agent_pos[0]+1 < self.size and self.grid[agent_pos[0]+1][agent_pos[1]] != 1
        elif action == "left":
            return agent_pos[1]-1 >= 0 and self.grid[agent_pos[0]][agent_pos[1]-1] != 1
        elif action == "right":
            return agent_pos[1]+1 < self.size and self.grid[agent_pos[0]][agent_pos[1]+1] != 1
        
    def get_obstacle_percentage(self):
        return np.sum(self.grid == 1)/(self.size*self.size)
    
    def get_pos(self):
        return self.agent_pos[0],self.agent_pos[1]
    
    def get_objetive(self):
        return self.target_pos[0],self.target_pos[1]
    
    def get_neighbors(self, posX,posY):
        neighbors = []
        if posX-1 >= 0 and self.grid[posX-1][posY] != 1:
            neighbors.append((posX-1,posY))
        if posX+1 < self.size and self.grid[posX+1][posY] != 1:
            neighbors.append((posX+1,posY))
        if posY-1 >= 0 and self.grid[posX][posY-1] != 1:
            neighbors.append((posX,posY-1))
        if posY+1 < self.size and self.grid[posX][posY+1] != 1:
            neighbors.append((posX,posY+1))
        return neighbors