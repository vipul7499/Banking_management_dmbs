from tkinter import *
main=Tk()
main.title('Sinha Bank')
main.geometry("1000x750+10+20")
main.configure(background='light green')


text=Label(main, text="Siddharth Sinha", fg='red', font=("Helvetica", 16))
text.place(x=40, y=80)

heading = Label(main ,bg="blue",font="Helvetica 20 bold italic", text='Welcome to Sinha bank')
heading.place(x=330, y=10)

#heading.pack()


#canvas1.coords(entry1 , new_xy)

canvas2 = Canvas(main, width = 300, height = 400)
canvas2.pack(side = LEFT , padx = 40)
entry2 = Entry(main) 
canvas2.create_window(100, 140, window=entry2)

canvas1 = Canvas(main, width = 500, height = 100)
canvas1.pack(side = TOP, pady = 175)
entry1 = Entry(main) 
canvas1.create_window(300, 300, window=entry1)




main.mainloop()
