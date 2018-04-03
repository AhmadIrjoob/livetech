'''
Created on Mar 9, 2018

@author: lorenzo
'''
from it.ds4biz.obj.AnnotatedTextObject import AnnotatedTextObject
from it.ds4biz.annotator.Annotator import TextAnnotator

class SimpleAnnotator(TextAnnotator):

    def __init__(self):
        pass
   
    def _find_sublist(self, sub, bigger):
        if not bigger:
            return -1
        if not sub:
            return 0
        first, rest = sub[0], sub[1:]
        pos = 0
        try:
            while True:
                pos = bigger.index(first, pos) + 1
                if not rest or bigger[pos:pos+len(rest)] == rest:
                    return pos
        except ValueError:
            return -1
        
    def _index_find(self,candidates, text, ind = 0):
        for candidate in candidates:
            candidate = list([candidate])
            indexofcand = self._find_sublist(candidate, text[ind:])
            if indexofcand > -1:
                yield (ind+indexofcand-len(candidate) , ind + indexofcand)
                if indexofcand + ind < len(text)-1:
                    yield from self._index_find([candidate], text, ind = indexofcand)
        
        
    def annotate(self, text, target_tokens):
        annoText = AnnotatedTextObject(text)
        
        set_of_index_found =set(self._index_find(target_tokens, text))
      
        for start,stop in set_of_index_found:
            for en in range(start, stop):
                annoText.add_annotation((True,en,en+1))
        return annoText
            

if __name__ == '__main__':
    a = ["a","B","ccc","dd"]
    tg = ["dd"]
    sa = SimpleAnnotator()
    at = sa.annotate(a, tg)
    print(at.get_annotations())
            
            
            