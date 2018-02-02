from tkinter import *

def doNothing():
    print("Doing nothinggggg....")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

# Adding file menu
FileMenu = Menu(menu)
menu.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="New", command=doNothing)
FileMenu.add_command(label="New", command=doNothing)
FileMenu.add_command(label="Setting", command=doNothing)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quit) # quit is in-built command which breaks the mainloop

# Adding Edit menu
EditMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Cut", command=doNothing)
EditMenu.add_command(label="Copy", command=doNothing)
EditMenu.add_separator()
EditMenu.add_command(label="Paste", command=doNothing)

# Adding toolbar
toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)

printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Adding status bar

statusbar = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W) # W--> WEST
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
