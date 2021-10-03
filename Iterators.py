tuple1= ("car","bike","train")
myit= iter(tuple1)

print(next(myit))
print(next(myit))
print(next(myit))

tuple2= "apples"
myit= iter(tuple2)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
 def __iter__(self):
  self.a= 1
  return self
 def __next__(self):
  x= self.a
  self.a+= 1
  return x

myclass= MyNumbers()
myiter= iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))