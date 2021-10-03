#lambda #anonymousfunction

x= lambda a: a+20
print(x(5))

x= lambda a,b: a+b
print(x(5,30))

def f1(n):
 return lambda a:a*n

doub= f1(2)
trip= f1(3)

print(doub(11))
print(trip(11))

#filters #specifiedfunction

def prime(x):
 for n in range(2,x):
  if x%n==0:
   return False
  else:
   return True

filtered= filter(prime,range(10))

print("Prime numbers are: ", list(filtered))

#map #specifiedfunction

def square(x):
 return x*x

numbers=[1,2,3,4,5]

listsquare= map(square,numbers)

print(list(listsquare))

