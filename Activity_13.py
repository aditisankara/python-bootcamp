n = int(input("enter the start number: "))
m = int(input("enter the end number: "))

i = n
while i <= m:
    if i % 2 != 0:
        print(i)
    i += 1
