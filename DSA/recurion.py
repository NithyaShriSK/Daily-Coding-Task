def recur(a):
    if(a==0):
        return
    else:
        print("Hello")
        return recur(a-1)
a=int(input())
recur(a)