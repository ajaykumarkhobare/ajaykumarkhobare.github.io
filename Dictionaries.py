#unordered,changeable and do not allow duplicate

dictt={
 "key":"value",
 "name":"Raj",
 "age":"26",
 "vehicle":"Ford Endeavour",
 "DOB":"12/12/12",
 "fruits":["Oranges","Pineapples","Blueberries"]
}

print(dictt)
print(len(dictt))
print(type(dictt))

x=dictt["vehicle"]

print(x)

dictt["vehicle"]="bike"

print(dictt)

dictt.update({"name":"Prakash"})

print(dictt)

dictt["colour"]="Black"

print(dictt)

dictt.pop("vehicle")

print(dictt)
