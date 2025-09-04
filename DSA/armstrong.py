num = int(input("Enter a number: "))
t = num 
count = 0
s = 0
temp = num
while temp != 0:
    temp //= 10
    count += 1
temp = num
while temp != 0:
    rem = temp % 10
    s += rem ** count
    temp //= 10
if s == t:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
