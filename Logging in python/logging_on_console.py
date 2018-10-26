import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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

    
