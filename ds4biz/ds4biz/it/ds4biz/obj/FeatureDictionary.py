'''
Created on Feb 19, 2018

@author: daniele
'''

class FeatureDictionary(dict):
    '''
    estende un  dict
    '''
    
    def get_target_word(self): 
        return self.get("target_word_t",None)
    
    def get_target_pos(self):
        return self.get("target_the_position_i",None)

        