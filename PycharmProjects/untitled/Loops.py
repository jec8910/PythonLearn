import math

for radius in range(5):
    print("Circumference: "+str(2*radius*math.pi))
    print("Area: " + str(radius*radius*math.pi))

for radius in range(5):
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
