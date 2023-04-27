import pandas as pd
import numpy as np
from pandas import Series, DataFrame


raw_data = {'first_name' : ['순신', '무식', '스텔론', '마이클', '관순'],
            'last_name' : ['이', '차', '실버스타', '잭슨', '유'],
            'age' : [42, 52, 35, 24, 30],
            'city' : ['서울', '북경', '마닐라', '워싱턴', '파리']}
df = pd.DataFrame(raw_data)

df = pd.DataFrame(raw_data, columns= ['first_name', 'last_name', 'age' , 'city'])
print(df,type(df))

print(DataFrame(raw_data, columns=['age', 'city']))

df = pd.read_excel("C:/Users/ezen/Desktop/Python_Math/Python/Chap11/excel-comp-data.xlsx")
print(df)
print(df.head(2).T)
print(df.tail(2))
print(df.info)
print(df.values)