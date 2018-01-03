##
##   Often while writing the code, we come across so many bugs and errors.
##  Here, I will cover the basic error and bug handling techniques.
##

##==========================================================================================================
##  EXCEPTION: Whenever any invalid code is executed, python raises an exception.
##
##  Raising your own exceptions: Means stop executing the code and mive the controle to 'except' statements.
##  Exception is raised using 'raise' staement.
##
##  Whenever exception is raised, it gives the information about 'traceback or callstack' which can further be used
##  for tracing bugs in code.
##  'traceback.format_exc()' --> is used to get and print the generated traceback. [need to import traceback]
##
##==========================================================================================================

## Example: printing the box of 'characters' based on user input
##
##


"""
***********
*         *
*         *
***********
"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string of length 1.')

    if (width < 2 ) or (height < 2):
        raise Exception('"Width" and "Heights" should be greater or equal to 2.')

    print(symbol * width)  #string replication


    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)  #string replication

#boxPrint('*', 30, 1 ) # Uncomment and run, you can see exception isgenerated
boxPrint('*', 30, 4 )


###
### Printing the traceback
import traceback

try:
    raise Exception("This is error message")
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info is written to error_log.txt')
