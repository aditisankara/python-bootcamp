input_line = input("input numbers: ")
numbers = input_line.split(' ')

sum = 0
for i in numbers:
    sum = sum + int(i)

s = f'{numbers[0]} + {numbers[1]} = {sum}'
print(s)
