import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')
print('Коэффициент корреляции Пирсона между возрастом и параметром survived:')
examp = data[['Age', 'Survived']]
colleration = examp.corr(method='pearson')
print(colleration)

print('\nКоэффициент корреляции Пирсона между классом, в котором пассажир ехал, и параметром survived:')
examp = data[['Pclass', 'Survived']]
colleration = examp.corr(method='pearson')
print(colleration)

print('\nКоэффициент корреляции Пирсона между ценой проезда и параметром survived:')
examp = data[['Fare', 'Survived']]
colleration = examp.corr(method='pearson')
print(colleration)