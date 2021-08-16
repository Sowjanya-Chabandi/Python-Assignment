'''5)form the largest number from the given list of non negetive numbers   3 8 5 9 98 101
ex: [3,8,5,9,98,101] -> 998853101 '''

def fun(ele):
    return str(ele)[0]
l=list(map(int,input().split()))
l.sort(reverse=True,key=fun)
s=""
for i in l:
    s+=str(i)
print(s)
