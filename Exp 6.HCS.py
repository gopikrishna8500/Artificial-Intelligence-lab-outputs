def hill_climbing(f, x0):

  x = x0 

  while True:

    neighbors = generate_neighbors(x)  

    best_neighbor = max(neighbors, key=f)  

    if f(best_neighbor) <= f(x):

      return x

    x = best_neighbor
