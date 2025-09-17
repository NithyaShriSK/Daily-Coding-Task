num=int(input())
n1=0
n2=1
print("Fibonacci series upto ",n,"terms:")
for i in range(num):
    print(n1,end=" ")
    temp=n1+n2
    n1=n2
    n2=temp