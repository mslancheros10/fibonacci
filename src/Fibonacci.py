
import sys
from Tkinter import *
import tkMessageBox

def showFibonacci(textArea):
    mensaje = ""
    try:
        print entryWidget.get()
        iterations=int(textArea)
        counter = 1
        x1, x2 = 0,1
        while(counter<=iterations):
            mensaje = mensaje + str(x2) +" "
            x1,x2 = x2,x1+x2
            counter+=1
        tkMessageBox.showinfo("The result is...", mensaje)
    except ValueError:
        tkMessageBox.showerror("Error", "Not a number")




top = Tk()
top.title("Fibonacci series")
textFrame = Frame(top)

entryLabel = Label(textFrame)
entryLabel["text"] = "Insert the number of iterations:"
entryLabel.pack(side=LEFT)

entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)

textFrame.pack()

button = Button(top, text="Submit", command=lambda:showFibonacci(entryWidget.get()))
button.pack()

top.mainloop()





