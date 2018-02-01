from tkinter import *
root = Tk()

topFrame = Frame(root)
topFrame.pack()         # pack is necessary everytime without this, it wont be shown on window

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="green")
button3 = Button(topFrame, text="Button 3", fg="blue")
button4 = Button(bottomFrame, text="Button 4", fg="purple")


button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
