def input_numbers():
    '''to input two numbers'''
    x = int(input("first number = "))
    y = int(input("second number = "))
    return x, y

def add(x, y):
    '''addition of two numbers'''
    sum = x + y
    return sum

def display(x, y, sum):
    '''to display the addition of two numbers'''
    print(x, " + ", y, " = ", sum)
    
def main():
    a, b = input_numbers()
    summation = add(a, b)
    display(a, b, summation)

main()

