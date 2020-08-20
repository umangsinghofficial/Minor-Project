
from tkinter import *

root=Tk()
root.geometry("800x500") #width X hight
root.title("Text in Format")
root.minsize(width="750",height="700")

label_1 = Label(root,text="Step 1",font="Times 10")
label_2 = Label(root,
                text="Hello World",
                bd=2,relief="solid",
                font="Times 32",
                padx=40,pady=10)
label_3 = Label(root,text="Step 2",font="Times 12")
label_4 = Label(root,text="Hello World",
                bd=3,relief="solid",
                font="Time 40",
                padx=70,pady=20)
label_5 = Label(root,text="Step 3",font="Times 14")
label_6 = Label(root,text="Hello World",
                bd=4,relief="solid",
                font="Time 48",
                padx=110,pady=30)
label_7 = Label(root,text="Step 4",font="Times 16")
label_8 = Label(root,text="Hello World",
                bd=5,relief="solid",
                font="Time 56",
                padx=150,pady=40)


label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
label_5.pack()
label_6.pack()
label_7.pack()
label_8.pack()


root.mainloop()
