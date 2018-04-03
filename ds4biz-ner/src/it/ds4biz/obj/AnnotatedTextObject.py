'''
Created on Feb 19, 2018

@author: daniele
'''
from it.ds4biz.obj.TextObject import TextObject

class AnnotatedTextObject(TextObject):
    '''
    rappresentazione della classe testo annotato
    '''

    
    
    def __init__(self, text):
        '''
        text : testo di input
        '''
        self.text=text
        self.annotations = list()
        
    
    def add_annotation(self,annotation):
        self.annotations.append(annotation)
      
    '''    
    iteratore sulle annotazioni
    '''   
    def all_annotation(self):
        yield self.annotations
        
    '''    
    ritorna la lista delle annotazioni
    ''' 
    def get_annotations(self):
        return self.annotations
        
