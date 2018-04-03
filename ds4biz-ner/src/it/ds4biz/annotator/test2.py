import unittest

from it.ds4biz.annotator.SimpleAnnotator import SimpleAnnotator



class TestAnnotator (unittest.TestCase):
    def testann(self):
        a = ["a", "B", "ccc", "dd"]
        tg = ["dd"]
        sa = SimpleAnnotator()
        at = sa.annotate(a, tg)
        at.get_annotations()
        self.assertEqual(at.get_annotations(),[(True,5,4)])




if __name__ == '__main__':
    unittest.main()