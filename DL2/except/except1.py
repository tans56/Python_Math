(x,y) = (2,0)

try:
    z = x/y
except ZeroDivisionError:
    print("0으로 나누는 예외 발생")

try:
    z = x/y
except ZeroDivisionError as e:
    print(e)