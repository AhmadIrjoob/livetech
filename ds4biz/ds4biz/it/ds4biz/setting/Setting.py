'''
Created on Feb 22, 2018

@author: daniele
'''
from sklearn.feature_extraction.text import HashingVectorizer
from it.ds4biz.util.sklearnUtils import IdentityTransformer, BooleanBinarizer
from it.ds4biz.util.customVectorizer import mcTextVectorizer

class DefaultTrasformPipelineSetting(object):
    '''
    classe per la configurazione della pipeline
    Default parameters:
    
        ("t", [HashingVectorizer()])
        ("i", [IdentityTransformer()])
        ("f", [IdentityTransformer()])
        ("b", [BooleanBinarizer()])
    '''

    suf_to_setting_functions=dict()
    excludeSet = set()
    def __init__(self):

        self.add_column_type("t", [HashingVectorizer()])
        self.add_column_type("i", [IdentityTransformer()])
        self.add_column_type("f", [IdentityTransformer()])
        self.add_column_type("b", [BooleanBinarizer()])
        self.make_mult_colum_suffix({'t'})
        
    def make_mult_colum_suffix(self,listSuffixMultiColonizzer=set()):
        for x in listSuffixMultiColonizzer:
            listTrasform=self.suf_to_setting_functions[x]
            #print("tras",mcTextVectorizer(listTrasform[0][0]))
            #(mcTextVectorizer()
            
            d= [mcTextVectorizer(v) for v in listTrasform[0]]
            #print(d) 
            self.suf_to_setting_functions[x]=(d,listTrasform[1])
             
    def add_column_type(self,suffix,tranformation_list):
            selector_function = lambda x: self._filter_data_by_suffix(x, suffix)
            self.suf_to_setting_functions[suffix]= (tranformation_list, selector_function)
            

    def update_column_type(self,suffix,tranformation_list):
            print("update suffix: "+suffix)
            self.add_column_type(suffix, tranformation_list)


    def setexclude(self,excludeSet=set()):
            '''
             imposta i suffissi che non si vogliono analizzare
             exp: setexclude('t','i')  oppure setexclude(['t','i'])
             exp: setexclude() rimuove tutti i filtri
            '''
            self.excludeSet=excludeSet
            


    #TODO APPEND SUBTRASFORMATION BY SUFFIX 
    
    
    def get_trasformations(self):
        d = filter(lambda x: x[0] not in self.excludeSet ,self.suf_to_setting_functions.items())
        d = [v[1] for v in d] 
        return d
    
    def _filter_suffix(self,string,suffix, sep = "_"):
        found_suffix = string.split(sep)[-1]
        return found_suffix == suffix
    
    
    def _filter_data_by_suffix(self,data_frame,suffix):
        cols_ = list(data_frame.columns)
        keys_to_return = list(filter(lambda x: self._filter_suffix(x, suffix), cols_))
        return data_frame[keys_to_return]
    
if __name__ == '__main__':
        
    tr=DefaultTrasformPipelineSetting()
    tr.setexclude(('t','i'))
    print(tr.get_trasformations())
    