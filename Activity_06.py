'''prompt for input'''
input_line = input("input numbers: ")

'''creating a list from the input'''
numbers = input_line.split(' ')

'''creating sliced list'''
sliced_list = numbers[0:3]

'''length of list'''
n = len(numbers)
  
print(f'sliced list = {sliced_list}')

'''replacement of first and last elements with 0'''
rep_list_1 = numbers
rep_list_1[0] = 0
rep_list_1[n-1] = 0

rep_list_2 = sliced_list
rep_list_2[0] = 0
rep_list_2[2] = 0

print(f'replaced list-1 = {rep_list_1}')
print(f'replaced list-2 = {rep_list_2}')

