"""
    Посчитайте среднюю цену за билет и медиану.
    """

import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')
pot=pd.Series(data['Fare'])
print(pot.describe())
print('Медиана: ', pot.median())