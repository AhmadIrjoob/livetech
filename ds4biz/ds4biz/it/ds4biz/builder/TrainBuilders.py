'''
Train Dataset Builder

@author: Lorenzo
'''
from it.ds4biz.obj.AnnotatedTextObject import AnnotatedTextObject
from it.ds4biz.feature.FeatureExtractor import WindowsTextFeatureExtractor

class TrainBuilder:
    
    def __init__(self, featureExtractor):
        self.featureExtractor = featureExtractor
        
    def _get_label(self, pox, annotations,negativeLabel):
        for annotation in annotations:
            if pox in range(annotation[1], annotation[2]):
                return annotation[0]
        
        return negativeLabel


    def build(self, annotetedText,negativeLabel="NoEntity"):
        '''
        #commentare
        '''    
        token = annotetedText.get_text()
        annotations = annotetedText.get_annotations()
        vector_features = self.fextr.extract(token)
        for w in vector_features:
            pox = w.get_target_pos()
            label = self._get_label(pox, annotations,negativeLabel)
            yield (label, w)

        
        
class FilterWindowsTrainBuilder(TrainBuilder):
    '''
    classe che crea le annotazioni da passare a, 
    
    self.num_pred_word: lunghezza inferiore della finestra da utilizzare come contesto per il training set
    self.num_post_word: lunghezza superiore della finestra da utilizzare come contesto per il training set
    '''

    
    def __init__(self,featureExtractor,num_pred_word = -8,num_post_word = 8):
        '''
        Constructor
        '''
        self.fextr=featureExtractor
        self.num_pred_word = num_pred_word
        self.num_post_word = num_post_word
    
    
    def build(self, annotetedText,negativeLabel="NoEntity"):

        annotations = annotetedText.get_annotations()
        space_range = list(map(lambda x: range(x[1]+self.num_pred_word, x[2]+self.num_post_word), annotations))
        for label,w in super().build(annotetedText, negativeLabel):
            pox = w.get_target_pos()
            if any(pox in x for x in space_range):
                yield (label, w)
        
            

if __name__ == '__main__':
    an = AnnotatedTextObject("ciao amici miei sono proprio io, questa è una prova lungihissima che mi deve ridare solo una parte del tutto e basta prova aaa ss ss dd".split(" "))
    an.add_annotation(("IE",1,2))
    an.add_annotation(("FE",4,5))

    gen=FilterWindowsTrainBuilder(WindowsTextFeatureExtractor(pre_size=100,post_size=0),-4,4)
    a = gen.build(an) 
    for el in a:
        print(el)
        