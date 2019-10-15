import tkinter
from tkinter import *
import tkinter.messagebox

def getSquareRoot ():  
    x1 = entry1.get()
    
    label1 = Label(main, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)
    
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

heading = Label(main ,bg="blue",font="Helvetica 20 bold italic", text='Welcome to Sinha bank')
heading.pack()

canvas1 = Canvas(main, width = 100, height = 100)
canvas1.pack()
entry1 = Entry(main) 
canvas1.create_window(100, 140, window=entry1)

    
button1 = Button(text='Get the Square Root', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

canvas1.coords(entry1 , new_xy)


main.mainloop()
