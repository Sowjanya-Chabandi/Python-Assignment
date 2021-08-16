'''8)implement stack to support push,pop,getmin,getmax,top without any inbuilt functions'''

class Stack:
    def __init__(self):
        self.items=[]
    def push(self,val):
        self.items=[val]+self.items
        return self.items
    def pop(self):
        if len(self.items)<=0:
            return "No element in the stack"
        self.items=self.items[1:]
        return self.items
    def top(self):
        return self.items[0]
    def getmin(self):
        self.items.sort()
        return self.items[0]
    def getmax(self):
        self.items.sort()
        return self.items[-1]

s=Stack()
print(s.pop())
print(s.push('2'))
print(s.push('8'))
print(s.push('6'))
print(s.push('0'))
print(s.pop())
print(s.top())
print(s.getmin())
print(s.getmax())
