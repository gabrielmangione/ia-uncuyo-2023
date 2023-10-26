import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("./tp5-busquedas-locales/resultados_nreinas_it.csv", header=None)
data.columns = ["Reinas","Algoritmo", "Solucionado", "Tiempo", "Pasos"]

#Cambiar el numero de cada algoritmo por 0 para Hill Climbing, 1 para Simulated Annealing y 2 para Genetico
data["Algoritmo"] = data["Algoritmo"].replace(0, "Hill Climbing")
data["Algoritmo"] = data["Algoritmo"].replace(1, "Simulated Annealing")
data["Algoritmo"] = data["Algoritmo"].replace(2, "Genetico")

#                                                                      

# Crea un gráfico de caja a partir de resultados_nreinas_it.csv para cada cantidad de reinas
for i in range(4, 12, 2):
    subset_data = data[data["Reinas"] == i]
    if not subset_data.empty:
        sns.boxplot(x="Algoritmo", y="Tiempo", data=subset_data[(subset_data["Solucionado"] == True)])
        plt.title("Tiempo de ejecución para " + str(i) + " reinas")
        plt.savefig("resultados_nreinas_it_" + str(i) + ".png")
        plt.show()


'''
#Crea un grafico de caja a partir de no-informadas-results.csv para cada fila donde encontrado==True
sns.boxplot(x="Algoritmo", y="Longitud del camino", data=data[data["Encontrado"] == True])
plt.title("Longitud del camino para cada algoritmo")
plt.savefig("no-informadas-results.png")
plt.show()

#Crea un grafico de caja a partir de no-informadas-results.csv para cada fila donde encontrado==True y Algoritmo!=DFS
sns.boxplot(x="Algoritmo", y="Longitud del camino", data=data[(data["Encontrado"] == True) & (data["Algoritmo"] != "DFS")])
plt.title("Longitud del camino para cada algoritmo")
plt.savefig("no-informadas-results-sin-dfs.png")
plt.show()

#Crea un grafico de barras a partir de no informada-result.cds contando la cantidad de veces que se encontro el camino en 30 iteraciones
#Cuenta la cantidad de veces que cada algoritmo encontro el camino en 30 iteraciones
data2=data[data["Encontrado"] == True].groupby(["Algoritmo"]).count()
data2=data2.reset_index()
data2=data2[["Algoritmo", "Iteracion"]]
data2.columns=["Algoritmo", "Cantidad de veces"]
data2=data2.sort_values(by="Cantidad de veces", ascending=False)

#Crea el grafico de barras
sns.barplot(x="Algoritmo", y="Cantidad de veces", data=data2)
plt.ylim(0,30)
plt.title("Cantidad de veces que se encontro el camino en 30 iteraciones")
plt.savefig("no-informadas-results-cantidad.png")
plt.show()'''