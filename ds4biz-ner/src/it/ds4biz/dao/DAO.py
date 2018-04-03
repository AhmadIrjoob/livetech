'''
Created on Feb 19, 2018

@author: daniele
'''
from it.ds4biz.log.LoggerUtils import getLogger
import os

#log = getLogger(__name__)



class TextDAO:
    def all(self):
        raise Exception("Not implemented \"all\"")
    
    
class FSTextDao(TextDAO):
    
    def __init__(self,path,header=False):
        self.path=path
        self.header = header
        
    def exist(self):
        if os.path.exists(self.path) is False:
            raise Exception("Not exist ", self.path)

    
    def all(self):
        self.exist()
        with open(self.path, encoding="latin") as stream:
            if self.header:
                next(stream)
            for line in stream:
                yield line


class FSAnnotatedTextDAO(FSTextDao):

    def all(self):
        self.exist()
        with open(self.path, encoding="latin") as stream:
            if self.header:
                next(stream)
            for line in stream:
                yield line

