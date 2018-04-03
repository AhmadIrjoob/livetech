'''
Created on Mar 6, 2018

@author: daniele
'''
from it.ds4biz.ner.Ner import RuleBaseNER
import re

class RegExRuleBasedNer(RuleBaseNER):
    '''
    classdocs
    '''

    #pattern = r"(^|\b|n|N|[^A-Za-z0-9])([0-9]{9})([^0-9]|$)"
    def __init__(self,  pattern = r"\b([0-9]{9})\b"):
        '''
        applica una regola expression per recuperare le entità
        ''' 
        self.pattern=pattern
    
    def extract(self, text):
        ''' 
        
        '''
        t = " ".join(text)
        self.pattern = self.pattern


        if not isinstance(t,str):
            return set()

        found_items = set()
        if len(t) > 0:
            for r in re.findall(self.pattern, t):
                found_items.add(r)
        else:
            return set()
        return found_items
            