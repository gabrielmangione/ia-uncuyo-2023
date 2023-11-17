from csp import CSP
import time

N = [4,8,10,12,15]
aTimesB = []
aStatesB = []
aTimes = []
aStates = []

for n in N:
    #Backtracking
    csp = CSP(n)
    now = time.time()
    aStatesB.append(csp.backtracking())
    aTimesB.append(round(time.time() - now, 5))

    #Forward Checking
    csp = CSP(n)
    now = time.time()
    aStates.append(csp.forwardChecking())
    aTimes.append(round(time.time() - now, 5))

for i in range(len(N)):

    print(f"Backtracking {N[i]} reinas")
    print("Cantidad de estados: ",aStatesB[i])
    print("Tiempo de ejecución: ",aTimesB[i], "\n")

    print(f"Forward Checking {N[i]} reinas")
    print("Cantidad de estados: ",aStates[i])
    print("Tiempo de ejecución: ",aTimes[i], "\n")

#------------------------------------------------------------

import matplotlib.pyplot as plt

data_time = [aTimesB, aTimes]
data_states = [aStatesB, aStates]

labels = ['Backtracking', 'Forward Checking']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

ax1.boxplot(data_time, labels=labels)
ax2.boxplot(data_states, labels=labels)

ax1.set_title('Tiempo de ejecución de Backtracking y Forward Checking')
ax1.set_xlabel('Método')
ax1.set_ylabel('Tiempo de ejecución')

ax2.set_title('Estados de Backtracking y Forward Checking')
ax2.set_xlabel('Método')
ax2.set_ylabel('Estados')

plt.tight_layout()

plt.show()

#guardar
fig.savefig('./tp6-csp/figures/boxplot.png')