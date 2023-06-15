# 1. 데이터 및 라이브러리 불러오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

x = fetch_california_housing(as_frame=True)['data']
y = fetch_california_housing(as_frame=True)['target']
print(x)
print(y)
'''
    MedInc : 소득 (중앙값)
    HouseAge : 주택 나이 (중앙값)
    AveRooms : 전체 방 수
    AveBedrms : 전체 침실 수
    Population : 인구
    AveOccup : 가족 구성원 수
    Latitude : 위도
    Longitude : 경도
'''
data = pd.concat([x, y], axis=1)
print(data)

print(data.info())

#3. EDA
print(data.head())

# feature
# plt.figure(figsize=(8,8))
# sns.histplot(data=data, x="MedHouseVal")
# plt.show()

'''
    0.69 : median income이 MedHouseVal에 가장 큰 영향 요소임을 알 수 있음
    0.33 : 일반적으로 집의 방수가 많으면 수입이 많은 편임
'''
# plt.figure(figsize=(10,10))
# sns.heatmap(data.corr(), annot=True)
# plt.show()

print(data.loc[data.AveRooms > 100, :])         # 1914, 1979 row 제거
print(data.loc[data.AveOccup > 200, :])         # 3364, 13034, 16669, 19006 row 제거

# remove outlier
data = data.drop(index=[1914, 1917, 3364, 13034, 16669, 19006])
# remove (상관계수 중복되는 컬럼)
data.drop(columns=["AveBedrms", "Longitude"])
print(data)

#5. Training
# train data - test data split

# 학습을 위해 training / test dataset 나누기
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

print(x_train)

#Validation
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.25)
print(x_train.shape, x_val.shape, x_test.shape, y_train.shape, y_val.shape, y_test.shape)

# feature scaling
scaler = StandardScaler()           # 표준정규분포 형태로 스케일링해줌
x_train = scaler.fit_transform(x_train)       # 표준정규분표 형태로 스케일한 값으로 x_train 스케일링
x_val = scaler.fit_transform(x_val)           # 스케일링해줌
x_test = scaler.fit_transform(x_test)         # 스케일링해줌

print(x_train)

# training
reg = LinearRegression()                # 모델 불러옴
reg.fit(x_train, y_train)               # 학습
pred_train = reg.predict(x_train)       # 학습 데이터 예측값 구함
pred_val = reg.predict(x_val)           # 검증 데이터 예측값 구함

# 학습 데이터 오차값, 검증 데이터 오차값
mse_train = mean_squared_error(y_train, pred_train)
mse_val = mean_squared_error(y_val, pred_val)

print("Linear Regression\t, train=%.4f, val=%.4f" %(mse_train, mse_val))

# 6. Test
result = reg.predict(x_test)
print("-----------------Linear Regression")
print("MSE in training : %.4f" % mean_squared_error(y_test, result))