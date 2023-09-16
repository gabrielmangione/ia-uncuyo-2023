#Implementar un simulador que determine la medida de rendimiento para el entorno del mundo de la aspiradora según las siguientes especificaciones:
# La medida de rendimiento premia con un punto al agente por cada recuadro que limpia (aspira) en un período de tiempo concreto,
# a lo largo de una «vida» de 1000 acciones. La «dimensión» de la grilla se conoce a priori pero la distribución de la suciedad y
# la localización inicial del agente no se conocen (aleatorio). Las cuadrículas se mantienen limpias y aspirando se limpia la cuadrícula
#en que se encuentra el agente Las acciones Izquierda, Derecha, Arriba, Abajo mueven al agente en dichas direcciones, excepto en el caso
#en que lo pueda llevar fuera de la grilla. Las acciones permitidas son: Arriba Abajo Izquierda Derecha Limpiar (aspirar) NoHacerNada
#El agente percibe su locación y si esta contiene suciedad