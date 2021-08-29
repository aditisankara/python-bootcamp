import math

def ip_dimensions():
    l = float(input("length = "))
    b = float(input("breadth = "))
    h = float(input("height = "))
    return l, b, h

def volume(l, b, h):
    #finding value of k
    k = l**2 + b**2 + h**2
    #finding volume
    vol = (b**2) * (h**2) / (k**0.5)
    return vol

def radius(vol):
    #finding radius
    rad = (3*vol/(4*math.pi)) ** (1/3)
    return rad

def display_result(vol, rad):
    print("Volume of tromboloid = %.3f," %vol, "\nradius of sphere = %.3f" %rad)

def main():
    l, b, h = ip_dimensions()
    
    v = volume(l, b, h)
    r = radius(v)

    display_result(v, r)

main()
