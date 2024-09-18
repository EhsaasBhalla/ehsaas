def split_func(string_input, split_input):
    if split_input == None or '\n':
        split_input = " "
    return split_index_func(string_input, split_input)


def split_index_func(string_input_1, split_input_1):
    split_index = []
    for i in range(len(string_input_1)):
        if i == 0:
            split_index.append(i)
        if string_input_1[i] == split_input_1:
            split_index.append(i)
        if i == len(string_input_1) - 1:
            split_index.append(i + 1)
    return split_list(string_input_1, split_index)


def split_list(string_input_2, split_index_input):
    split_string = []
    for i in range(len(split_index_input)):
        if i == len(split_index_input) - 1:
            break
        if i != 0:
            split_string.append(string_input_2[split_index_input[i] + 1:split_index_input[i + 1]])
        else:
            split_string.append(string_input_2[split_index_input[i]:split_index_input[i + 1]])
    return split_string


string = input("Enter the string: ")
split_char = input("Enter the character with which you want to split: ")
splitted_string = split_func(string, split_char)
print(splitted_string)
