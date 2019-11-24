new_list = str.lower(input('Print your list '))
number_of_x = 0  # counter
number_of_o = 0  # counter

for i in new_list:
    if i == 'x':
        number_of_x += 1  
    elif i == 'o':
        number_of_o += 1
        
if number_of_x == number_of_o:  # number of x and o comparing
    print(True)
else:
    print(False)
