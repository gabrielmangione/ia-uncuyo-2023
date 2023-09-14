#Implementar un agente reflexivo simple para el entorno de la
#aspiradora del ejercicio anterior.
import random

class Agent_reflexive:
    def __init__(self, env):
        self.env = env

    def up(self):
        return 'Arriba'

    def down(self):
        return 'Abajo'

    def left(self):
        return 'Izquierda'

    def right(self):
        return 'Derecha'

    def suck(self):
        return 'Limpiar'

    def idle(self):
        return 'NoHacerNada'

    def perspective(self):
        return self.env.is_dirty()

    def think(self):
        if self.perspective():  # Si el agente percibe suciedad
            return self.suck()  # Aspira
        else:
            # Si no hay suciedad, el agente se mueve de manera aleatoria
            possible_actions = [self.up(), self.down(), self.left(), self.right(), self.idle()]
            return random.choice(possible_actions)
        
class Agent_random:
    
    def __init__(self, env):
        self.env = env

    def up(self):
        return 'Arriba'

    def down(self):
        return 'Abajo'

    def left(self):
        return 'Izquierda'

    def right(self):
        return 'Derecha'

    def suck(self):
        return 'Limpiar'

    def idle(self):
        return 'NoHacerNada'

    def perspective(self):
        return self.env.is_dirty()

    def think(self):
        possible_actions = [self.up(), self.down(), self.left(), self.right(), self.suck(), self.idle()]
        return random.choice(possible_actions)
