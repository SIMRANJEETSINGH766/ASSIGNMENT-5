l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n=input("enter the no of rows to print")
b=int(n)
a=0
for i in range(0,b+1):
    for j in range(0,i):
        if a>25:
            a=a%25-1
        print(l[a],end="")
        a=a+1
    print("")
