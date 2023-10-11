import enviroment as env
import agent as ag
import numpy as np
import random 

size = 100
data = []

for i in range(30):
    enviroment = env.Enviroment(size,random.randint(0, size-1),random.randint(0, size-1),random.randint(0, size-1),random.randint(0, size-1),0.08)
    agent_A_Start= ag.Agent(enviroment)
    a_Star_Result, a_Star_Found = agent_A_Start.think()
    data.append(["A*",i,a_Star_Result,a_Star_Found])

#Crea un csv con los resultados
np.savetxt("./tp4-busquedas-informadas/informadas-results.csv", data, delimiter=",", fmt='%s')
