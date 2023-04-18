from tkinter import *           # tkinter 모듈을 포함

root = Tk()                     # 루트 윈도우를 생성
root.geometry("500x200")        # width x height, 단위는 픽셀
label1 = Label(root, text="안녕 파이썬 GUI")  # 레이블 위젯을 생성
label2 = Label(root, text="파이썬을 사랑합니다", bg="yellow", fg="blue", font=("궁서체", 32))

label1.pack()                    # 압축 배치 관리자를 이용하여 레이블 위젯을 윈도우에 배치
label2.pack()

root.mainloop()                 # 윈도우가 사용자 동작을 대기