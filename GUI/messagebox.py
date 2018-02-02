from tkinter import *
import tkinter.messagebox

root = Tk()

# Simple messagebox
# showinfo:
tkinter.messagebox.showinfo('Window Title', 'Winter is coming')


## askquestion:
## Following gives 'YES / NO' messagebox and takes answer from user.
## Based on this answer , we can do any action we want.
answer = tkinter.messagebox.askquestion('Poll', 'Do you love khaleesi?')
if answer == 'yes':
    print(" I love khaleesiiiii....!!! :D ")

root.mainloop()
