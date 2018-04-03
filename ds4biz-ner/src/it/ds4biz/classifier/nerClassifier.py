'''
Created on 20 feb 2018

@author: lorenzo
'''


from sklearn.base import ClassifierMixin
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
import dill
from it.ds4biz.util import CostumPipeline
from sklearn.ensemble.forest import RandomForestClassifier
from it.ds4biz.feature.FeatureExtractor import WindowsTextFeatureExtractor
from it.ds4biz.util.CostumPipeline import CustomPipeline
from it.ds4biz.util.functions import _flatten
import copy

class nerClassifier(ClassifierMixin):

    '''
    classifier for mlNer base on Sklearn
    '''

    def __init__(self, model, extractor, custom_pipeline):
        '''
        Constructor
        '''
        self.model = model
        self.extractor = extractor
        self.cust_pipe = custom_pipeline
    
    def _regroup(self, vector, size_of_groups):
        output = []
        for size in size_of_groups:
            item = vector[:size]
            output.append(item)
            vector = vector[size:]
        return(output)

        
    def fit(self,x,y):
        
        x = self.cust_pipe.fit_transform(x)
        self.model.fit(x,y)
        return self.model
    
    def predict(self,text):
        
        #text = text.get_text()
        multi_text_extract = map(lambda x: self.extractor.extract(x.get_text()), text)
        multi_text_extract_for_len= copy.deepcopy(multi_text_extract) 

        lenghts = [len(list(x)) for x in multi_text_extract_for_len]
        #if len(multi_text)==0: return[]
        #multi_text_extract = map(lambda x: self.extractor.extract(x), multi_text)
        x = list(_flatten(multi_text_extract))
        x = self.cust_pipe.transform(x)
        predictions =  self.model.predict(x)
        
        return self._regroup(predictions, lenghts)
        
    
    
    def save(self, filename):
        class_string = dill.dumps(self)
        joblib.dump(class_string,filename,9)
    
    
class nerGridSearchClassifier(nerClassifier):
    '''
    
    '''
    
    
    def __init__(self, model, parmeters_grid, extractor, custom_pipeline, **kwargs):
        
        '''
        parmeters_grid: {'n_estimation':[80,100,200],'criterion':'Entropy'}
        '''
        
        model = GridSearchCV(estimator=model,
                             param_grid= parmeters_grid,
                             **kwargs)
        
        super().__init__(model, extractor, custom_pipeline)
        
        


def load(filename):
       
        return  dill.loads(joblib.load(filename))
        
        
if __name__ == '__main__':
    
    a = RandomForestClassifier()
    e = WindowsTextFeatureExtractor()
    k = CustomPipeline()
    obj = nerGridSearchClassifier(a,{"f":[1,3,4]}, e,k)
    print(obj.__dict__)
    
    obj.save("/home/ahmad/ahmad/test_dump.pkl")
    
    
    obj2 = load("/home/ahmad/ahmad/test_dump.pkl")
    
    print(obj2.__dict__)
    print(obj2.cust_pipe.__dict__)

    
    
    

    