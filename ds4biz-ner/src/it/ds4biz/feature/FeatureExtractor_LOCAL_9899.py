'''
Feature Extractor for Ner

@author: Lorenzo
'''
from src.it.ds4biz.obj.TextObject import TextObject
from src.it.ds4biz.util.Windows import context
from src.it.ds4biz.feature.FeatureUtils import getBaseWordFeatures,\
    getBaseTargetWordFeatures
from src.it.ds4biz.obj.FeatureDictionary import FeatureDictionary

class FeatureExtractor:
    
    def __init__(self):
        raise Exception("Not implemented")

    
    
    def extract(self, object):
        raise Exception("Not implemented: extract")

    
        

class TextFeatureExtractor(FeatureExtractor):

    def extract(self, tokens):
        if not isinstance(tokens, list):
            raise Exception("tokens must be list")

 
class uniqwordTexxtFea(TextFeatureExtractor):

    def extract(self, tokens):
        feat_dict=FeatureDictionary()
        for t in tokens:
            feat_dict=getBaseTargetWordFeatures(t,0,feat_dict,"target")

   
class WindowsTextFeatureExtractor(TextFeatureExtractor):

    def __init__(self,pre_size=2,post_size=2):
        self.pre_size=pre_size
        self.post_size=post_size
        
        
    def extract(self, tokens):
        super().extract(tokens)
        for word_target,pox,pre_words,post_words in context(tokens,self.pre_size, self.post_size):
            feat_dict=FeatureDictionary()
            
            feat_dict=getBaseTargetWordFeatures(word_target,pox,feat_dict,"target")
            feat_dict=getBaseWordFeatures(word_target,feat_dict,'target')
            
            for ind, word in enumerate(pre_words):
                feat_dict["pred_word_" + str(ind)+"_t"] = word
                feat_dict= getBaseWordFeatures(word,feat_dict, "pred_word_" + str(ind))

            for ind, word in enumerate(post_words):
                feat_dict["foll_word_" + str(ind)+"_t"] = word
                feat_dict= getBaseWordFeatures(word, feat_dict,"foll_word_" + str(ind))
            
            yield feat_dict        
        
        
if __name__ == '__main__':
    w=WindowsTextFeatureExtractor(pre_size=3)
    for d in  w.extract("ciao amici miei sono proprio io".split(" ")):
     print(d.get_target_word())
    
    
    
    
    
    