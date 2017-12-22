"""
    Какие доли составляли пассажиры первого, второго, третьего класса?
"""

import pandas as pd

def percentage(perc, whole):
    return (perc * 100) / whole


def get_nubmer_of_pclass(pclass, data=None):

    pclassratio = data.value_counts()

    if pclass == 1:
        return pclassratio[1]
    elif pclass == 2:
        return pclassratio[2]
    else:
        return pclassratio[3]


data = pd.read_csv('train.csv', index_col='PassengerId')
first = get_nubmer_of_pclass(1, data['Pclass'])
second = get_nubmer_of_pclass(2, data['Pclass'])
third = get_nubmer_of_pclass(3, data['Pclass'])

total = first + second + third
print('Первый класс: ', int(round(percentage(first, total))), '% \nВторой класс: ', int(round(percentage(second, total))), '% \nТретий класс: ', int(round(percentage(third, total))), '%')