'''
    움직이는 애니메이션 공 30개를 만드는 프로그램을 작성하시오.
    리스트를 생성하고 리스트에 객체를 저장하시오.
'''

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
        canvas.move(self.id, self.dx, self.dy)
        x0,y0,x1,y1 = canvas.coords(self.id)
        if y1 > canvas.winfo_height() or y0 < 0:  #원이 위쪽이나 아래쪽으로 벗어났으면
            self.dy = -self.dy                    #dy의 부호를 반전시킴
        if x1 > canvas.winfo_width() or x0 < 0:         #원이 왼쪽이나 오른쪽으로 벗어났으면
            self.dx = -self.dx                           # dy의 부호를 반전시킴


colors = ["red","orange","yellow","green","blue","violet", "indigo"]
ballList = []
for i in range(30):
    ballList.append(Ball(random.choice(colors), random.randint(1,60)))

while True:
    for i in range(30):
        ballList[i].move()
    window.update()
    time.sleep(0.01)



window.mainloop()