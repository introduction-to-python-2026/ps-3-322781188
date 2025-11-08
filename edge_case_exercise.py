def move(my_list, direction=None):
    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
      if index_of_one == len(my_list) - 1 :
        return my_list 
      else :
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
    elif direction == 'left':
      if index_of_one == 0 :
        return my_list 
      else :
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
    the_pig_location = [0, 0, 0, 1, 0, 0]
    print(move(the_pig_location, "right"))  



def pay():
  n_terms = 10
  list_of_numbers = []
  for i in range(n_terms):
      if i % 2 != 0:
          list_of_numbers.append(-1)
      else:
       list_of_numbers.append(1)
  odd = 3 
  for i in range(1, n_terms):
      list_of_numbers[i] = list_of_numbers[i] / odd
      odd += 2
  tozaa = 4*sum(list_of_numbers)

  return tozaa
