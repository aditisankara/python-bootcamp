def ip_range():
    #to input start and end of range
    a = int(input("enter the start number: "))
    b = int(input("enter the end number: "))
    return a, b

def disp_odd_numbers(a, b):
    #to display odd numbers between a and b
    odd_numbers = [*range(a, b+1, 2)]
    print(*odd_numbers, sep = "\n")

def main():
    n, m = ip_range()

    if n % 2 == 0:
        n = n + 1

    disp_odd_numbers(n, m)

main()
