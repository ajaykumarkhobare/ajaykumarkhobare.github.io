fruits=["apple","banana","kiwi","mango"]
newfruit=[]

for x in fruits:
 if "i" in x:
  newfruit.append(x)

print(newfruit)

newfruit=[x for x in fruits if "a" in x]

print(newfruit)

newfruit=[x for x in fruits if x!="banana"]

print(newfruit)

newfruit=[x for x in range(10)]

print(newfruit)

newfruit=[x for x in range(10) if x<6]

print(newfruit)

newfruit=[x.upper() for x in fruits]

print(newfruit)

newfruit=[x if x!="banana" else "orange" for x in fruits]

print(newfruit)