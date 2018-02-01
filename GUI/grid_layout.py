from tkinter import *
root = Tk()

label_1 = Label(root, text="Username")
label_2 = Label(root, text="password")

# For input from user we use 'Entry'
entry_1 = Entry(root)
entry_2 = Entry(root)


label_1.grid(row=0, sticky=E) # bydefault column=0, sticky is used for right/left alignment. [E=East, N=North, W=West, S=South]
label_2.grid(row=1, sticky=E) # bydefault column=0

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

## To keep the following widget in middle we cant use row and column combination, what we gona use is 'columnspan' which merges no of columns specified and keeps the
## widget at middle
checkbox = Checkbutton(root, text="Keep me logged in")
checkbox.grid(columnspan=2)

button = Button(text="login")
button.grid(columnspan=2)

root.mainloop()
