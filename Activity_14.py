from math import sqrt

def is_prime(n):
    flag = 0
    for i in range(2,int((sqrt(n)+1))):
        if n % i == 0:
            flag = 1
            break
    if flag != 0 or n == 1:
        op = 'not a prime number'
    else:
        op = 'prime number'
    print(op)
            

def main():
    num = int(input("enter an integer: "))
    is_prime(num)

main()
