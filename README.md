# Minor-Project
We make a Minor project to store information in Button Format


from tkinter import *

root =Tk()
root.geometry("655x333")
root.minsize(width=700,height=300)
root.configure(bg="orange")

def categories():
    print("Categories is Male")
def name():
    print("Name is Umang Kumar")
def study():
    print("Pursuing Btech 3rd year in Computer Branch")
def phone():
    print("Phone No. is : 8130908412")

a_one = Label(root,text="Information store in Button format" ,font= "Times 20",
              bg="orange",padx=10,pady=20)
a_one.pack()

frame = Frame(root, borderwidth=4, relief=SOLID ,padx=20,pady=40 )
frame.pack()

frame.configure(bg="orange")
b1 = Button(frame, fg="Black",bg="yellow",text="Categories", command=categories)
b1.pack(side=LEFT, pady=23)

b2 = Button(frame, fg="Black",bg="green",text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="Black",bg="pink",text="Detail for Education",command=study)
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="Black",bg="red",text="Phone No.",command=phone)
b4.pack(side=LEFT, padx=23)

root.mainloop()
