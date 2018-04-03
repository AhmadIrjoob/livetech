'''
Created on Feb 21, 2018

@author: lorenzo
'''
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
from it.ds4biz.util.sklearnUtils import ItemSelector



class mcTextVectorizer(BaseEstimator, TransformerMixin):
    '''
    Multi Column Text Vectorizer
    '''
    def __init__(self, Vectorizer):
        self.vectorizer = Vectorizer
        
        
    
    def fit(self,x,y=None):
        transformations =  [
        (cname, Pipeline([
            ('selector', ItemSelector(key=cname)),
            ('vectorizer', self.vectorizer)
        ]))

        for cname in list(x.columns)
        ]
        
        self.thePipeline = Pipeline([
            ('union', FeatureUnion(transformer_list= transformations))
        ])
        
        self.thePipeline.fit(x)
        
        return self
    
    def transform(self,x):
        return self.thePipeline.transform(x)
        
        