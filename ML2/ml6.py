import tensorflow as tf

# 같은 크기를 가진 두개의 텐서에 대하여 사칙연산 가능
# 기본적으로 요소별 연산


a = tf.constant([
    [1,2],
    [3,4]
])

b = tf.constant([
    [5,6],
    [7,8]
])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 행렬 곱 (matrix
print(tf.matmul(a, b))