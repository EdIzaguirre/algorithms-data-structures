# Data Structures and Algorithms

A repository I am making to implement common algorithms and data structures from scratch.

## Algorithms
### Binary Search
- Searches through an array by halving the size of the array on each iteration.
- Input: Array of size $n$
- Output: Index of found element $x$, or None
- Runtime: $O(\log n)$

### Quicksort
- Takes an unsorted array and sorts it by picking a pivot (in this case middle value) and recursively sorting the lower and upper halves of the array. 
- Input: Unsorted array
- Output: Sorted array
- Runtime: $O(n \log n)$ (average) or $O(n^2)$ (worst case), depends on pivot choice. 

### Breadth-First Search
- Searches through a graph for a particular node. Starts with an initial node, and works radially outward until desired node is found (if present).
- Input: Graph and initial node
- Output: True if desired node is found. False otherwise
- Runtime: $O(nodes + edges)$

## Data Structures
### Linked list
- A singly linked list of nodes, where each node contains a value and a reference to the next node.
- Contains functions such as size, add, remove at value, remove at index, and more. 


