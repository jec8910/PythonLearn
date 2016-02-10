import sys

numbers = raw_input("Enter three numbers separated by a space: ")
print numbers
numbers = numbers.split(" ")
numbers = [int(i) for i in numbers]
numbers = sorted(numbers)
for number in numbers:
    sys.stdout.write(str(number))
    if number!= numbers[-1]:
            sys.stdout.write(", ")
