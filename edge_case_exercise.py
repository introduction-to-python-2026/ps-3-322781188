def move(my_list, direction=None):
    if 1 not in my_list:
        return my_list
    index_of_one = my_list.index(1)
    list_length = len(my list)

    if direction == 'right' and index_of_one + 1 < list_length:
        my list[index_of_one] = 0
        my list[index_of_one + 1] = 1

    elif direction == 'left' and index_of_one > 0:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
