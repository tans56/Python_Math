from tkinter import *
root = Tk()

entry = Entry(root, fg="black", bg="yellow", width=20)
entry.pack()

def process():
    label["text"] = entry.get() + "가 입력됨"

button = Button(root, text="클릭하세요!", command=process)
button.pack()
label = Label(root, text="아무 값도 입력 안됨")
label.pack()

root.mainloop()