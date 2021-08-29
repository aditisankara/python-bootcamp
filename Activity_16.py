import copy

ip_string = input("input string: ")
list_1 = ip_string.split(' ')

list_2 = copy.deepcopy(list_1)

#method 1 - list.sort()
list_1.sort()

#method 2 - sorted(list)
sorted_list_2 = sorted(list_2)

print("list_1 = ", list_1)
print("list_2 = ", list_2)
print("sorted_list_2 = ", sorted_list_2)
