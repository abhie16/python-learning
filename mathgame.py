from tkinter import *
import random

count = 0
def windowC():

    def click():
        if a + b == int(ans.get()):
            lab = Label(MathGameWindow, text="correct")
            lab.grid(columns=1, row=4)

            if count<5:
                windowC()
                count +=1
        else:
            lab = Label(MathGameWindow, text="incorrect")
            lab.grid(columns=1, row=4)

    MathGameWindow = Tk()

    MathGameWindow.geometry("500x500")
    MathGameWindow.title("Math Game")

    a = int(random.random() * 100)
    b = int(random.random() * 100)
    que = str(a) + " + " + str(b) + " = "
    lab = Label(MathGameWindow, text=que)
    lab.grid(columns=1, row=1)
    ans = Entry(MathGameWindow, width=20)
    ans.grid(columns=3, row=2)

    btn = Button(MathGameWindow, text='Log In', command=click)
    btn.grid(column=1, row=3)
    MathGameWindow.mainloop()


for i in range(0, 1):
    windowC()
