'''
Created on 20 feb 2018

@author: lorenzo
'''

from it.ds4biz.ner.Ner import RuleBaseNER
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from it.ds4biz.config.Config import Config
from nameparser.parser import HumanName


 
class NltkRuleBasedNer(RuleBaseNER):
    '''
    classdocs
    '''

    def _get_human_names(self,tokens):
    
        pos = pos_tag(tokens,lang='ita')
        sentt = ne_chunk(pos, binary=False)
        person_list = []
        person = []
    
        name = ""
    
        for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
    
            for leaf in subtree.leaves():
                person.append(leaf[0])
    
            if len(person) > 1:  # avoid grabbing lone surnames
    
                for part in person:
                    name += part + ' '
    
                if name[:-1] not in person_list:
                    person_list.append(name[:-1])
    
                name = ''
    
            person = []
    
        out_list = [HumanName(name).last + ' ' + HumanName(name).first for name in person_list]
    
        return (out_list)
    
    
    def extract(self, text):
        candidates = self._get_human_names(text)
        return candidates
    
    
    
class FilterNltkRuleBasedNer(NltkRuleBasedNer):
    '''
    Filtered with positve and negative word list
    '''
    def _read_words(self,path):
        word_list = []
        with open(path, 'r') as open_file:
            contents = open_file.readlines()
            for i in range(len(contents)):
                word_list.append(contents[i].strip('\n'))
        return word_list
    
    def _any_word_in_list(self,la,lb):
        la = [l.lower() for l in la]
        lb = [l.lower() for l in lb]
        l=any(x in la for x in lb)
        return (any(x in la for x in lb))
            
    def __init__(self,path_to_positive,path_to_negative):
        self.positive_words = self._read_words(path_to_positive)
        self.negative_words = self._read_words(path_to_negative)
        
    
    def extract(self, text):
        candidates = super().extract(text)
        
        #filter with positive and negative        
        candidates = filter(lambda x: self._any_word_in_list(x.split(" "), self.positive_words), candidates)
        candidates = filter(lambda x: not self._any_word_in_list(x.split(" "), self.negative_words), candidates)
        
        return list(candidates)
    
        
if __name__ == '__main__':
    test = "Buongiorno, mi chiamo Lorenzo Lancia e abito in via Casal De Pazzi 20"
    text = test.split(sep=" ")
    Ner = FilterNltkRuleBasedNer(path_to_positive=Config().getWordPostiveList(),path_to_negative=Config().getWordNegativeList())
    print(Ner.extract(text))
