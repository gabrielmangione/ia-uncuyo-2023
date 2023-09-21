#Crea un grafico de caja a partir de no-informadas-results.csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("./tp3-busquedas-no-informadas/no-informadas-results.csv", header=None)
data.columns = ["Algoritmo", "Iteracion", "Longitud del camino", "Encontrado"]

#Crea un grafico de caja a partir de no-informadas-results.csv 
sns.boxplot(x="Algoritmo", y="Longitud del camino", data=data)
plt.title("Longitud del camino por algoritmo")
plt.savefig("./tp3-busquedas-no-informadas/boxplot.png")
plt.show()

