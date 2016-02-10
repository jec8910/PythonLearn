numbers = raw_input("Enter a time in the format hours:minutes: ")
numbers = numbers.split(":")
offset = int(raw_input("Offset: "))

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[1] += offset
numbers[0] += numbers[1]/60
numbers[1] %= 60
numbers[0] %= 24
print str(numbers[0])+":"+str(numbers[1])