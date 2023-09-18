#Implementar un agente reflexivo simple para el entorno de la
#aspiradora del ejercicio anterior.

class Agent:
    def __init__(self,env):
        self.env = env
        self.score = 0
        self.life = 1000
        self.moves = ["left","down","right"]
        self.foundHome = False

    def up(self):
        self.life -=1 
        return self.env.refreshPos("up")
    
    def down(self):
        self.life -=1 
        return self.env.refreshPos("down")
    
    def left(self):
        self.life -=1 
        return self.env.refreshPos("left")
    
    def right(self):
        self.life -=1 
        return self.env.refreshPos("right")
    
    def clean(self):
        self.life -=1 
        return self.env.cleanCell()
    
    def idle(self):
        self.life -=1 
        return True

    def get_performance(self):
        return self.score / (self.env.get_performance() + self.score) 
    
    def perspective(self,env):
        return env.is_dirty()
    
    def think(self):
        
        if self.env.is_dirty():
            self.clean()
            self.score += 1

        elif not (self.foundHome):
            if self.env.accept_action("up"):
                self.up()
            elif self.env.accept_action("left"):
                self.left()
            else:
                self.foundHome = True
                return False
            
        else:
            next_move=self.moves.pop()
            if next_move == "left":
                if self.env.accept_action("left"):
                    self.left()
                    self.moves.append(next_move)
                else:
                    self.moves.insert(0,next_move)
                    return False
            elif next_move == "down":
                
                self.moves.insert(0,next_move)
                if self.env.accept_action("down"):
                    self.down()
                else:
                    self.foundHome = False
                
            elif next_move == "right":
                if self.env.accept_action("right"):
                    self.right()
                    self.moves.append(next_move)
                else:
                    self.moves.insert(0,next_move)
                    return False
        return True





