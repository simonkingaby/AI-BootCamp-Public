# Model Metrics
## Model: LinearRegression()
| Metric | Value |
| :--- | ---: |
|Mean Squared Error:|0.6101531982421875| 
|R-Squared:|0.25430914606294575| 
|Adjusted R-squared:|0.2161152242759259| 

## Model: KNeighborsRegressor(n_neighbors=9)
| Metric | Value |
| :--- | ---: |
|Mean Squared Error:|0.3584819387288523| 
|R-Squared:|0.5618859267117651| 
|Adjusted R-squared:|0.5394459375921238| 

## Model: RandomForestRegressor(n_estimators=128, random_state=1)
| Metric | Value |
| :--- | ---: |
|Mean Squared Error:|0.1137836597583912| 
|R-Squared:|0.8609407692137679| 
|Adjusted R-squared:|0.8538182232466682| 

## Model: ExtraTreesRegressor(n_estimators=128, random_state=1)
| Metric | Value |
| :--- | ---: |
|Mean Squared Error:|0.15337682653356483| 
|R-Squared:|0.8125524916013438| 
|Adjusted R-squared:|0.8029515216589737| 

## Model: AdaBoostRegressor(n_estimators=128, random_state=1)
| Metric | Value |
| :--- | ---: |
|Mean Squared Error:|0.5914961101889575| 
|R-Squared:|0.27711066535756335| 
|Adjusted R-squared:|0.24008462626612148| 

## Model: SVR(epsilon=0.2)
| Metric | Value |
| :--- | ---: |
|Mean Squared Error:|0.331153518056741| 
|R-Squared:|0.5952850032165627| 
|Adjusted R-squared:|0.5745556985032647| 

## Model: LogisticRegression(random_state=1)
| Metric | Value |
| :--- | ---: |
|Mean Squared Error:|0.25925925925925924| 
|R-Squared:|0.683149643425473| 
|Adjusted R-squared:|0.6669207227228753| 

## Model: SVC(kernel='poly', probability=True)
| Metric | Value |
| :--- | ---: |
|Training Accuracy:|0.9984567901234568| 
|Testing Accuracy:|0.9768518518518519| 
|Balanced Accuracy Score:|0.9514158576051781| 
|ROC AUC Score:|0.9989827480978596| 
```
Confusion Matrix:
 [[ 95   7   0   1]
 [  0  14   0   1]
 [  0   0 294   0]
 [  1   0   0  19]]
```
```
Classification Report:
               precision    recall  f1-score   support

           0       0.99      0.92      0.95       103
           1       0.67      0.93      0.78        15
           2       1.00      1.00      1.00       294
           3       0.90      0.95      0.93        20

    accuracy                           0.98       432
   macro avg       0.89      0.95      0.91       432
weighted avg       0.98      0.98      0.98       432

```

## Model: KNeighborsClassifier(n_neighbors=9)
| Metric | Value |
| :--- | ---: |
|Training Accuracy:|0.9598765432098766| 
|Testing Accuracy:|0.9189814814814815| 
|Balanced Accuracy Score:|0.6576860841423948| 
|ROC AUC Score:|N/A| 
```
Confusion Matrix:
 [[ 89   2  12   0]
 [ 10   4   0   1]
 [  0   0 294   0]
 [  9   1   0  10]]
```
```
Classification Report:
               precision    recall  f1-score   support

           0       0.82      0.86      0.84       103
           1       0.57      0.27      0.36        15
           2       0.96      1.00      0.98       294
           3       0.91      0.50      0.65        20

    accuracy                           0.92       432
   macro avg       0.82      0.66      0.71       432
weighted avg       0.91      0.92      0.91       432

```

## Model: DecisionTreeClassifier()
| Metric | Value |
| :--- | ---: |
|Training Accuracy:|1.0| 
|Testing Accuracy:|0.9722222222222222| 
|Balanced Accuracy Score:|0.927992701935143| 
|ROC AUC Score:|N/A| 
```
Confusion Matrix:
 [[ 96   4   0   3]
 [  0  14   0   1]
 [  1   0 293   0]
 [  1   2   0  17]]
```
```
Classification Report:
               precision    recall  f1-score   support

           0       0.98      0.93      0.96       103
           1       0.70      0.93      0.80        15
           2       1.00      1.00      1.00       294
           3       0.81      0.85      0.83        20

    accuracy                           0.97       432
   macro avg       0.87      0.93      0.90       432
weighted avg       0.98      0.97      0.97       432

```

## Model: RandomForestClassifier(n_estimators=128, random_state=1)
| Metric | Value |
| :--- | ---: |
|Training Accuracy:|1.0| 
|Testing Accuracy:|0.9606481481481481| 
|Balanced Accuracy Score:|0.8715614886731392| 
|ROC AUC Score:|N/A| 
```
Confusion Matrix:
 [[ 93   7   1   2]
 [  3  11   0   1]
 [  0   0 294   0]
 [  3   0   0  17]]
```
```
Classification Report:
               precision    recall  f1-score   support

           0       0.94      0.90      0.92       103
           1       0.61      0.73      0.67        15
           2       1.00      1.00      1.00       294
           3       0.85      0.85      0.85        20

    accuracy                           0.96       432
   macro avg       0.85      0.87      0.86       432
weighted avg       0.96      0.96      0.96       432

```

