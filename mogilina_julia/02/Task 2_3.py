array = list(input('Print your array '))
new_list = []  # create new list for results
output = ''

for i in array:
    if i  not in new_list:  # if our element not in list we add it
        new_list.append(i)
    else:
        for j in range(len(new_list)):
            if new_list[j] == i:  # if element already in new list 
                new_list[j] = ''  # we remove it with blank space  
                break
            
for k in new_list:
    output += k  # add elements to output 

print(output)
