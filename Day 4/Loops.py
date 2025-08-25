#printing All odd values from 1 to n
n=int(input())
for i in range(n):
    if(i%2!=0):
        print(i,end=" ")

#while loops
#printing 2 table
n=int(input())
i=1
while(i<=10):
    print(i,"x",n,"=",i*n)
    i+=1