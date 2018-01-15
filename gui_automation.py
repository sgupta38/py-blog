##
##  This example demonstrates how python can be used for real time mouse movement such as dragging, clicking etc and help in automating GUIs
##

import pyautogui

print(pyautogui.size())         # gives the screen resolution
print(pyautogui.position())     # gives the current position of mouse cur


pyautogui.moveTo(1, 1)  # This moves the mouse cursor to new position

## Above function moves cursor so quickly, to see it actually, you can specify duration like,
pyautogui.moveTo(250, 250, duration = 1.5)  # This moves the mouse cursor to new position in 1.5 sec
pyautogui.moveTo(1, 1, duration = 1.5)  # This moves the mouse cursor to new position


## This moves mouse cursor 'Relative to current location'
pyautogui.moveRel(200, 200, duration = 2.5)

pyautogui.moveRel(1000, 1000, duration = 1.5)
pyautogui.moveRel(0, -500, duration = 1.5)  # Note that 'negative Y' value moves the cursor to upper position

## You can also click on 'Menu'. But to get position of Menu, first take your cursor to 'Menu' and find its position using pyautogui.position()
##  Note those co-ordinates and use the same in pyautogui.click() function.

# In my case, I have already found it.
pyautogui.click(417, 47)

## You can also try using doubleClick(), and middleClick() functions . Just pass X,Y Co-ordinates


## IMP:  You should note that, these automating GUI programs are handy sometimes. Because 'Mouse Control' is in scripts hands.
##       It become so difficult to abort the script in between, as script is fully controlling mouse movements.
##       I have seen lot of people removing plug or shutting down system to obviate the script. :D :D
##       There is one trick, Python throws 'FailSafeException' and crashes the program when mouse position is moved to (0,0) location.
##       So, to abort the script, try to move mouse cursor to (0, 0) location asap. :D



### Protip:   To see the real time mouse movement X and Y co-ordinates, open your terminal /Command Prompt (windows)
##            And just type following lines of code which will give you real time mouse positions with RGB colors.
##             This is really useful, instead of explicitly calling position() function.
##
##
##               py -3.6
##              import pyautogui
##              pyautogui.displayMousePosition()
##
##
##
