import unittest

from it.ds4biz.builder.ManualAnnotator import ManualAnnotatorBuilder
from it.ds4biz.builder.TrainBuilders import FilterWindowsTrainBuilder
from it.ds4biz.util.WordTokenizer import word_tokenizer
from it.ds4biz.feature.FeatureExtractor import WindowsTextFeatureExtractor



class TestBuilder (unittest.TestCase):
    def testManual(self):
        text = "Buongiorno sono il Dottor. Zingler grande amico del Dott. Giorgio"
        text = word_tokenizer(text)
        target_tokens = ["Zingler", "Giorgio"]
        print(text, target_tokens)
        gen = FilterWindowsTrainBuilder(WindowsTextFeatureExtractor(), -100, 100)

        annbuild = ManualAnnotatorBuilder(gen)
        annbuild.add_manual_annotation(text, target_tokens)
        c=['Buongiorno','sono','il','Dottor','Zingler','grande','amico','del','Dott','Giorgio','$']
        for i,a in enumerate(annbuild.all_dataset(),start=0):
            self.assertEqual(a[1]['target_lenght_i'],len(c[i]))
            self.assertEqual(a[1]['target_start_with_t'], c[i][0])
            self.assertEqual(a[1]['target_word_t'], c[i])
            self.assertEqual(a[1]['target_is_first_uppercase_b'], c[i][0].isupper())




if __name__ == '__main__':
    unittest.main()