print("input numbers")
input_line = input()
number_list = input_line.split(' ')
sum = 0
for i in number_list:
    sum = sum + int(i)
print("Sum of all the numbers is = %d" %(sum))
