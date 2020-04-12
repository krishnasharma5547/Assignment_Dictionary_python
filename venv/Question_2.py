d1 = {}
d2 = {}

# Storing values using loop ==>>
for i in range(1,6):
    cm = i * 100
    d1[i] = cm
    d2[cm] = i
print("Meters to Centimeters: ")
print(d1)
print("Centimeters to Meters: ")
print(d2)