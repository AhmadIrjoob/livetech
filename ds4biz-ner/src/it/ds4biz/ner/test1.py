
import unittest

from it.ds4biz.config.Config import Config
from it.ds4biz.ner.nltkRuleBasedNer import FilterNltkRuleBasedNer


class TestNer (unittest.TestCase):
    def testner(self):

        test = "Buongiorno, mi chiamo Lorenzo Lancia e abito in via Casal De Pazzi 20"
        text = test.split(sep=" ")
        Ner = FilterNltkRuleBasedNer(path_to_positive=Config().getWordPostiveList()
                                     ,path_to_negative=Config().getWordNegativeList())

        self.assertEqual(Ner.extract(text), ['Lancia Lorenzo'])

if __name__ == '__main__':
    unittest.main()