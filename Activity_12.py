def ip_numbers():
    #to input numbers
    ip = input("input numbers: ")
    return ip

def greatest(a, b, c):
    #to compare three values
    if a >= b and a >= c:
        l = a
    elif b >= a and b >= c:
        l = b
    else:
        l = c
    return l

def display(l, a, b, c):
    #to display greatest of three numbers
    print(l, "is the greatest number among ", a, ",", b, "and", c)

def main():
    ip_line = ip_numbers()
    n = ip_line.split(' ')

    g = greatest(n[0], n[1], n[2])
    display(g, n[0], n[1], n[2])

main()
