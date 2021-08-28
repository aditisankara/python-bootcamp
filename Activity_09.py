l = float(input("l = "))
b = float(input("b = "))
h = float(input("h = "))

'''finding value of k'''
k = l**2 + b**2 + h**2

'''finding volume'''
vol = (b**2) * (h**2) / (k**0.5)

print("volume = ", end = "")
print('%.3f' %vol)

'''finding radius'''
r = (3*vol/(4*3.142)) ** (1/3)

print("radius = ", end = "")
print('%.3f' %r)

