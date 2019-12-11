aName = "allen"
age = 27

print(aName, "is", age, "years old")
print("%s is %d years old" % (aName, age))

price = 24
item = "banana"
print("The %s costs %d cents" % (item, price))
print("The %+10s costs %5.2f cents" % (item, price))
itemDict = {
    "item": "banana",
    "price": 24
}
print("The %(item)s costs %(price)7.1f cents" % itemDict)
