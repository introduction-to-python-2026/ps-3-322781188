def approximate_pi(n_terms):
       list_of_alternating_signs = []
       for i in range(n_terms):
           list_of_alternating_signs.append((-1)**i/(2*i+1)) 
       return 4*sum(list_of_alternating_signs)
