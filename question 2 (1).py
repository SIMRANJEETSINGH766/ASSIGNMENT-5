a=input("enter the starting no of range ")
b=input("enter the end no of range ")
c=input("enter by which to divide")
a=int(a)
b=int(b)
c=int(c)
print("range of no",a,"---",b)
for i in range(a,b+1):
    if i%c==0:
        print(i, "is divisible by" ,c)
