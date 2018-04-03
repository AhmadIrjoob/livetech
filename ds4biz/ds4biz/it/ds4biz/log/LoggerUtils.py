'''
Created on Jan 20, 2017

@author: aledip
'''

import logging
import os
from it.ds4biz.config.Config import Config


def getLogger(module, logname=False,path=None):
    
    if path==None:
        log_path=Config().getLogOutput()
    else:
        absPath = os.path.abspath(__file__ + "/../../../../")
        log_path = absPath + '/log'

    if not os.path.exists(log_path):
        os.makedirs(log_path)
    if logname == False:
        fname = log_path + '/' + 'log.txt'
    else:
        fname = log_path + '/' + logname

    with open(fname, 'a+'):
        pass

    logger = logging.getLogger(module)
    fhand = logging.FileHandler(fname)
    shand = logging.StreamHandler()

    formatter = logging.Formatter('(%(name)s) %(asctime)s %(levelname)s %(message)s')
    fhand.setFormatter(formatter)
    shand.setFormatter(formatter)

    logger.addHandler(fhand)
    logger.addHandler(shand)
    logger.setLevel(logging.DEBUG)

    return logger


if __name__ == '__main__':
    log = getLogger(__name__)
    log.debug('msg1')
    log.info('msg2')
    log.critical('msg3')
    log.warning('msg4')
    log.error('msg5')
