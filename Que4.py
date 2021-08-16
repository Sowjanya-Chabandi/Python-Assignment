'''4)write a common function to print area of square and reactangle based
on input'''

def area(a=None,b=None):
    if a!=None and b!=None:
        print("Area of rectangle is:",(a*b))
    elif a!=None:
        print("Area of square is:",(a*a))
    
area(10)
area(10,20)

    
