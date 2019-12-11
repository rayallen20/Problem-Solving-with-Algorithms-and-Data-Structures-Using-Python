import math

n = input("Please input n: ")
n = float(n)

if n < 0:
    print("Sorry, value is negative")
else:
    print(math.sqrt(n))

score = input("Please input score: ")
score = float(score)

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

sqList = []
for x in range(1, 11):
    sqList.append(x ** 2)

print(sqList)

sqList = [x ** 2 for x in range(1, 11)]
print(sqList)

sqList = [x ** 2 for x in range(1, 11) if x % 2 != 0]
print(sqList)

charList = [ch.upper() for ch in "comprehension" if ch not in 'aeiou']
print(charList)
