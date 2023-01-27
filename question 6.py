a=int(input("enter the starting no for range "))
b=int(input("enter the end no for the range "))
for i in range(a,b+1):
    if i>1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(i,"is prime no.")
            
