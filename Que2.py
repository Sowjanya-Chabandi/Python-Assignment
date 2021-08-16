'''2)find whether parantheses in string is balanced or not
ex : "(()())" --> True
"((())" --> False'''

s=input()
c=0
l1=["(","{","["]
l2=[")","}","]"]
for i in s:
    if i in l1:
        c+=1
    elif i in l2:
        c-=1
    
if c==0:
    print('True')
else:
    print('False')
