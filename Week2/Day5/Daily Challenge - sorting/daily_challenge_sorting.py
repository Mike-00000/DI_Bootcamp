

input_string = input("Write a comma separated sequence of words")
input_string_no_space = input_string.replace(" ", "")
list_string  = input_string_no_space.split(",")
list_string.sort()
for name in list_string:
    print(name)