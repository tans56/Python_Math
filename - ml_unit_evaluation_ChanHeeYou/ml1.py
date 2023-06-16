import pandas as pd
from sklearn.linear_model import LinearRegression

# 문항 1
data = {
    'horse power': [130, 250, 190, 300, 210, 220, 170],
    'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
}

df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E', 'F', 'G'], columns=['horse power', 'efficiency'])
df.index.name = 'name'

print(df)

# 문항 2
X = df[['horse power']]
y = df['efficiency']

model = LinearRegression()
model.fit(X, y)

coefficients = model.coef_
intercept = model.intercept_
score = model.score(X, y)

print("계수:", coefficients)
print("절편:", intercept)
print("예측 점수:", score)

# 문항 3
predicted_efficiency = model.predict(pd.DataFrame({'horse power': [280]}))

print(f"280 마력 자동차의 예상 연비: {predicted_efficiency[0]:.2f} km/l")



