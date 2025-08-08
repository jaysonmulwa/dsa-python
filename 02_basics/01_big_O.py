"""
Big O Notation
=======================
Big O notation is a mathematical notation used to describe the upper bound of an algorithm's time or space complexity. It provides a high-level understanding of how the performance of an algorithm scales with the size of the input data.
It is particularly useful for comparing the efficiency of different algorithms and understanding their scalability.
Big O notation is expressed as O(f(n)), where f(n) is a function that describes the growth rate of the algorithm's time or space complexity as the input size n increases.
Big O notation is not concerned with the exact number of operations or the specific time taken, but rather with how the performance grows relative to the input size.

Common Big O Notations
========================
- O(1): Constant time complexity. The algorithm's performance does not change with the size of the input data.
- O(log n): Logarithmic time complexity. The algorithm's performance grows logarithmically with the size of the input data.
- O(n): Linear time complexity. The algorithm's performance grows linearly with the size of the input data.
- O(n log n): Linearithmic time complexity. The algorithm's performance grows in a combination of linear and logarithmic factors.
- O(n^2): Quadratic time complexity. The algorithm's performance grows quadratically with the size of the input data.
- O(2^n): Exponential time complexity. The algorithm's performance grows exponentially with the size of the input data.
- O(n!): Factorial time complexity. The algorithm's performance grows factorially with the size of the input data.
- O(n^k): Polynomial time complexity. The algorithm's performance grows polynomially with the size of the input data, where k is a constant.
- O(sqrt(n)): Square root time complexity. The algorithm's performance grows with the square root of the size of the input data.
- O(n^3): Cubic time complexity. The algorithm's performance grows cubically with the size of the input data.

Rules for Big O Notation
=======================
1. Ignore constant factors: When analyzing the time complexity, we focus on the highest-order term and ignore constant factors. 
    For example, O(2n) is simplified to O(n).
2. Ignore lower-order terms: When analyzing the time complexity, we focus on the highest-order term and ignore lower-order terms. 
    For example, O(n + log n) is simplified to O(n).
3. Use the worst-case scenario: Big O notation describes the upper bound of an algorithm's performance, so we consider the worst-case scenario when analyzing time complexity.
4. Focus on the input size: Big O notation describes how the performance of an algorithm scales with the size of the input data, so we focus on the input size n when analyzing time complexity.

Theta and Omega Notation
========================
Theta (Θ) notation describes the tight bound of an algorithm's time or space complexity. It provides both an upper and lower bound, indicating that the algorithm's performance grows at a specific rate.
Omega (Ω) notation describes the lower bound of an algorithm's time or space complexity. It indicates that the algorithm's performance will not grow slower than a certain rate.

"""


"""
Cheat Sheet for Big O Notation
========================
"""
"""
# Search Algorithms
Binary Search: O(log n)
Linear Search: O(n)

# Sorting Algorithms
-> Simple comparison-based sorting algorithms:
Bubble Sort: O(n^2)
Selection Sort: O(n^2)
Insertion Sort: O(n^2)

-> Divide and conquer sorting algorithms: 
-> Solve sub problems and combine results
Merge Sort: O(n log n)
Quick Sort: O(n log n)
Heap Sort: O(n log n)
Counting Sort: O(n + k) where k is the range of the input data
Radix Sort: O(nk) where k is the number of digits in the largest number
Bucket Sort: O(n + k) where k is the number of buckets

# Data Structures
Array Access: O(1)
Array Insertion: O(n)
Array Deletion: O(n)

Linked List Access: O(n)
Linked List Insertion: O(1) (if inserting at the head)
Linked List Deletion: O(1) (if deleting the head)

Stack Push: O(1)
Stack Pop: O(1)

Queue Enqueue: O(1)
Queue Dequeue: O(1)

# Hash Table Access: O(1) on average
Hash Table Insertion: O(1) on average
Hash Table Deletion: O(1) on average

# Tree Traversal
Binary Tree Inorder Traversal: O(n)
Binary Tree Preorder Traversal: O(n)
Binary Tree Postorder Traversal: O(n)

# Graph Traversal
Depth-First Search (DFS): O(V + E) where V is the number of vertices and E is the number of edges
Breadth-First Search (BFS): O(V + E) where V is the number of vertices and E is the number of edges

Dijkstra's Algorithm: O((V + E) log V) using a priority queue
Floyd-Warshall Algorithm: O(V^3) 
Bellman-Ford Algorithm: O(VE)
Prim's Algorithm: O(E log V) using a priority queue
Kruskal's Algorithm: O(E log E) or O(E log V) using a union-find data structure
Floyd-Warshall Algorithm: O(V^3)
A* Search Algorithm: O(E) where E is the number of edges in the graph

# Fibonacci Sequence
Fibonacci Recursive: O(2^n)
Fibonacci Iterative: O(n)
Fibonacci Dynamic Programming: O(n)
Fibonacci Matrix Exponentiation: O(log n)
Fibonacci Space Optimized: O(1)
Fibonacci Binet's Formula: O(1)

"""



