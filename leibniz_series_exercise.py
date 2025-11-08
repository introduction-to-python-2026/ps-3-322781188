def approximate_pi(n_terms):
  n_terms = 1000
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
