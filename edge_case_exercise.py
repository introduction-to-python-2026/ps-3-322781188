def move(my_list, direction):
  list_count = len(my_list)
  index_of_one = my_list.index(1)
  if direction == "right":
    if index_of_one == (list_count -1):
      my_list [list_count-1] = 1
    else:
      my_list[index_of_one] = 0
      my_list[index_of_one + 1] = 1
  elif direction == "left":
    if index_of_one == 0:
      my_list [0] = 1
    else:
      my_list[index_of_one] = 0
      my_list[index_of_one - 1] = 1
  return my_list
