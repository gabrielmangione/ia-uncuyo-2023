import agent,enviroment,random,time

#Evaluar el desempeño del agente reflexivo frente al desempeño del agente aleatorio
#Medida de desempeño y unidades de tiempo consumidas
#Entornos 2x2 4x4 8x8 16x16 32x32 64x64 128x128
#Porcentaje de suciedad en el ambiente 0.1,0.2,0.4,0.8
#Repetir 10 veces cada combinacion
#elaborar una tabla con los resultados en termino de la medida del rendimiento

def run_simulation(env_size, dirt_rate, num_repeats):
    random.seed(0)  # Fijamos la semilla para reproducibilidad
    total_performance_random = 0
    total_performance_reflexive = 0
    total_time_random = 0
    total_time_reflexive = 0

    for _ in range(num_repeats):
        env = Environment(sizeX=env_size, sizeY=env_size, init_posX=random.randint(0, env_size-1),
                          init_posY=random.randint(0, env_size-1), dirt_rate=dirt_rate)
        agent_random = AgentRandom(env)
        agent_reflexive = AgentReflexive(env)

        start_time = time.time()
        while env.get_performance() < env_size * env_size:
            action = agent_random.think()
            env.accept_action(action)
        end_time = time.time()
        total_time_random += end_time - start_time
        total_performance_random += env.get_performance()

        env = Environment(sizeX=env_size, sizeY=env_size, init_posX=random.randint(0, env_size-1),
                          init_posY=random.randint(0, env_size-1), dirt_rate=dirt_rate)
        start_time = time.time()
        while env.get_performance() < env_size * env_size:
            action = agent_reflexive.think()
            env.accept_action(action)
        end_time = time.time()
        total_time_reflexive += end_time - start_time
        total_performance_reflexive += env.get_performance()

    avg_performance_random = total_performance_random / num_repeats
    avg_performance_reflexive = total_performance_reflexive / num_repeats
    avg_time_random = total_time_random / num_repeats
    avg_time_reflexive = total_time_reflexive / num_repeats

    return avg_performance_random, avg_time_random, avg_performance_reflexive, avg_time_reflexive

# Configuraciones de entorno y porcentaje de suciedad a evaluar
env_sizes = [2, 4, 8, 16, 32, 64, 128]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
num_repeats = 10

# Crear una tabla con los resultados
print("Entorno\tPorcentaje Suciedad\tAgente Aleatorio (Puntos)\tAgente Aleatorio (Tiempo)\tAgente Reflexivo (Puntos)\tAgente Reflexivo (Tiempo)")
for env_size in env_sizes:
    for dirt_rate in dirt_rates:
        avg_perf_random, avg_time_random, avg_perf_reflexive, avg_time_reflexive = run_simulation(env_size, dirt_rate, num_repeats)
        print(f"{env_size}x{env_size}\t{dirt_rate}\t{avg_perf_random:.2f}\t{avg_time_random:.2f}\t{avg_perf_reflexive:.2f}\t{avg_time_reflexive:.2f}")
