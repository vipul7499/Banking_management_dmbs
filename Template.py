import tkinter
from tkinter import *
import tkinter.messagebox
def process(a):
    if(a == 1):
        print(1)
    if(a == 2):
        print(1)
    if(a == 3):
        print(1)
    if(a == 4):
        print(1)
    if(a == 5):
        print(1)

main = Tk()
main.geometry("1000x750")
main.configure(background='light green')
main.title('Banking Managment System')
w = Label(main ,bg="blue",font="Helvetica 20 bold italic", text='Welcome to Sinha bank')
w.pack() 
v = IntVar() 
Radiobutton(main, text='Add Video', variable=v, value=1).pack(anchor=W) 
Radiobutton(main, text='Train Newly Added Persons', variable=v, value=2).pack(anchor=W)
Radiobutton(main, text='Train All', variable=v, value=3).pack(anchor=W)
Radiobutton(main, text='Fine Tune', variable=v, value=4).pack(anchor=W)
Radiobutton(main, text='Recognize', variable=v, value=5).pack(anchor=W)
blackbutton = Button(main, text ='Submit', fg ='black' , command = lambda : process(v.get()))
blackbutton.pack()
main.mainloop()
