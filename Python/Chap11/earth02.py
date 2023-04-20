import numpy as np

# 파이썬 리스트 선언
data = [1,2,3,4,5]
print(data)

# 파이썬 2차원 리스트(행렬) 선언
data2 = [[1,2], [3,4]]
print(data2)

# 파이썬 리스트를 numpy array로 변환
arr = np.array(data)
print(arr, type(arr))

arr = np.array([1,2,3,4,5])
print(arr, type(arr))

# 2차원 리스트를 np.array로 만듦
# 2차원 numpy array => 행렬
arr2 = np.array(data2)
print(arr2, type(arr2))


# 0부터 9까지 숫자를 자동으로 생성한 numpy array
arr3 = np.array(list(range(10)))
print(arr3, type(arr3))

# 10 부터 99까지 숫자를 자동으로 생성한 numpy array 생성하시오.
arr4 = np.arange(10,100)
print(arr4, type(arr4))

# reshaping array
#3 * 3 행렬을 생성하시오.
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(x)


#reshape()을 이용하여 생성
y = np.arange(1,10).reshape(3, 3)
print(y)


z = np.arange(6)
print(z)

z = np.arange(6).reshape(6, 1)
print(z)


# 배열의 연산
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1 + arr2)

# concatenate() : 배열들을 합쳐주는 함수
arr3 = np.concatenate([arr1,arr2])
print(arr3)


arr4 = np.concatenate([arr1,arr2], axis=0)
print(arr4)

#유니버셜(Unuversal) 함수 : 데이터의 원소별로 연산을 수행해주는 함수
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)

#리스트로 더하기 연산
L1 = [1,2,3]
L2 = [4,5,6]
print(L1 + L2)

# broadcast 함수 : 서로 크기가 다른 numpy array 연산할때,
# 자동으로 연산을  전파(broadcast) 해주는 기능- 행렬곱 연산 할때 편리함
arr1 = np.array([1,2,3])
arr2 = np.array([[-1,-1,-1],
                [-1,-1,-1]])
print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2)

# indexing
# numpy array의 indexing과 python list의 indexing은 같음
arr1 = np.arange(10)
print(arr1[0])
#마지막원소
print(arr1[-1])
#앞에서 부터 원소 3개 slicing
print(arr1[:3])

# Numpy Math 함수
# (표준정규분포에서) random sampling을 한 원소를 생성

math1 = np.random.randn(5,3)
print(math1)

# 정대값 씌우기
print(np.abs(math1))

# 제곱근 구하기
print(np.square(math1))
