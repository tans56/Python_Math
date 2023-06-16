'''
    matplotlib.pyplot
        - 데이터 분석 시각화 방법에서 가장 많이 사용되는 라이브러리
            - 파이썬 오픈소스 라이브러리 중 가장 널리 사용되는 시각화 라이브러리임
        - seaborn 같은 다른 다양한 시각화 라이브러리들은 matplotlib의 영향을 많이 받음
        - 2002년부터 만들어짐. MATLAB의 기능들을 파이썬으로 가져옴

    seaborn
        - statistical data visualization based on matplotlib
        - 2012년 만들어짐. matplotlib를 더 편하게 사용할 수 있도록 만든 라이브러리임
        -
'''
import matplotlib.pyplot as plt
import numpy as np

# # figure라는 도화지 위에 여러 컴포넌트를 얻어서 그래프를 완성함
# plt.Figure()
#
# # 라인을 그리는 것이 기본임. 리스트가 하나만 있는경우 y축임, x축은 인덱스가 들어감
# #plt.plot([1, 2, 4, 8, 16])
#
# # 리스트가 두개일 경우는 순서대로 x축, y축 리스트값임.
# plt.plot([1, 2, 3, 4, 5],[1, 2, 4, 8, 16])
# plt.show()

# 막대 그래프 그리기
# x = ["Americano", "CafeLatte", "CafeMocha", "Macchiato", "Affogato"]
# y = [1463, 301, 866, 905, 274]
# plt.figure(figsize=(8, 6))
# plt.grid(alpha=0.3, color="black", linewidth=0.5)
# plt.title("Coffe Sales in June", fontsize=20, loc="left")
# plt.xlabel("Menu", fontsize=15)
# plt.ylabel("Sales", fontsize=15)
# plt.bar(x, y, color="lightcoral", label="Sales")
# plt.plot(sorted([100, 200, 400, 800, 1600], reverse=True))
# plt.legend()
# #plt.ylim(0,2000)
# plt.yticks([num for num in range(0,2000,500)])          # y축 숫자 범위 조정
# plt.show()


# scatterplot()

# x = np.random.random(1000)       # 랜덤한 값 샘플링. 정규분포에 따름
# y = np.random.random(1000)
#
# plt.figure(figsize=(6, 6))
# plt.scatter(x, y ,color="orange", marker="*", s=10)
# plt.show()

'''
1. subplot() 이용해서 여러 개의 plot을 한번에 그림
2. subplot() 이용해서 여러 개의 plot을 하나의 figure에 출력할 수 있음
3. plt.subplot(nrows, ncols, index)
               로우의수, 컬럼의수, 인덱스
'''

plt.figure(figsize=(6, 8))
# plt.subplot(2, 1, 1)
# plt.subplot(2, 1, 2)
#
# plt.subplot(2, 2, 1)
# plt.subplot(2, 2, 2)
# plt.subplot(2, 2, 3)
# plt.subplot(2, 2, 4)
#
# plt.subplot(2, 1, 1)
# plt.subplot(2, 2, 3)
# plt.subplot(2, 2, 4)

# plt.subplot(1, 2, 1)
# plt.plot([0.1, 0.3, 0.5])           # x값 [0, 1, 2]에 대응하는 y값을 선 그래프 그림
#
# plt.subplot(3, 2, 2)
# plt.bar([1, 2, 3], [3, 2, 1])       # x값 [1, 2, 3]에 대응하는 y값 [3, 2, 1]을 막대그래프로 그림
#
# plt.subplot(3, 2, 4)
# plt.plot([4, 1, -3])
#
# plt.subplot(3, 2, 6)
# plt.scatter([1, 2, 3, 4, 5], [5, 3, 4, 2, 1])
#
# plt.show()
