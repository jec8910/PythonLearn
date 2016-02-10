degF = raw_input("Enter a temperature in degrees Fahrenheit: ")
degF = float(degF)
print degF
degC = 5./9. * (degF - 32.)
# other option:
# degF = str(degF)
# degC = str(degC)
# print degF + " degrees Fahrenheit is " + degC + " degrees Celsius"
print degF, " degrees F is ", degC, " degrees C"