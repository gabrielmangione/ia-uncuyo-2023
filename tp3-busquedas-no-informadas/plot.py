#Crea un grafico de caja a partir de no-informadas-results.csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("./tp3-busquedas-no-informadas/no-informadas-results.csv", header=None)
data.columns = ["Algoritmo", "Iteracion", "Longitud del camino", "Encontrado"]

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
plt.show()
