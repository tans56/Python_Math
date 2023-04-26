import pandas as pd          #pandas 모듈 호출
import numpy as np           #numpy 모듈 호출

from pandas import Series, DataFrame


list_data = [1,2,3,4,5]
list_name = ["a","b","c","d","e"]
example_obj = Series(data= list_data, index=list_name)
print(example_obj)

print(example_obj.index)
print(example_obj.values)
print(type(example_obj.values))
print(example_obj.dtype)

example_obj.name = "number"
example_obj.index.name = "id"
print(example_obj)

#시리즈 객체 생성
dic_data = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5}
example_obj = Series(dic_data, dtype= np.float32, name= "example_data")
print(example_obj)


data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
df_data = pd.read_csv(data_url, sep='\s+', header=None) #csv 데이터 로드
df = pd.DataFrame(df_data)
print(df)