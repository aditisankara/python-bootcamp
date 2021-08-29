input_line = input("enter three numbers: ")
n = input_line.split(' ')

#comparing the three numbers
if n[0] >= n[1] and n[0] >= n[2] :
    l = n[0]
    
elif n[1] >= n[0] and n[1] >= n[2] :
    l = n[1]
    
else :
    l = n[2]

print(l, "is the greatest among ", n[0], ",", n[1], "and", n[2])
