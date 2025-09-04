def Prime(a):
    if a==2:
        return "Prime"
    else:
        for i in range(2,(a//2)+1):
            if(a%i==0):
                return "Not Prime"
        return "prime"
a=int(input())
n=0
prime=Prime(a)
print(prime)