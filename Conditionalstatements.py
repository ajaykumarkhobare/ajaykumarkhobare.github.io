#a==b
#a!=b
#a<b
#a<=b
#a>b
#a>=b

a=33
b=200

if a>b:
 print("a is greater than b")
else:
 print("b is greater than a")

a=33
b=33

if a>b:
 print("a is greater than b")
elif a==b:
 print("a and b are equal")

a=33
b=200
c=300

if a>b and c>a:
 print("r")
else:
 print("w")

if a>b or c>a:
 print("r")
else:
 print("w")
