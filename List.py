#ordered,changeable and allow duplicates
list=["car","bike",30,40,3.0,"true"]

print(len(list))
print(type(list))
print(list[5])
print(list[2:5])
print(list[2:])
print(list[:5])

list[2]="scooter"

print(list)

list[1:3]=["scooter","plane","yatch"]

print(list)

list.insert(3,"jeep")

print(list)

list.append("oranges")

print(list)