from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import pandas as pd

def preprocess(df, ycol):
    """
    Written for pollution data; will drop null values and
    split into training and testing sets. Uses ycol
    as the target column.
    """

    df.dropna(inplace=True)
    X = pd.get_dummies(df.drop(columns=ycol))
    y = df[ycol].values.reshape(-1, 1)
    return train_test_split(X, y)

def r2_adj(x, y, model):
    """
    Calculates adjusted r-squared values given an X variable, 
    predicted y values, and the model used for the predictions.
    """
    r2 = model.score(x,y)
    n = x.shape[0]
    p = y.shape[1]
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)

def process(df, target):
    """
    Defines a series of steps that will preprocess data,
    split data, and train a model for predicting target
    using linear regression. It will return the trained model
    and print the mean squared error, r-squared, and adjusted
    r-squared scores.
    """
    
    steps = [("Scale", StandardScaler(with_mean=False)), 
             ("Linear Regression", LinearRegression())]
    pipeline = Pipeline(steps)
    X_train, X_test, y_train, y_test = preprocess(df, target)
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2_value = r2_score(y_test, y_pred)
    r2_adj_value = r2_adj(X_test, y_test, pipeline)
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2_value}")
    print(f"Adjusted R-squared: {r2_adj_value}")
    return "Done!"
