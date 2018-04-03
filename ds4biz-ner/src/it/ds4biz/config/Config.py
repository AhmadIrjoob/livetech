'''
Created on Jan 19, 2017
@author: tiziano
'''
import configparser
from configparser import ConfigParser
from variabili import BASEPATH


class Config(object):
    '''
    Classe di utils per il file config
    '''
    # name = '../../config/opencup.var.cfg'
    # name = '/home/daniele/workspace/OpenCup/config/opencup.var.cfg'
    name = BASEPATH + "/config/properties.ini"
    config = None

    def __init__(self, name=None):
        if not self.config:
            self.config = ConfigParser()
            self.config._interpolation = configparser.ExtendedInterpolation()
            if name is None:
                self.config.read(self.name)
            else:
                self.config.read(name)

    ################################################################# INPUT ########################################################################

    def getPathInput(self):
        return self.config.get('paths_input', 'input_text')
    
    def getWordPostiveList(self):
        return self.config.get('resources', 'positive_words')
    
    def getWordNegativeList(self):
        return self.config.get("resources", "negative_words")
    ################################################################# LOG ########################################################################
    def getLogOutput(self):
        return self.config.get('log', 'output_log')
    def getModelPath(self):
        return self.config.get("resources", 'model_dump')
 
 

if __name__ == '__main__':
    print(BASEPATH)
    #c = Config()
