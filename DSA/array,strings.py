arr=eval(input())
print("Maximum value in arr:",max(arr))
print("Minimun value in arr:",min(arr))
#strings
s=input()
if(s==s[::-1]):
    print("Palindrome")
else:
    print("Not a Palindrome")