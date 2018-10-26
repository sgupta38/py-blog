# Demo Writing logs to another file. Here, writing the program logs to 'hello.log' file.

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)                     # Main logging module

#creating a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)                       # Here, file will log only 'INFO' logs. To log debug, change it to logging.DEBUG

#creating a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

#add the handler to logger
logger.addHandler(handler)

def Add(a,b):
    logger.info('Add() entry')
    logger.debug('Input is :%s %s', a, b)
    c = a+b
    logger.debug('Output is: %s', c)
    logger.info('Add() exit')
    return c

def main():
    logger.info('Main() entry')
    a = 46
    b = 36
    res = Add(a,b)
    print('Result of addition is:', res)
    logger.info('Main() exit')

if __name__ == '__main__':
    main()
