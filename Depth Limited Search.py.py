def depth_limited_search(graph, start, goal, limit):
    def dls(node, goal, depth):
        if depth == 0:
            return 'cutoff'
        elif node == goal:
            return 'success'
        else:
            cutoff_occurred = False
            for neighbor in graph[node]:
                result = dls(neighbor, goal, depth-1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result != 'failure':
                    return result
            if cutoff_occurred:
                return 'cutoff'
            else:
                return 'failure'
    return dls(start, goal, limit)

# Example usage:
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E','F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}
start = 'A'
goal = 'J'
limit = 3

result = depth_limited_search(graph, start, goal, limit)
print(result)
