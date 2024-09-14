def dfs_iterative(graph, start_node):
    """
    Perform Depth-First Search (DFS) on a graph starting from a given node (iterative version).

    :param graph: A dictionary where keys are node names and values are lists of adjacent nodes
    :param start_node: The node from which DFS starts
    :return: List of nodes in the order they were visited
    """
    visited = set()
    stack = [start_node]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    
    return result

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    print("DFS (iterative) traversal order:", dfs_iterative(graph, start_node))
