#Evaluar el desempeño del agente reflexivo frente al desempeño del agente aleatorio
#Medida de desempeño y unidades de tiempo consumidas
#Entornos 2x2 4x4 8x8 16x16 32x32 64x64 128x128
#Porcentaje de suciedad en el ambiente 0.1,0.2,0.4,0.8
#Repetir 10 veces cada combinacion
#elaborar una tabla con los resultados en termino de la medida del rendimiento

import enviroment, agent, numpy as np

def run_experiment(sizeX,sizeY,init_posX,inti_posY,dirt_rate):
    env = enviroment.Enviroment(sizeX,sizeY,init_posX,inti_posY,dirt_rate)
    ag = agent.Agent(env)
    while ag.life > 0:
        env.print_grid()
        flag = False 
        while flag != True:
            flag = ag.think()

    env.print_grid()
    return ag.get_performance()

print(run_experiment(5,5,4,4,0.5))