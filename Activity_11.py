def input_number():
    #to input a number
    x = int(input("enter number: "))
    return x

def add(x, y):
    #addition of two numbers
    sum = x + y
    return sum

def display(x, y, sum):
    #to display the addition of two numbers
    print(x, " + ", y, " = ", sum)
    
def main():
    a = input_number()
    b = input_number()
    summation = add(a, b)
    display(a, b, summation)
    
    
main()

