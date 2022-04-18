def reverse_list(input_list):
    input_list.reverse()
    for item in input_list:
        if isinstance(item,list):
            reverse_list(item)
    return input_list

input_list = list(input())
print(reverse_list(input_list))