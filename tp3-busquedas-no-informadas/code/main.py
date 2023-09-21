import enviroment as env
import agent as ag
import numpy as np
import random 

size = 100
data = []

for i in range(30):
    enviroment = env.Enviroment(size,random.randint(0, size-1),random.randint(0, size-1),random.randint(0, size-1),random.randint(0, size-1),0.08)
    #Agente DFS
    agentDFS= ag.Agent(enviroment,"A")
    DFSresult, DFSFound = agentDFS.think()
    data.append(["DFS",i,DFSresult,DFSFound])

    #Agente BFS
    agentBFS= ag.Agent(enviroment,"B")
    BFSresult, BFSFound = agentBFS.think()
    data.append(["BFS",i,BFSresult,BFSFound])
    
    #Agente DLFS
    agentDFSL= ag.Agent(enviroment,"C")
    DFSLresult, DFSLFound = agentDFSL.think()
    data.append(["DLFS",i,DFSLresult,DFSLFound])
    
    #Agente UCS
    agentUS= ag.Agent(enviroment,"D")
    USresult, USFound = agentUS.think()
    data.append(["UCS",i,USresult,USFound])

#Crea un csv con los resultados
np.savetxt("./tp3-busquedas-no-informadas/no-informadas-results.csv", data, delimiter=",", fmt='%s')