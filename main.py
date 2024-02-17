import pandas as pd
import numpy as np

array = np.array([5,8,12,6,1,-5])
print(array)


serie = pd.Series([5,8,12,6,1,-5], name = 'Numeros')
print(serie)

df = pd.DataFrame({'nome': ['Alice', 'bob', 'charlie'],
                   'Idade': [25,30,35],
                   'Cidade': ['A', 'B', 'C']})
print(df)

print('---------------------')
print(type(array))
print('-------------------')
print(type(serie))
print('-------------------')
print(type(df))

fraudes = pd.read_csv('Dados1 Cartoes.csv')
print(fraudes)
print(fraudes.shape)
print('-------------------')
print(fraudes.columns)
print('-------------------')
print(fraudes.Info())
print('-------------------')
print(fraudes.memory_usage())








