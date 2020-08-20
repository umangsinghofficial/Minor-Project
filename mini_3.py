from tkinter import*
def umang(event):
    print(f"You clicked on the Button at {event.x},{event.y}")
    
root=Tk()
root.title("Button")
root.geometry("800x500")

label_1 = Label(root,text="Check range of website in X-axis and -axis ",font="Times 20",pady=30 )
label_1.pack()
widget=Button(root,text="Click me please",font="Time 20",relief="solid",fg="white",bg="orange",padx=20,pady=30)
widget.pack()

widget.bind('<Button-1>',umang)
widget.bind('<Double-1>',quit)

root.mainloop()
