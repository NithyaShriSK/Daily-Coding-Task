def recur(a,i):
    if(i==a):
        return
    else:
        print(i,end=" ")
        return recur(a,i+1)
a=int(input())
i=1
recur(a+1,i)