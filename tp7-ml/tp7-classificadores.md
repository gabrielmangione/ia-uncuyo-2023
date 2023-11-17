### Matriz de confusion para clasificador aleatorio

|          | Actual Positive | Actual Negative |
|----------|-----------------|-----------------|
| **Predicted Positive** | 344 (TP)        | 2816 (FP)       |
| **Predicted Negative** | 352 (FN)        | 2870 (TN)       |

### Matriz de confusion para clasificador por clase mayoritario

|          | Actual Positive | Actual Negative |
|----------|-----------------|-----------------|
| **Predicted Positive** | 0 (TP)          | 0 (FP)          |
| **Predicted Negative** | 696 (FN)        | 5686 (TN)       |


### Comparacion 

| Classifier | Accuracy   | Precision  | Sensitivity | Specificity |
|------------|------------|------------|-------------|-------------|
| Random     | 0.5036039  | 0.1088608  | 0.4942529   | 0.5047485   |
| Majority   | 0.8909433  | NaN        | 0.0000000   | 1.0000000   |
