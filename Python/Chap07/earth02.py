# *args : 매개변수 개수가 정해져 있지 않은 경우
def args_func(*args):
    for i, v in enumerate(args):
        print('{}'.format(i),v, end=' ')
args_func('earth')
print()
args_func('earth', 'moon')
print()
args_func('earth', 'moon', 'sun')

print('-'*30)

# 위치 인수
def calc(x,y):
    return x - y
print(calc(10,20))
print(calc(20,10))

# 키워드 인수
print(calc(y=10, x=20))
print(calc(y=20, x=10))
print('-'*30)

# 중첩 함수
def nested_func(num):
    def func_in(num):
        print(num)

    print("중첩 함수")
    func_in(num + 100)

#func_in() 호출 불가
nested_func(1)

# 함수의 Hint
def tot_length(word: str, num: int) -> int:
    return len(word) * num

print("hint func :", tot_length("Heavy Snow Falls In Seoul", 10))
print('-'*30)

'''
    BMI 계산 공식 함수 
'''
# def BMI(): 매개변수 키, 몸무게
# def result_BMI(): BMI 결과 출력

def bmi(cm, kg):
    result = kg/(cm*cm)
    return result

def result_bmi(result):
    if result<18.5:
        print("당신은 저체중입니다.")
    elif result>=18.5 and result<23:
        print("당신은 정상입니다.")
    elif result>=23 and result<25:
        print("당신은 과체중입니다.")
    elif result>=25 and result<30:
        print("당신은 중등도비만입니다.")

h = float(input("키를 입력하세요: "))
w = float(input("몸무게를 입력하세요: "))

result = bmi(h,w)
result_bmi(result)














