'''
Ner Class
@author: Lorenzo
'''
from it.ds4biz.feature.FeatureExtractor import FeatureExtractor

class Ner:
    '''
    Name Entity Recognizer
    Superclass
    '''

    def extract(self,text):
        raise Exception("Not implemented \"extract\"")


class MlBasedNer(Ner):
    '''
    Machine Learning Based NER
    '''
    
    def __init__(self, mlClassifier):
        '''
        Takes as input as skleran clssifier 
        '''
        
        self.clf = mlClassifier
    
    
    def extract(self,text):

        y_hat = self.clf.predict(text)
        return y_hat


class  RuleBaseNER(Ner):
    
    def extract(self,text):
        raise Exception("Not implemented \"extract\"")
