from tkinter import *
root = Tk()

one = Label(root, text="One", bg="red", fg="white")
one.pack() # By default location of this widget remains same, either you resize your parent windows or not

two = Label(root, text="two", bg="green", fg="black")
two.pack(fill=X)        # This means our widget will change in x-direction according to parent window.

three = Label(root, text="three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)  # This means our widget will change in Y-direction according to parent window.

root.mainloop()
