### Arbol de decisión: 

- outlook
    - rainy
        -  windy
            - False -> True
            - True -> False
    - sunny
        - humidity
            - normal -> True
            - high -> False
  - overcast -> True

### Resultados sobre tennis.csv

| outlook  | temp | humidity | windy | classification | prediction |
|----------|------|----------|-------|-----------------|------------|
| sunny    | hot  | high     | False | False           | False      |
| sunny    | hot  | high     | True  | False           | False      |
| overcast | hot  | high     | False | True            | True       |
| rainy    | mild | high     | False | True            | True       |
| rainy    | cool | normal   | False | True            | True       |
| rainy    | cool | normal   | True  | False           | False      |
| overcast | cool | normal   | True  | True            | True       |
| sunny    | mild | high     | False | False           | False      |
| sunny    | cool | normal   | False | True            | True       |
| rainy    | mild | normal   | False | True            | True       |
| sunny    | mild | normal   | True  | True            | True       |
| overcast | mild | high     | True  | True            | True       |
| overcast | hot  | normal   | False | True            | True       |
| rainy    | mild | high     | True  | False           | False      |

Por la precision de las predicciones podemos pensar que el arbol está overfiteando.

### Estrategias para arboles de decision para datos de tipo real

Cuando nos enfrentamos a atributos continuos o de valor entero en un árbol de decisión, la gestión de un conjunto infinito de posibles valores resulta ser un problema. En lugar de generar infinitas ramas, se adopta una estrategia más efectiva centrada en encontrar puntos de división optimos. Este enfoque busca identificar el pundo que particiona los datos de manera más efectiva, contribuyendo así a la toma de decisiones precisa del modelo. Para llevar a cabo esta tarea de manera eficiente, se utilizan diversos criterios que evalúan la calidad de un punto de división en función de cómo afecta la homogeneidad de las muestras en los nodos resultantes. Algunos de los criterios comúnmente empleados son la impureza de Gini (mide la probabilidad de clasificar incorrectamente una muestra elegida al azar) y la ganancia de información (evalúa la reducción en la entropía de un conjunto de datos después de realizar una división) 