'''
Created on Mar 9, 2018

@author: lorenzo
'''
from it.ds4biz.annotator.SimpleAnnotator import SimpleAnnotator
from it.ds4biz.builder.TrainBuilders import FilterWindowsTrainBuilder
from it.ds4biz.feature.FeatureExtractor import WindowsTextFeatureExtractor
from it.ds4biz.util.WordTokenizer import word_tokenizer

class ManualAnnotatorBuilder:
    '''
    crea un dataset con le annotazioni manuali
    '''


    def __init__(self, train_builder ,num_pred_word = -8,num_post_word = 8):
        '''
        Constructor
        '''
        self.num_pred_word = num_pred_word
        self.num_post_word = num_post_word
        self.annotator = SimpleAnnotator()
        self.train_builder = train_builder
        self.traindata = []
        
    def add_manual_annotation(self, text, target_tokens):
        
        annotext = self.annotator.annotate(text, target_tokens)
        print(list(annotext.all_annotation()))
        new_dataset_part = self.train_builder.build(annotext)
        self.traindata.extend(new_dataset_part)
        
    def all_dataset(self):
        for elment in self.traindata:
            yield elment
        
if __name__ == '__main__':
    text = "Buongiorno sono il Dottor. Zingler grande amico del Dott. Giorgio"
    text = word_tokenizer(text)
    target_tokens = ["Zingler", "Giorgio"]
    print(text,target_tokens)
    gen=FilterWindowsTrainBuilder(WindowsTextFeatureExtractor(),-100,100)

    annbuild = ManualAnnotatorBuilder(gen)
    annbuild.add_manual_annotation(text, target_tokens)
    for a in annbuild.all_dataset():
        print(a)
        
      
        
    