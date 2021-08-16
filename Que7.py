'''7)Find the number of substrings need to cut from given number to get a hidden palindrome in string
ex: input -> poirioky
output -> oirio - 2 cuts
iri - 2 cuts
input -> oirioky
output -> oirio - 1 cuts
iri - 2 cuts'''

def pal(s):
    for i in range(len(s)//2):
        if s[i]!=s[-1*(i+1)]:
            return False
    return True
def palindrome(str):
    l,r=0,len(str)
    j=r
    res=[]
    b=[]
    while l<r+1:
        temp=str[l:j]
        j-=1
        if pal(temp):
            res.append(temp)
        if j<l+2:
            l+=1
            j=r
    a=[]
    for i in range(len(res)):
        if len(res[i])>1:
            a.append(res[i])
    #return list(set(a))  
    
    for i in range(len(a)):
        i1=s.index(a[i][0])
        i2=s.index(a[i][-1])
        if i1==0 or i2==-1:
            print(a[i]," 1 cut")
        else:
            print(a[i]," 2 cuts")
s=input()
palindrome(s)
