#Evaluar el desempeño del agente reflexivo frente al desempeño del agente aleatorio
#Medida de desempeño y unidades de tiempo consumidas
#Entornos 2x2 4x4 8x8 16x16 32x32 64x64 128x128
#Porcentaje de suciedad en el ambiente 0.1,0.2,0.4,0.8
#Repetir 10 veces cada combinacion
#elaborar una tabla con los resultados en termino de la medida del rendimiento

import enviroment, agent, numpy as np
#Test the agent on enviromets of size 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128 with dirt rates of 0.1, 0.2, 0.4, 0.8 and repeat 10 times each combination
#The agent will be tested against a random agent
def run_test():
    #Test the agent on enviroments of size 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128 with dirt rates of 0.1, 0.2, 0.4, 0.8 and repeat 10 times each combination
    #The agent will be tested against a random agent
    sizes = [2,4,8,16,32,64,128]
    dirt_rates = [0.1,0.2,0.4,0.8]
    data = []
    repetitions = 10
    for size in sizes:
        for dirt_rate in dirt_rates:
            reflex_agent_performance = 0
            random_agent_performance = 0
            reflex_agent_life = 0
            random_agent_life = 0
            for i in range(0,repetitions):
                #Create the enviroment
                env1 = enviroment.Enviroment(size,size,np.random.randint(0,size-1),np.random.randint(0,size-1),dirt_rate)
                #Make a copy of the enviroment to test the random agent in the same enviroment
                env2 = enviroment.Enviroment(size,size,env1.agent_posX,env1.agent_posY,dirt_rate)
                #Create the agents
                reflex_agent = agent.Agent(env1)
                random_agent = agent.AgentR(env2)
                #Run the agents
                run_agents(reflex_agent,random_agent,env1,env2)
                #Print the results
                print("Enviroment size: ", size, "x", size, " Dirt rate: ", dirt_rate, " Repetition: ", i+1)
                print("Reflex agent performance: ", reflex_agent.get_performance())
                print("Random agent performance: ", random_agent.get_performance())
                
                reflex_agent_performance += reflex_agent.get_performance()
                random_agent_performance += random_agent.get_performance()
                reflex_agent_life += reflex_agent.life
                random_agent_life += random_agent.life 
                print("")
            #calculate the mean of the results
            reflex_agent_performance = reflex_agent_performance / repetitions
            random_agent_performance = random_agent_performance / repetitions
            reflex_time = round(1000 - (reflex_agent_life / repetitions))
            random_time = round(1000 - (random_agent_life / repetitions))

            #Save the results
            data.append([size,dirt_rate,reflex_agent_performance,random_agent_performance,reflex_time,random_time])
    #Save the results in a csv file
    np.savetxt("results.csv", data, delimiter=",", fmt='%s')

#Run the agents on the enviroment
def run_agents(reflex_agent,random_agent,env1,env2):
    #Run the agents on the enviroment while they have life
    while reflex_agent.life > 0 and env1.get_dirtness() > 0:
        #Run the reflex agent
        flag = False
        while not flag:
            flag = reflex_agent.think()
    
    while random_agent.life > 0 and env2.get_dirtness() > 0:
        #Run the random agent
        flag = False
        while not flag:
            flag = random_agent.think()
            
#Run the test
run_test()

