new_string = input('Enter your string ')
string_len = len(new_string)
output = ''  # blank string for result

for i in range(string_len - 1, -1, -1):  # we go through the string from stop to start
    output += new_string[i]  # and add elements to output

print(output)
