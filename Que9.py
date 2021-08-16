'''9)Get list of duplicate number from the list and the complexity should be O(n)'''

l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)
print(l2)
