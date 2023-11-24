import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
print(len(mtcars))
print(mtcars)
print(mtcars.head(5))
print(mtcars.tail(3))
print(mtcars.info())
print(mtcars.describe())