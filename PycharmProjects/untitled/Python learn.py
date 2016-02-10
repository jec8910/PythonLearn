print("Hello world")
myName = raw_input("What is your name?")
myVar = 'Hello'
print(myName)
print(myVar)

import math
radius = int(raw_input('Radius: '))
print("Circumference: "+str(2*radius*math.pi))
print("Area: " + str(radius*radius*math.pi))

for radius in range(5)
    print("Circumference: "+str(2*radius*math.pi))
    print("Area: " + str(radius*radius*math.pi))

for radius in range(5)
    print radius
    print("Circumference: "+str(2*radius*math.pi))
    if radius%2:
        print("Area: " + str(radius*radius*math.pi))

radius = 0
while radius >= 0:
    radius = int(raw_input("Radius: "))
    print radius
    if radius == 8:
        break
import sys

numbers = raw_input("Numbers: ")
numbers.split(" ")
numbers = sorted(numbers)
for number in numbers
    sys.stdout.write(number)
    if number!=+ numbers(-1):
            sys.stdout.write(", ")
print("\n")
    print puts a new line
numbers = raw_input("Numbers: ")
numbers = numbers.split(":")
offset = int(raw_input("Offset: "))

for i in range(len(numbers)):
    numbers(i) = int(numbers(i))

numbers(1) += offset
numbers(0) += numbers(1)/60
numbers(1) %= 60
numbers(0) %= 24
print str(numbers(0)+":"+str(numbers(1))
