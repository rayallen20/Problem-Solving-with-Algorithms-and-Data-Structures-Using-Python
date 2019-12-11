import math

inputNum = input("Please enter a integer :")
inputNum = float(inputNum)
try:
    math.sqrt(inputNum)
except ValueError:
    print("Bad value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(inputNum)))

inputNum = input("Please enter a integer :")
inputNum = float(inputNum)

if inputNum < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(inputNum))
