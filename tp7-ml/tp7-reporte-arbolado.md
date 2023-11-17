### Proceso de preprocesamiento:

Se realizo oversampling sobre el conjunto de entrenamiento para equilibrar las clases.

### Resultados obtenidos sobre el conjunto de validación

| id | inclinacion_peligrosa |
|----|------------------------|
| 1  | 0.11596883            |
| 2  | 0.11596883            |
| 4  | 0.04522631            |
| 6  | 0.04522631            |
| 9  | 0.23271617            |
| 13 | 0.10574773            |
| 14 | 0.23271617            |
| 17 | 0.23271617            |
| 23 | 0.04522631            |
| 28 | 0.23271617            |

### Resultados obtenidos en Kaggle

El resultado obtenido en la prueba publica de kaggle fue 0.74112

### Descripción detallada del algoritmo propuesto

Se utiliza el algoritmo de random forest con una formula que considera altura y especie. Luego se crean 200 arboles y se evalua utilizando el data test.
