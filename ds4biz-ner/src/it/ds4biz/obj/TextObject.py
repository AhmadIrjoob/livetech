'''
Created on Feb 19, 2018

@author: daniele
'''

class TextObject(object):
    '''
    rappresentazione della classe testo
    '''


    def __init__(self, text):
        '''
        text : testo di input
        '''
        self.text=text
        
    def get_text(self):
        if len(self.text)==0:
            return ["a"]
        return self.text
    
