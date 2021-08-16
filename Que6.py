'''6)Get first non-repeating character from given string
ex: abcdcd --> a
abbcd ----> c '''

s=input()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
k=list(d.keys())
v=list(d.values())
ind=v.index(1)
print(k[ind])
