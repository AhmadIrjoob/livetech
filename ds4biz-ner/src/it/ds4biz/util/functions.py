'''
Created on Mar 9, 2018

@author: lorenzo
'''
def _flatten(mylist):
    for item in mylist:
        yield from item