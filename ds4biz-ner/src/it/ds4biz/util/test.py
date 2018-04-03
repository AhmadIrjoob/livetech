from it.ds4biz.util.Windows import context
from it.ds4biz.util.WordTokenizer import number_tokenizer
import unittest




class TestWT (unittest.TestCase):
    def testWT(self):

        s = number_tokenizer(
        "STUDIOINFO_FIRMADa: segreteria@pec.studiolegaledalponte.itInviata: 9/8/2017 8:50:16 AMA: (TN)Tel. 0464-556155 Fax 0464-560414 All.: c.s.")

        self.assertEqual(s,['segreteria', '9', '8', '2017', '8', '50', '16', 'ama', 'tn', '0464', '556155', 'fax', '0464', '560414', 'all'])


    def testW(self):
        s = "Hi Iam Ahmad"


        aa=[ ('Hi'  , 0, ['^'] , ['Iam'])
            ,('Iam'  , 1, ['Hi'], ['Ahmad'])
            ,('Ahmad', 2, ['Iam'], ['$'])]

        for i,el in enumerate(context(s.split(" "), 1, 1),start=0):
            self.assertEqual(aa[i], el)


if __name__ == '__main__':
    unittest.main()

