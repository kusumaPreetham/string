#fibonacci series
n1 = 0
n2 = 1
n=int(input("Enter the number:"))
i=1
if n==0:
    print(n1)
elif n==2:
    print(n1,n2,end="")
else:
    print(n1,n2,end="")
    while i<n-1:
        n3=n1+n2
        print(n3,end="")
        n1=n2
        n2=n3
        i=i+1