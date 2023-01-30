import random
import math

def simulated_annealing(cities, initial_temp, cooling_rate, max_iterations):
    current_path = random.sample(cities, len(cities))
    current_cost = calculate_cost(current_path)
    best_path = current_path
    best_cost = current_cost
    temp = initial_temp

    for i in range(max_iterations):
        next_path = get_neighbor(current_path)
        next_cost = calculate_cost(next_path)
        delta_cost = next_cost - current_cost
        if delta_cost < 0:
            current_path = next_path
            current_cost = next_cost
            if current_cost < best_cost:
                best_path = current_path
                best_cost = current_cost
        else:
            acceptance_probability = math.exp(-delta_cost / temp)
            if random.random() < acceptance_probability:
                current_path = next_path
                current_cost = next_cost
        temp = temp * cooling_rate

    return best_path, best_cost

def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += dist(path[i], path[i + 1])
    cost += dist(path[-1], path[0])
    return cost

def get_neighbor(path):
    new_path = path.copy()
    x = random.randint(0, len(path) - 1)
    y = random.randint(0, len(path) - 1)
    new_path[x], new_path[y] = new_path[y], new_path[x]
    return new_path

def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


cities = [(0, 0), (1, 2), (2, 2), (3, 3), (1, 4), (2, 5)]
initial_temp = 100
cooling_rate = 0.99
max_iterations = 1000

best_path, best_cost = simulated_annealing(cities, initial_temp, cooling_rate, max_iterations)

print("Best path: ", best_path)
print("Best cost: ", best_cost)
