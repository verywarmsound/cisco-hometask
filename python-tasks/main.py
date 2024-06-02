from typing import List
from collections import Counter
import re

# Task 1: Define the GNode interface
class GNode:
    def getName(self) -> str:
        pass

    def getChildren(self) -> List['GNode']:
        pass

# Task 1: Implement the walkGraph function
def walkGraph(node: GNode) -> List[GNode]:
    visited = set()
    result = []

    def dfs(current_node: GNode):
        if current_node in visited:
            return
        visited.add(current_node)
        result.append(current_node)
        for child in current_node.getChildren():
            dfs(child)

    dfs(node)
    return result

# Task 2: Implement the paths function
def paths(node: GNode) -> List[List[GNode]]:
    all_paths = []

    def dfs(current_node: GNode, path: List[GNode]):
        path.append(current_node)
        if not current_node.getChildren():
            all_paths.append(path.copy())
        else:
            for child in current_node.getChildren():
                dfs(child, path)
        path.pop()

    dfs(node, [])
    return all_paths

# Example usage
class ExampleGNode(GNode):
    def __init__(self, name):
        self.name = name
        self.children = []

    def getName(self) -> str:
        return self.name

    def getChildren(self) -> List[GNode]:
        return self.children

# Constructing the example graph
A = ExampleGNode('A')
B = ExampleGNode('B')
C = ExampleGNode('C')
E = ExampleGNode('E')
F = ExampleGNode('F')
G = ExampleGNode('G')
H = ExampleGNode('H')
I = ExampleGNode('I')
D = ExampleGNode('D')
J = ExampleGNode('J')

A.children = [B, C, D]
B.children = [E, F]
C.children = [G, H, I]
D.children = [J]

# Task 1: Testing walkGraph
def test_walkGraph():
    print("walkGraph(A):")
    for node in walkGraph(A):
        print(node.getName(), end=" ")
    print()

# Task 2: Testing paths
def test_paths():
    print("\npaths(A):")
    for path in paths(A):
        print(" -> ".join(node.getName() for node in path))

# Task 3: Quick and dirty word count program
def count_words(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    sorted_word_counts = word_counts.most_common()
    for word, count in sorted_word_counts:
        print(f"{count} {word}")

if __name__ == '__main__':
    # Task 1
    test_walkGraph()
    # Task 2
    test_paths()
    # Task 3
    print("\nWord count in 'input.txt':")
    count_words('input.txt')
