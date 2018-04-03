def ngram(w,n):
    for i in range(len(w)-n+1):
        yield tuple(w[i:i+n])
        
def rangegram(w,m,n):
    for i in range(m,n+1):
        for el in ngram(w,i):
            yield el

def preceding(it,n):
    temp=[]
    for el in it:
        if len(temp)>n:
            temp.pop(0)
        yield el,temp[:]
        temp.append(el)

def after(it,n):
    temp=[next(it) for _ in range(n)]
    for el in it:
        ret=temp.pop(0)
        yield ret,temp[:]
        temp.append(el)
    while temp: 
        ret=temp.pop(0)
        yield ret,temp[:]

def windows(it,n):
    temp=[]
    for el in it:
        temp.append(el)
        if len(temp)==n:
            yield temp[:]
            temp.pop(0)

def purge(l):
    return [x for x in l if x]

def context(it,m,n):
    temp=decit(it,m,n,"^","$")
    for i,c in enumerate(windows(temp,m+n+1)):
        yield c[m],i ,c[:m],c[m+1:]
    
        
def decit(it,m,n,bsym=None,asym=None):
    for i in range(m):
        yield bsym
    for el in it:
        yield el
    for i in range(n):
        yield asym
        

if __name__=="__main__":

    s = "Buongiorno, mi chiamo Mario e so' mejo io"
    tmp=[]



    for el in context(s.split(" "),2,3):
        print(el)




