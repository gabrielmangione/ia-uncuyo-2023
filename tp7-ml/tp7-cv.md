## Codigo funciones create_folds y cross_validation

```{r}
library(caret)
library(rpart)

# Función para crear los folds
create_folds <- function(data, num_folds) {

  total_observations <- nrow(data)
  fold_size <- floor(total_observations / num_folds)
  fold_list <- list()

  for (i in 1:num_folds) {
    start_index <- (i - 1) * fold_size + 1
    end_index <- min(i * fold_size, total_observations)
    fold_indices <- start_index:end_index
    fold_list[[paste("Fold", i)]] <- fold_indices
  }
  
  return(fold_list)
}


# Función para validación cruzada y cálculo de métricas
cross_validation <- function(dataframe, k) {
  set.seed(123)  # Para reproducibilidad

  # Crear un modelo de control para la validación cruzada
  ctrl <- trainControl(method = "cv", number = k, classProbs = TRUE)

  # Definir la fórmula
  train_formula<-formula(inclinacion_peligrosa~ .)

  # Entrenar el modelo usando rpart con el control definido
  tree_model<-rpart(train_formula, data=dataframe, method='class')
  
  # Calcular las predicciones en la validación cruzada
  predictions <- predict(tree_model, newdata = dataframe, type = "class")
  
  # Calcular métricas
  confusion_matrix <- confusionMatrix(predictions, dataframe$inclinacion_peligrosa)
  
}

data <- read.csv("data/arbolado-mza-dataset.csv")

data$inclinacion_peligrosa <- as.factor(data$inclinacion_peligrosa)

# Realizar validación cruzada
result <- cross_validation(data, 5)

print(result)
```
### Resultados estadisticos 

Confusion Matrix and Statistics

                 Reference
    Prediction     0     1
             0 28201   376
             1   132  3203
                                          
                  Accuracy : 0.9841          
                    95% CI : (0.9826, 0.9854)
       No Information Rate : 0.8878          
       P-Value [Acc > NIR] : < 2.2e-16       
                                          
                     Kappa : 0.9176          
                                          
    Mcnemar's Test P-Value : < 2.2e-16       
                                          
               Sensitivity : 0.9953          
               Specificity : 0.8949          
            Pos Pred Value : 0.9868          
            Neg Pred Value : 0.9604          
                Prevalence : 0.8878          
            Detection Rate : 0.8837          
      Detection Prevalence : 0.8955          
         Balanced Accuracy : 0.9451          
                                          
          'Positive' Class : 0               
                            