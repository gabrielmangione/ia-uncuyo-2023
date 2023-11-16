2.4
### 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

- #### (a) The sample size n is extremely large, and the number of predictors p is small.

 Se esperaría que sea mejor.Un enfoque más flexible se ajustará más a los datos y con un tamaño de muestra grande se obtendría un ajuste mejor que un enfoque inflexible.

- #### (b) The number of predictors p is extremely large, and the number
of observations n is small.

Se esperaria que sea peor. Un metodo flexible puede overfitear en un numero pequeño de observaciones.

- #### (c) The relationship between the predictors and response is highly non-linear.

Se esperaria que sea mejor. Con más grados de libertad, un modelo flexible obtendría un ajuste mejor.

- #### (d) The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.
 
Se esperaría que sea peor. Los métodos flexibles se ajustan al ruido en los términos de error y aumentan la varianza.

### 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.
- #### (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.

Se trata de un problema de regresión en donde nos interesa inferir el salario del CEO basada en las características de la empresa.
n - 500 empresas en EE. UU.
p - beneficio, número de empleados, industria

- #### (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

Se trata de un problema de clasificacion en donde nos interesa predecir el exito o fracaso de un nuevo producto.
n - 20 productos similares lanzados anteriormente
p - precio cobrado, presupuesto de marketing, precio de la competencia, etc

- #### (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the  % change in the US market, the % change in the British market, and the % change in the German market.

Se trata de un problema de regresión donde se busca predecir la salida cuantitativa del % de cambio.
n - 52 semanas de datos semanales de 2012
p - % de cambio en el mercado estadounidense, % de cambio en el mercado británico, % de cambio en el mercado alemán

## 5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

Las ventajas de un enfoque altamente flexible para regresión o clasificación incluyen lograr un mejor ajuste para modelos no lineales y reducir el sesgo. Las desventajas son la necesidad de estimar un mayor número de parámetros, el riesgo de overfiting y aumentar la varianza.

Preferiríamos un enfoque más flexible cuando estamos interesados en la predicción y no en la interpretabilidad de los resultados. Mientras que preferiríamos uno menos flexible cuando estamos interesados en la inferencia y la interpretabilidad de los resultados.

### 6."Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a nonparametric approach)? What are its disadvantages?

Un enfoque paramétrico simplifica el problema de estimar f al reducirlo a la estimación de un conjunto de parámetros, ya que asume una forma para f. Por otro lado, un enfoque no paramétrico no asume una forma funcional para f y, por lo tanto, requiere un número muy grande de observaciones para estimar f con precisión.

Las ventajas de un enfoque paramétrico para regresión o clasificación son la simplificación de la modelización de f a unos pocos parámetros y que no se requieren tantas observaciones en comparación con un enfoque no paramétrico. Y sus desventajas son el riesgo de estimar incorrectamente f si la forma de f asumida es incorrecta o de sobreajustar las observaciones si se utilizan modelos más flexibles.

### 7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.
| Obs. | X1 | X2 | X3   | Y    |
|------|----|----|------|------|
| 1    | 0  | 3  | 0    | Rojo |
| 2    | 2  | 0  | 0    | Rojo |
| 3    | 0  | 1  | 3    | Rojo |
| 4    | 0  | 1  | 2    | Verde|
| 5    | -1 | 0  | 1    | Verde|
| 6    | 1  | 1  | 1    | Rojo |

Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.

- (a) Compute the Euclidean distance between each observation and
the test point, X1 = X2 = X3 = 0

d((0,0,0), 1) = 3

d((0,0,0), 2) = 2

d((0,0,0), 3) = 3.16

d((0,0,0), 4) = 2.23

d((0,0,0), 5) = 1.41

d((0,0,0), 6) = 1.73

- (b) What is our prediction with K = 1? Why? 

La prediccion sería verde ya que la observacion 5 sería la mas cercana para K=1.

- (c) What is our prediction with K = 3? Why?

La prediccion seria rojo ya que las observaciones 2, 5 y 6 serían las mas cercanas para K = 3, en donde 2 es rojo, 5 es verde, y 6 es rojo.

- (d) If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the best value for K to be large or small? Why?

Esperaríamos que el mejor valor para K sea pequeño, ya que sería más flexible para una frontera de decisión no lineal.