import math as m
len1=input(" length of first side")
len2=input(" length of second side")
len3=input(" length of third side")
len1=float(len1)
len2=float(len2)
len3=float(len3)
if len1+len2>len3 and len2+len3>len1 and len3+len1>len2:
    s=len1+len2+len3/2
    d=s*(s-len1)*(s-len2)*(s-len3)
    area=m.sqrt(d)
    print("area of triangle by heron's formulae",area)
else:
    print("no triangle exist with these sides")
