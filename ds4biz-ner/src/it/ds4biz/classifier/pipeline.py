'''
Created on Feb 21, 2018

@author: lorenzo
'''

class nerClassPipeline:
    def __init__(self,classifier,transformer):
        self.cls = classifier
        self.transformer = transformer
        
    def fit(self,X,y):
        X = self.transformer.fit_transform(X)
        return self.cls.fit(X,y)
    
    def predict(self, X):
        X = self.transformer.transform(X)
        return self.clf.predict(X)
    