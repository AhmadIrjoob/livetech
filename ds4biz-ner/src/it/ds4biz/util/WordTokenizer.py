'''
Created on Feb 28, 2018

@author: lorenzo
'''
from nltk.tokenize import word_tokenize
import re



def word_tokenizer(text):
    tokens = word_tokenize(text, language="italian")
    #print(tokens)
    tokens = filter(lambda x: x.isalpha() or x.isnumeric(), tokens)
    #tokens =[word for word in tokens if word.isalpha()]
    
    return list(tokens)

def number_tokenizer(text):
    l = " "
    text = text.lower()
    for r in re.findall(r"([^0-9]*)?([0-9]*)?",text):
        l=l+" ".join(r)
        l+=" "
 
    return word_tokenizer(l)
        
if __name__ == '__main__':
    s=number_tokenizer("STUDIOINFO_FIRMADa: segreteria@pec.studiolegaledalponte.itInviata: 9/8/2017 8:50:16 AMA: generaliitalia@pec.generaligroup.comCc: Oggetto: Recesso dalla polizza n291648365Si veda la lettera in allegato.Cordiali saluti.avv. Andrea Dalponte   Avv. Andrea DalponteStudio Legale Avv. Andrea DalponteViale A. Lutti n. 10 - 38066 Riva del Garda (TN)Tel. 0464-556155 Fax 0464-560414 All.: c.s.")
    print(s)