#call by reference
a=int(input())
b=int(input())
def numbers(a,b):
    print("The sum of two value:",a+b)
numbers(a,b)
#call by value
def number(a,b):
    print("The product os two numbers:",a*b)
number(10,5)