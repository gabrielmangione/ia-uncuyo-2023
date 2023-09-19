#Implementar un agente reflexivo simple para el entorno de la
#aspiradora del ejercicio anterior.
import numpy as np
class Agent:
    def __init__(self,env):
        self.env = env
        self.score = 0
        self.life = 1000

    def up(self):
        self.env.refreshPos("up")
    
    def down(self):
        self.env.refreshPos("down")
    
    def left(self):
        self.env.refreshPos("left")
    
    def right(self):
        self.env.refreshPos("right")
    
    def clean(self):
        self.env.cleanCell()
    
    def idle(self):
        pass

    def get_performance(self):
        return self.score / (self.env.get_dirtness() + self.score) 
    
    def perspective(self,env):
        return env.is_dirty()
    
    def think(self):
        
        if self.perspective(self.env):
            self.clean()
            self.score += 1

        else: 
            moves = ["up","down","left","right"]
            next_move = np.random.choice(moves)
            if self.env.accept_action(next_move):
                if next_move == "up":
                    self.up()
                elif next_move == "down":
                    self.down()
                elif next_move == "left":
                    self.left()
                elif next_move == "right":
                    self.right()
                
            else: return False
        self.life -= 1
        return True

#Implementar un agente aleatorio para el entorno

class AgentR:
    def __init__(self,env):
        self.env = env
        self.score = 0
        self.life = 1000

    def up(self):
        self.env.refreshPos("up")
    
    def down(self):
        self.env.refreshPos("down")
    
    def left(self):
        self.env.refreshPos("left")
    
    def right(self): 
        self.env.refreshPos("right")
    
    def clean(self):
        self.env.cleanCell()
    
    def idle(self):
        pass

    def get_performance(self):
        return self.score / (self.env.get_dirtness() + self.score) 
    
    def perspective(self,env):
        return env.is_dirty()
    
    def think(self):
        moves = ["up","down","left","right","idle","clean"]
        next_move = np.random.choice(moves)
        if self.env.accept_action(next_move):
            if next_move == "up":
                self.up()
            elif next_move == "down":
                self.down()
            elif next_move == "left":
                self.left()
            elif next_move == "right":
                self.right()
            elif next_move == "idle":
                self.idle()
        else: 
            if next_move == "clean":    
                if self.perspective(self.env):
                    self.score += 1
                self.clean()
            else: return False
        self.life -= 1
        return True


