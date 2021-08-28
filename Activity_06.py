input_line = input("input numbers: ")
numbers = input_line.split(' ')
sliced_list = numbers[0:3]

for i in range(3):
    sliced_list[i] = int(sliced_list[i])
  
print(f'sliced list = {sliced_list}')

rep_list_1 = numbers
rep_list_1[0] = 0
rep_list_1[4] = 0

rep_list_2 = sliced_list
rep_list_2[0] = 0
rep_list_2[2] = 0

for i in range(5):
    rep_list_1[i] = int(rep_list_1[i])

for i in range(3):
    rep_list_2[i] = int(rep_list_2[i])

print(f'replaced list-1 = {rep_list_1}')
print(f'replaced list-2 = {rep_list_2}')

