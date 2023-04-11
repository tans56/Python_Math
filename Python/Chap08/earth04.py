'''
    리스트로 그래프 그리기
        - 리스트를 10개의 난수로 채우고
          이 데이터를 그래프로 시각화하시오.

          random.randint(a, b)
'''
import random
import matplotlib.pyplot as plt

rnum = []

for i in range(10):
    rnum.append(random.randint(1, 10))
    plt.plot(rnum)
    plt.ylabel('som random numbers')

plt.show()