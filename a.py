# Create a graph with the distances shown on the diagram
graph = {
    'A': {'B': 10, 'C': 5, 'D': 11},
    'B': {'A': 10, 'D': 8},
    'C': {'A': 5, 'D': 7},
    'D': {'A': 13, 'C': 7, 'B': 8}
}

# Function to find all paths between two nodes in a graph
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    #exits if the start is the end ie. one node
    if start == end:
        return [path]
    #returns empty as there is no start
    if start not in graph:
        return []
    paths = []
    #iterates through each node thats connected to the starting point
    for node in graph[start]:
        if node not in path:  # checks if node isnt in the current path
            #recursively searches for paths from current node until it reaches the end node
            newpaths = find_all_paths(graph, node, end, path)
            paths.extend(newpaths)
    return paths

# Function to calculate the total length of a path
def calculate_path_length(graph, path):
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i]][path[i + 1]]
    return length

# Find all paths from A to D and from D to A
paths_to_D = find_all_paths(graph, 'A', 'D')
paths_from_D_to_A = find_all_paths(graph, 'D', 'A')

# Combine paths to find the round trips and their lengths
round_trip_paths = [(path_to_D + path_from_D[1:], calculate_path_length(graph, path_to_D + path_from_D[1:]))
                    for path_to_D in paths_to_D for path_from_D in paths_from_D_to_A]

# Find the shortest round trip path and its length
shortest_round_trip_path, shortest_round_trip_length = min(round_trip_paths, key=lambda x: x[1])

# Output the shortest path and its length
print(f"The shortest path from A to D and back to A is {' -> '.join(shortest_round_trip_path)} with a total length of {shortest_round_trip_length}.")