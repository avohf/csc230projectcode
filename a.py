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
    #exits if the start is the end 
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

round_trip_paths = []
for path_to_D in paths_to_D:
    for path_from_D in paths_from_D_to_A:
        # Combine paths while avoiding to duplicate the node D by slicing the first index of path_from_D
        round_trip_path = path_to_D + path_from_D[1:]
        round_trip_length = calculate_path_length(graph, round_trip_path)
        round_trip_paths.append((round_trip_path, round_trip_length))


# Initialize variables to store the shortest path and its length
# Assume the first path is the shortest initially
shortest_round_trip_path = round_trip_paths[0][0]  # The first path
shortest_round_trip_length = round_trip_paths[0][1]  # The length of the first path

# Iterate over all round trip paths to find the one with the smallest length
for path, length in round_trip_paths:
    if length < shortest_round_trip_length:
        shortest_round_trip_path = path
        shortest_round_trip_length = length

# Output the shortest path and its length
print(f"The shortest path from A to D and back to A is {' -> '.join(shortest_round_trip_path)} with a total length of {shortest_round_trip_length}.")
