from tkinter import *
root = Tk()
def process():
    label["text"] = "버튼 클릭됨"

button = Button(root, text="클릭하세요!", command=process)
button.pack()

label = Label(root, text="버튼 클릭 안됨")
label.pack()
root.mainloop()


