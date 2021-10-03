numbers=[1,2,3,4,5,67,89,100]

for x in numbers:
 print(x)

for x in numbers:
 if x==5:
  break
 print(x)

for x in numbers:
 if x==4:
  continue
 print(x)

x="fruits"

for a in x:
 print(a)

for x in range(100):
 print(x)

for x in range(40,100):
 print(x)

i=1
while i<6:
 print(i)
 if i==3:
  break
 i+=1

i=1
while i<6:
 i+=1
 if i==3:
  continue
 print(i)
