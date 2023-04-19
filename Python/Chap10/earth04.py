'''
움직이는 애니메이션 공 프로그램을 작성하시오.
'''
import random
from tkinter import *
import time
import random

window = Tk()

canvas = Canvas(window, width=600, height=400)
canvas.pack()

class Ball():
    def __init__(self,color,size):
        self.id = canvas.create_oval(0, 0, size, size, fill=color)
        self.dy = random.randint(1,10)
        self.dx = random.randint(1, 10)

    def move(self):
        canvas.move(self.id, self.dy, self.dx)
        x0,y0,x1,y1 = canvas.coords(self.id)
        if y1 > canvas.winfo_height() or y0 < 0:  #원이 위쪽이나 아래쪽으로 벗어났으면
            self.dy = -self.dy                    #dy의 부호를 반전시킴
        if x1 > canvas.winfo_width() or x0 < 0:         #원이 왼쪽이나 오른쪽으로 벗어났으면
            self.dx = - self.dx                           # dy의 부호를 반전시킴


ball1 = Ball("blue", 60)
ball2 = Ball("green", 100)
ball3 = Ball("orange", 80)

while True:
    ball1.move()
    ball2.move()
    ball3.move()
    window.update()
    time.sleep(0.05)

window.mainloop()