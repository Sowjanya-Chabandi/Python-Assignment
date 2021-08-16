'''1)Get the difference betwen max and min number can be formed from input number
ex: input 126345
output 530865‬ explanation => 654321-123456'''

n=int(input("Enter a number:"))
s=list(map(int,str(n)))
s.sort(reverse=True)
max=int("".join(map(str,s)))
s.sort()
min=int("".join(map(str,s)))
print(int(max)-int(min))
