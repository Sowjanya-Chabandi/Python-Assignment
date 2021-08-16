'''12)Reverse Dictionary mapping
ex :  {'a':'1','b':'2','c':'3'}  -> {'1':'a','2':'b','3':'c'}'''

d={'a':'1','b':'2','c':'3'}
dict={b:a for a,b in d.items()}
print(dict)
