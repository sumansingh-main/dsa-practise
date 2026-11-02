# Data Structures & Algorithms — Core Concepts

A quick-reference guide to the most important DSA concepts.

## 1. Complexity Analysis (Big-O)

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | Array index access, hash lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2ⁿ) | Exponential | Naive recursive Fibonacci |
| O(n!) | Factorial | Permutations |

Always consider **time** and **space** complexity, and best / average / worst cases.

## 2. Core Data Structures

| Structure | Access | Search | Insert | Delete | Notes |
|---|---|---|---|---|---|
| Array | O(1) | O(n) | O(n) | O(n) | Contiguous memory |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | *Given node reference |
| Stack (LIFO) | O(n) | O(n) | O(1) | O(1) | Undo, DFS, parentheses matching |
| Queue (FIFO) | O(n) | O(n) | O(1) | O(1) | BFS, scheduling |
| Hash Table | – | O(1) avg | O(1) avg | O(1) avg | Collisions: chaining / open addressing |
| Binary Search Tree | O(log n) avg | O(log n) | O(log n) | O(log n) | O(n) if unbalanced |
| Heap | – | O(n) | O(log n) | O(log n) | Priority queue; peek min/max O(1) |
| Trie | – | O(L) | O(L) | O(L) | Prefix search; L = word length |
| Graph | – | – | – | – | Adjacency list / matrix |

## 3. Searching & Sorting

**Searching**
- Linear search — O(n)
- Binary search — O(log n), requires sorted data

**Sorting**

| Algorithm | Best | Average | Worst | Stable | Space |
|---|---|---|---|---|---|
| Bubble / Insertion / Selection | O(n)/O(n)/O(n²) | O(n²) | O(n²) | B,I: yes | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | Yes | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | No | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | No | O(1) |
| Counting / Radix | O(n+k) | O(n+k) | O(n+k) | Yes | O(n+k) |

## 4. Common Algorithmic Patterns

- **Two Pointers** — sorted arrays, pair sums, palindromes
- **Sliding Window** — subarray/substring problems with a moving range
- **Fast & Slow Pointers** — cycle detection in linked lists
- **Prefix Sum** — fast range-sum queries
- **Binary Search on Answer** — minimize/maximize a feasible value
- **Divide and Conquer** — split, solve, combine (merge sort)
- **Backtracking** — explore + undo (N-Queens, permutations, subsets)
- **Greedy** — locally optimal choices (interval scheduling, Huffman)
- **Dynamic Programming** — overlapping subproblems + optimal substructure
- **Monotonic Stack/Queue** — next greater element, sliding window max

## 5. Recursion & Dynamic Programming

**Recursion checklist:** base case → recursive case → progress toward base case.

**DP approach:**
1. Define the state (what does `dp[i]` mean?)
2. Write the recurrence relation
3. Set base cases
4. Choose top-down (memoization) or bottom-up (tabulation)
5. Optimize space if possible

Classic problems: Fibonacci, Climbing Stairs, 0/1 Knapsack, Longest Common Subsequence, Longest Increasing Subsequence, Coin Change, Edit Distance.

```python
# Bottom-up Fibonacci, O(n) time, O(1) space
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

## 6. Trees

- **Traversals:** Inorder (L-Root-R, sorted for BST), Preorder, Postorder, Level-order (BFS)
- **Balanced trees:** AVL, Red-Black — guarantee O(log n)
- **Key problems:** height, diameter, LCA, validate BST, serialize/deserialize

```python
def inorder(node):
    if node:
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)
```

## 7. Graphs

- **Representations:** adjacency list (sparse), adjacency matrix (dense)
- **BFS** — shortest path in unweighted graphs, level traversal (queue)
- **DFS** — connectivity, cycle detection, topological sort (stack/recursion)
- **Dijkstra** — shortest path, non-negative weights, O((V+E) log V)
- **Bellman-Ford** — handles negative weights, O(VE)
- **Floyd-Warshall** — all-pairs shortest path, O(V³)
- **Minimum Spanning Tree** — Kruskal (Union-Find), Prim (heap)
- **Topological Sort** — ordering in a DAG (Kahn's / DFS)
- **Union-Find (DSU)** — connected components, near O(1) operations

```python
from collections import deque

def bfs(graph, start):
    seen, q = {start}, deque([start])
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return seen
```

## 8. Problem-Solving Strategy

1. Understand the problem; restate it and clarify constraints
2. Work through small examples and edge cases (empty, single element, duplicates)
3. Start with brute force, then identify the bottleneck
4. Pick a pattern or data structure to optimize
5. Code it cleanly
6. Test with examples and analyze complexity

## 9. Suggested Learning Path

1. Big-O, arrays, strings
2. Hash maps, stacks, queues
3. Linked lists, recursion
4. Sorting & binary search
5. Trees & heaps
6. Graphs (BFS/DFS)
7. Dynamic programming & greedy
8. Advanced: tries, segment trees, union-find

## Practice Resources

- LeetCode (Blind 75 / NeetCode 150)
- HackerRank, Codeforces, GeeksforGeeks
- *Introduction to Algorithms* (CLRS)
