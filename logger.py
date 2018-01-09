##
## This covers the basic 'logging' in python. Using 'Factorial' program for demonstrating logger.
##
## Note: Never use Print() for logging, becos its hard to remove it when you are done.

import logging

#  use basicConfig(): Following line of code needs to be set up if you want to use 'logging'

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

## To save the logs to file instead of console, inititalise 'filename' parameter at the beginning.
## The five log levels are:  .DEBUG, .INFO, .WARNING, .ERROR, .CRITICAL
##

logging.basicConfig(filename='mylogger.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

## To disable logging related to .info,
##   example:  logging.disable(logging.INFO)
##
##
##  Note that parameter has to be spelled in 'CAPITAL' otherwise, it will throw error.
logging.disable(logging.DEBUG)      ## This will disable all the 'debug' log messages. i.e, it wont be printed.

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.critical('i is %s, total is %s' % (i, total))

    logging.debug('Return Value is %s' % (total))
    return total

print(factorial(5))
logging.debug('End of program')
