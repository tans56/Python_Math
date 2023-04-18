'''
    원을 클래스로 구현하시오
    클래스 이름은 circle로 한다
        - 생성자
        - 반지름 (radius)
        - getArea()
        - getPrimeter()

    출력예시: (반지름이 10인 원의 면적과 원의 둘레를 출력하시오)
        원의 면적 :
        원의 둘레:
'''
import math


class Circle:
    def __init__(self, radius = 0):
        self.radius = radius


    def getArea(self):
        return math.pi * self.radius * self.radius

    def getPrimeter(self):
        return 2 * math.pi * self.radius


c = Circle(10)
print("원의 면적 : ", c.getArea())
print("원의 둘레 : ", c.getPrimeter())