import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
# 4번 문항
data = {
'horse power': [130, 250, 190, 300, 210, 220, 170],
'weight': [1900, 2600, 2200, 2900, 2400, 2300, 2100],
'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
}

df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E', 'F', 'G'], columns=['horse power', 'weight', 'efficiency'])
df.index.name = 'name'

print(df)

X = df[['horse power', 'weight']]
y = df['efficiency']

model = LinearRegression()
model.fit(X, y)

coefficients = model.coef_
intercept = model.intercept_
score = model.score(X, y)

print("계수:", coefficients)
print("절편:", intercept)
print("예측 점수:", score)


predicted_efficiency = model.predict(pd.DataFrame({'horse power': [280], 'weight': [2500]}))

print(f"280 마력 자동차의 예상 연비: {predicted_efficiency[0]:.1f} km/l")

# 5번 문항
plt.figure(figsize=(10,10))
sns.pairplot(data=df)
plt.show()

# 6번 문항
plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(), annot=True)
plt.show()