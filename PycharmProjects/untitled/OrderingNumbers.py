import sys

numbers = raw_input("Numbers: ")
numbers.split(" ")
numbers = sorted(numbers)
for number in numbers:
    sys.stdout.write(number)
    if number!=+ numbers(-1):
            sys.stdout.write(", ")