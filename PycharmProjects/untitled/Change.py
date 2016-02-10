cents = raw_input("Enter a whole number from 1 to 99.\nThe machine will"
                  " determine a combination of coins.\n")
print cents, " cents in coins:"
cents = int(cents)
numQ = cents/25
cents = cents % 25
numD = cents/10
cents = cents%10
numN = cents/5
cents = cents%5
numP = cents
print numQ, " quarters\n", numD, " dimes\n", numN, "nickels\n", numP, \
    " pennies"
