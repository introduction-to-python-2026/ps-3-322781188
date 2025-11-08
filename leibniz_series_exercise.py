def approximate_pi(n_terms):
    list_of_numbers = []
    numerator = -1
    denominator = -1
    pi_sum = 0
    for i in range(n_terms):
      numerator *= -1
      denominator += 2
      leibniz = numerator / denominator
      list_of_numbers.append(leibniz)
      pi_sum += leibniz
    return (pi_sum *4)
