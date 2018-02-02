from tkinter import *

root = Tk()

## Loading the image of 'Mahabhrata' hero, Danshoor "Karna". :)
photo = PhotoImage(file="karna.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()
