def count(word):
    out={}
    for i in word:
        if i in out:
            out[i]+=1
        else:
            out[i]=1
    return out

count('srikanth')