n=1
l=[]
while n<11:
    print("enter",n,"no.")
    num=float(input())
    n=n+1
    l.append(num)
print("negative numbers are")
for i in l:
    if i<0:
        print(i,end=",")
print()
print("positve numbers are")
for r in l:
    if r>0:
        print(r,end=",")
print()
print("even numbers are ")
for j in l:
    if j%2==0:
        print(j,end=",")
print()
print("odd numbers are")
for u in l:
    if u%2==1 :
        print(u,end=",")
print()
for k in range(len(l)):
    print(l[k],"occurances",l.count(l[k]))
