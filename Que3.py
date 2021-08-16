'''3)create an generator function to return next number in Fibonacci series.
ex : fib.next() -> 0
fib.next() -> 1
fib.next() -> 1
fib.next() -> 2 '''

def fib():
    a,b=0,1
    #for i in range(5):
    while(True):
        yield a
        a,b=b,a+b
y=fib()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

