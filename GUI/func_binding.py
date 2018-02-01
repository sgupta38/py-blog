from tkinter import *
root = Tk()


## Technique 1
## Here, we are binding the function "printName" with the button. So whenevr, button is clicked, "printName" function will b executed.
##
##  Notice the parameter 'command' is used for function binding
#def printName():
#    print("Winter is coming..!!!!")
#button = Button(root, text="Click Me", command=printName)
#button.pack()


## Technique 2
## Here, we are binding the function "printName" with the button, based on some event such as 'mouseclick'
##
##  Notice the parameter 'command' is used for function binding
def printName(event):
    print("Winter is coming..!!!!")

button = Button(root, text="Click Me")
button.bind("<Button-1>", printName)   # Takes two parameter, 1st is mousebutton number, 2nd is 'function name' to call
button.pack()

root.mainloop()
