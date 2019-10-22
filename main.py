import tkinter
from tkinter import *
import tkinter.messagebox

def customerlogin ():
    password = entry2.get()
    username = entry1.get()
    print(username)
    print(password)
    
def bankerlogin():
    username = entry3.get()
    password = entry4.get()
    print(username)
    print(password)


main = Tk()
main.geometry("1000x750")
main.configure(background='light green')
main.title('Banking Managment System')

heading = Label(main ,bg="blue",font="Helvetica 20 bold italic", text='Welcome to Sinha bank')
heading.pack()



canvas1 = Canvas(main, width = 300, height = 400)
canvas1.pack(side = RIGHT , padx = 40)
#text = Label(canvas1,font="Helvetica 10 bold italic", text='k')

canvas1.create_text(100,40,fill="darkblue",font="Times 20 italic bold", text="Customer login")
canvas1.create_text(50,140,fill="black",font="Times 10 ", text="ID")
canvas1.create_text(50,190,fill="black",font="Times 10 ", text="PASS")
entry1 = Entry(main) 
canvas1.create_window(140, 140, window=entry1)
entry2 = Entry(main) 
canvas1.create_window(140, 190, window=entry2)

#text.pack()
    
button1 = Button(text='login', command=customerlogin)
canvas1.create_window(140, 220, window=button1)

#canvas1.coords(entry1 , new_xy)

canvas2 = Canvas(main, width = 300, height = 400)
canvas2.pack(side = LEFT , padx = 40)
canvas2.create_text(100,40,fill="darkblue",font="Times 20 italic bold", text="Banker login")
canvas2.create_text(50,140,fill="black",font="Times 10 ", text="ID")
canvas2.create_text(50,190,fill="black",font="Times 10 ", text="PASS")
entry3 = Entry(main) 
canvas2.create_window(140, 140, window=entry3)
entry4 = Entry(main) 
canvas2.create_window(140, 190, window=entry4)

#text.pack()
    
button2 = Button(text='login', command=bankerlogin)
canvas2.create_window(140, 220, window=button2)

main.mainloop()
