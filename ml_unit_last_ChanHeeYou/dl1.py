import numpy as np
import matplotlib.pyplot as plt

# Step 함수
def step(x):
    result = x > 0.00000001      # 작은 값과 비교하여 부동소수점 오차 방지
    result = result.astype(int)  # 불리언 값을 정수로 변환 (0 또는 1)
    result = result * 2 - 1     # 값들을 -1과 1로 매핑
    return result

# 크기가 (15, 3)인 figure 생성
plt.figure(figsize=(15, 3))

# Step 함수 그래프 그리기
x = np.arange(-6.0, 6.0, 0.00001)  # -6.0부터 6.0까지 작은 간격으로 x 값 생성
y = step(x)                       # Step 함수를 사용하여 y 값 계산
plt.subplot(1, 4, 1)              # 1x4 그리드에서 첫 번째 subplot 생성
plt.plot(x, y)                    # x와 y 값으로 그래프 그리기
plt.grid()                        # 그리드 표시
plt.title('Step')                 # subplot의 제목 설정

# Logistic Sigmoid 함수
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# Logistic Sigmoid 함수 그래프 그리기
x = np.arange(-6.0, 6.0, 0.00001)  # -6.0부터 6.0까지 작은 간격으로 x 값 생성
y = sigmoid(x)                    # Logistic Sigmoid 함수를 사용하여 y 값 계산
plt.subplot(1, 4, 2)              # 1x4 그리드에서 두 번째 subplot 생성
plt.plot(x, y)                    # x와 y 값으로 그래프 그리기
plt.grid()                        # 그리드 표시
plt.title('Logistic Sigmoid')      # subplot의 제목 설정

# Hyperbolic Tangent (tanh) 함수
x = np.linspace(-6.0, 6.0, 60)   # -6.0부터 6.0까지 60개의 균일한 간격으로 x 값 생성
y = np.tanh(x)                    # Hyperbolic Tangent 함수를 사용하여 y 값 계산
plt.subplot(1, 4, 3)              # 1x4 그리드에서 세 번째 subplot 생성
plt.plot(x, y)                    # x와 y 값으로 그래프 그리기
plt.grid()                        # 그리드 표시
plt.title('tanh(hyperbolic tangent)')  # subplot의 제목 설정

# ReLU와 Softplus 함수
def relu(x):
    return np.maximum(x, 0)

def softplus(x):
    return np.log(1 + np.exp(x))

# ReLU와 Softplus 함수 그래프 그리기
x = np.arange(-6.0, 6.0, 0.00001)  # -6.0부터 6.0까지 작은 간격으로 x 값 생성
y_relu = relu(x)                  # ReLU 함수를 사용하여 y 값 계산
y_softplus = softplus(x)          # Softplus 함수를 사용하여 y 값 계산
plt.subplot(1, 4, 4)              # 1x4 그리드에서 네 번째 subplot 생성
plt.plot(x, y_relu, label='ReLU')        # ReLU 함수 그래프 그리기
plt.plot(x, y_softplus, label='Softplus', color='red')  # Softplus 함수 그래프 그리기
plt.grid()                        # 그리드 표시
plt.title('ReLU and Softplus')    # subplot의 제목 설정
plt.legend()                      # 범례 추가

plt.tight_layout()  # 그래프 간격 조정

plt.show()