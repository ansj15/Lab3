# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10AyeAL4L8nguoxHQrCkmrBzIXTqV94lA
"""

from collections import deque

def find_shortest_path(grid, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (new_x, new_y) not in visited:
                if grid[new_x][new_y] == 0:
                    queue.append(((new_x, new_y), path + [(new_x, new_y)]))
                    visited.add((new_x, new_y))
    return []

grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (1, 1)
end = (4, 4)
path = find_shortest_path(grid, start, end)
print("Shortest Path:", path)

import time
def print_grid(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("------")

def get_neighbors(state):
    neighbors = []
    zero_index = state.index("0")
    row, col = divmod(zero_index, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r, c in moves:
        new_row, new_col = row + r, col + c
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            neighbors.append("".join(new_state))
    return neighbors

def depth_limited_search(state, goal, depth, visited):
    if state == goal:
        return [state]
    if depth == 0:
        return None

    visited.add(state)
    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result = depth_limited_search(neighbor, goal, depth - 1, visited)
            if result:
                return [state] + result
    return None

def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        result = depth_limited_search(start, goal, depth, visited)
        if result:
            return result, len(visited)
    return None, 0
def main():
    start_state = input("Enter start State: ")
    goal_state = input("Enter goal State: ")
    print("IDDFS Algorithm")
    start_time = time.time()
    max_depth = 20
    path, nodes_visited = iddfs(start_state, goal_state, max_depth)
    end_time = time.time()

    if path:
        print(f"Time taken: {end_time - start_time} seconds")
        print(f"Path Cost: {len(path) - 1}")
        print(f"No of Nodes Visited: {nodes_visited}")
        print("-----------------")
        for state in path:
            print_grid(state)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()

from collections import defaultdict

class findpath:
    def __init__(self, graph_structure):
        self.graph_structure = graph_structure

    def findNeighbors(self, node):
        return self.graph_structure[node]

    def heuristic(self, node):
        heuristic_values = {
            "The": 4,
            "cat": 3,
            "dog": 3,
            "runs": 2,
            "fast": 1
        }
        return heuristic_values[node]

    def a_search(self, start, goal):
        openSet = set([start])
        closedSet = set([])

        startCost = {}
        startCost[start] = 0

        predecessors = {}
        predecessors[start] = None

        while len(openSet) > 0:
            currentNode = None
            for node in openSet:
                if currentNode is None or startCost[node] + self.heuristic(node) < startCost[currentNode] + self.heuristic(currentNode):
                    currentNode = node

            if currentNode is None:
                print("Path does not exist!")
                return None

            if currentNode == goal:
                path = []
                while currentNode is not None:
                    path.append(currentNode)
                    currentNode = predecessors[currentNode]
                path.reverse()

                print("Sentence:", " -> ".join(path))
                print("Total cost:", startCost[goal])
                return path

            for (neighbor, travel_cost) in self.findNeighbors(currentNode):
                if neighbor not in openSet and neighbor not in closedSet:
                    openSet.add(neighbor)
                    predecessors[neighbor] = currentNode
                    startCost[neighbor] = startCost[currentNode] + travel_cost
                else:
                    if startCost[neighbor] > startCost[currentNode] + travel_cost:
                        startCost[neighbor] = startCost[currentNode] + travel_cost
                        predecessors[neighbor] = currentNode

                        if neighbor in closedSet:
                            closedSet.remove(neighbor)
                            openSet.add(neighbor)

            openSet.remove(currentNode)
            closedSet.add(currentNode)

        print("Path not exist!")
        return None


graph_structure = {
    "The": [("cat", 1), ("dog", 2)],
    "cat": [("runs", 2)],
    "dog": [("runs", 2)],
    "runs": [("fast", 1)],
    "fast": []
}

findpath = findpath(graph_structure)
findpath.a_search("The", "fast")