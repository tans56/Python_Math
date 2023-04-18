'''
    class 클래스 이름:
        def __init__(self,...):
            pass
        def 메소드1(self,...):
            pass
        def 메소드2(self,...):
            pass
'''

class Counter:
    def __init__(self, initVar=0):    #생성자
        self.count = initVar          # count : 인스턴스 변수 생성

    def increament(self):       #메소드
        self.count += 1


a = Counter(0)
print("카운터의 값 = ", a.count)

a.increament()
print("카운터의 값 = ", a.count)

b = Counter(100)
print("카운터의 값 = ", b.count)

b.increament()
print("카운터의 값 = ", b.count)