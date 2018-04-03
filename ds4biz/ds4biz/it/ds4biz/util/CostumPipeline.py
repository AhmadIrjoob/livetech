'''
Created on Feb 21, 2018

@author: lorenzo
'''
from sklearn.pipeline import make_union, make_pipeline, Pipeline
from sklearn.preprocessing._function_transformer import FunctionTransformer
from it.ds4biz.setting.Setting import DefaultTrasformPipelineSetting
import pandas as pd
from sklearn.externals import joblib         
import dill
from pprint import pprint

class CustomPipeline(Pipeline):
    
    def __init__(self,trasform_pipe_setting=DefaultTrasformPipelineSetting()):
        '''
            input:TrasformPipelineSetting (DefaultTrasformPipelineSetting)
        '''
        self.transformations=trasform_pipe_setting.get_trasformations()
        self.__dict__= self._settingParsergetPipeline().__dict__
    
    def _trasformToDataframe(self,X):
        try:
            if not isinstance(X,pd.DataFrame):
                X = pd.DataFrame(list(X))
        except Exception as e:
            print(e)  
        
        return X
    
    def fit(self, X):
        '''
        X instance of Dataframe or X instance of Iterable of Dictionary
        
        '''
        print('FIT')
        super().fit(self._trasformToDataframe(X))
                    
    
    def transform(self,X):
        '''
        X instance of Dataframe or X instance of Iterable of Dictionary
        
        '''
        x  = self._trasformToDataframe(X)
        
        return super().transform(x)
                    
    def fit_transform(self, X):
        t = self._trasformToDataframe(X)
        #print(t)
        return super().fit_transform(t)
        
        
    def _settingParsergetPipeline(self):
        
        pipe_parts = []
        for trs,selector_function in self.transformations:
            this_pipe = make_pipeline(FunctionTransformer(selector_function,validate=False), *trs)

            pipe_parts.append(this_pipe)
        
        
        the_pipeline = make_union(*pipe_parts)
        return make_pipeline(the_pipeline)
    
    def save(self,filename):
        joblib.dump(dill.dumps(self), filename)
        
    def get_save_string(self):
        return dill.dumps(self) 
    
def load_custom_pipe(filename):
    return dill.loads(joblib.load(filename) )
    

if __name__ == '__main__':
    p=CustomPipeline()
    p.save("/home/daniele/tmp.gen")
    a = load("/home/daniele/tmp.gen")
    print(a.steps) 
    
