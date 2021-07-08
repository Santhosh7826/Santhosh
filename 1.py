n=int(input())
n1=n
rem=0
sum=0
while(n>0):
    rem=n%10
    sum+=rem**3
    n=n//10
if(n1==sum):
    print(n1," is armstrong")
else:
    print("not armstrong")

