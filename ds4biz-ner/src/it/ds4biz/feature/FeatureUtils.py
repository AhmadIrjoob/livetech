'''
Created on Feb 19, 2018

@author: daniele
'''
'''
return features UpperCase and Lenght
'''
def getBaseWordFeatures(word, feat_dict={},prefix=""):

    feat_dict[prefix+"_is_first_uppercase_b"]= word.istitle()
    feat_dict[prefix+"_lenght_i"]=len(word)
    return feat_dict


'''
return features UpperCase and Lenght
'''
def getBaseTargetWordFeatures(word,pox,feat_dict={},prefix=""):

    feat_dict[prefix+"_word_t"]= word
    feat_dict[prefix+"_the_position_i"]=pox
#    feat_dict[prefix+"_word_is_numeric_b"] = word.isnumeric()
    return feat_dict


'''
return features number and start 
'''
def getBaseTargetWordNumberFeatures(word,feat_dict={},prefix=""):

    feat_dict[prefix+"_start_with_t"] = word[0]
    feat_dict[prefix+"_word_is_numeric_b"] = word.isnumeric()
    
    return feat_dict


'''
return feature Gender
'''
def getGenderWordFeatures(word, feat_dict={},prefix=""):
    
    if  word[-1]=="a":
        g="F"
    feat_dict[prefix+"_gender_t"]=g
    return feat_dict

'''
return UpperCase and Lenght
'''
def getFullCapitalWordFeatures(word, feat_dict={},prefix=""):
    feat_dict[prefix+"_is_uppercase_b"]=word.isupper()
    return feat_dict


if __name__ == '__main__':
    w = ""
    print(w[0])