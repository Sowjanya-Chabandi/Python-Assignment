'''11)write a program to read text from a file and write into another file.'''

f=open("file1.txt","r")
print("file opened to read")
data=f.read()
print(data)
f.close()

f1=open("C:\\SOWJANYA\\Python Assignment\\file2.txt","w")
print("file opened to write")
f1.write("Hello World!\n")
f1.write("Welcome")
f1.close()



