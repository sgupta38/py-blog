from tkinter import *
root = Tk()

def printName():
    print("Winter is coming..!!!!")

##
## Here, we are binding the function "printName" with the button. So whenevr, button is clicked, "printName" function will b executed.
##
##  Notice the parameter 'command' is used for function binding
button = Button(root, text="Click Me", command=printName)
button.pack()

root.mainloop()
