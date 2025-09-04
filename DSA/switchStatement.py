a=int(input("Enter a num1:"))
b=int(input("Enter a num2:"))
c=input("Enter the operation (+,-,*,/):")
match c:
    case "+":
        print("The sum is:",a+b)
    case "-":
        print("The difference is:",a-b)
    case "*":
        print("The product is:",a*b)
    case "/":
        print("The quotient is:",a/b)