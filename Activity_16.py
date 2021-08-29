import copy

def make_lists():
    #to input string and create the lists
    ip_string = input("input string: ")
    list_1 = ip_string.split(' ')
    list_2 = copy.deepcopy(list_1)
    return list_1, list_2

def sort_lists(list_1, list_2):
    #method 1 - list.sort()
    list_1.sort()
    #method 2 - sorted(list)
    sorted_list_2 = sorted(list_2)
    return sorted_list_2
    
def display_lists(list_1, list_2, sorted_list_2):
    print("list_1 = ", list_1)
    print("list_2 = ", list_2)
    print("sorted_list_2 = ", sorted_list_2)

def main():
    l1, l2 = make_lists()
    sl_2 = sort_lists(l1, l2)
    display_lists(l1, l2, sl_2)

main()
