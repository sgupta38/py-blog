from tkinter import *

root = Tk()

def leftclick(event):
    print("Left")

def middleclick(event):
    print("Middle")

def rightclick(event):
    print("Right")

frame = Frame(root, width=500, height=500)
frame.bind("<Button-1>", leftclick)      #<Button-1> is left mouse button
frame.bind("<Button-2>", middleclick)   #<Button-2> is middle mouse button
frame.bind("<Button-3>", rightclick)    #<Button-3> is right mouse button
frame.pack()


root.mainloop()
