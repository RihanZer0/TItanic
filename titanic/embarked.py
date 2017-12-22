"""
       Подсчитайте сколько пассажиров загрузилось на борт в различных портах?
       Приведите три числа через пробел.
   """

import pandas as pd

def get_nubmer_of_embarked(embarked, data=None):

    embarkedratio = data.value_counts()

    if embarked == 'C':
        return embarkedratio['C']
    elif embarked == 'Q':
        return embarkedratio['Q']
    else:
        return embarkedratio['S']


data = pd.read_csv('train.csv', index_col='PassengerId')
c = get_nubmer_of_embarked('C', data['Embarked'])
q = get_nubmer_of_embarked('Q', data['Embarked'])
s = get_nubmer_of_embarked('S', data['Embarked'])

print('Порт С: ', c, '\nПорт Q: ', q, '\nПорт S: ', s)