counter = 1
while counter <= 5:
    print("Hello World")
    counter += 1

for item in [1, 3, 6, 2, 5]:
    print(item)

for item in range(5):
    print(item ** 2)

wordList = ['cat', 'dog', 'rabbit']
letterList = []

for word in wordList:
    for letter in word:
        letterList.append(letter)

print(letterList)
