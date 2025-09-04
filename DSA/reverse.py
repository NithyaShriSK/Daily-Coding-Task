num=12345
rnum=0
while(num!=0):
    rnum=rnum*10+(num%10)
    num=num//10
print(rnum)