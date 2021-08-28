input_line = input()
number_list = input_line.split(' ')
sum = 0
for i in number_list:
    sum = sum + int(i)
print(sum)
