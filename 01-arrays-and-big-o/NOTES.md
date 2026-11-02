# Arrays & Big-O

## Part 1: Big-O

Big-O describes how an algorithm's cost **grows as input size n grows**. It ignores constants and lower-order terms.

- `3n + 10` → O(n)
- `n² + 50n` → O(n²)

### How to find it
- A single loop over n items → O(n)
- Nested loops over n → O(n²)
- Halving the problem each step → O(log n)
- Loop that does O(log n) work per item → O(n log n)
- Sequential steps **add**, nested steps **multiply**: `O(n) + O(n²)` → O(n²)

### Example

```python
def has_duplicate(nums):          # O(n) time, O(n) space
    seen = set()
    for x in nums:                # n iterations
        if x in seen:             # O(1) average
            return True
        seen.add(x)
    return False
```

Brute force would compare every pair: O(n²) time, O(1) space. Here you trade space for time.

### Time vs Space
Count the **extra** memory you allocate (sets, new arrays, recursion stack), not the input itself.

### Best / Average / Worst
Usually quote the worst case. Searching for `x` in a list: best O(1) (first element), worst O(n).

### Amortized cost
Appending to a dynamic array is O(1) **amortized**: most appends are cheap, an occasional resize costs O(n), but averaged over many appends it is O(1).

---

## Part 2: Arrays

An array stores elements in **contiguous memory**. Because every element has the same size, the address of `arr[i]` is `base + i * size`, which is why indexing is O(1).

| Operation | Cost | Why |
|---|---|---|
| Read / write `arr[i]` | O(1) | Direct address calculation |
| Append at end | O(1) amortized | May trigger resize |
| Insert at index i | O(n) | Shift elements right |
| Delete at index i | O(n) | Shift elements left |
| Search (unsorted) | O(n) | Must scan |
| Search (sorted) | O(log n) | Binary search |

**Static array:** fixed size (C, Java `int[]`).
**Dynamic array:** grows automatically (Python `list`, Java `ArrayList`, C++ `vector`). When full, it allocates a bigger block (usually 2x), copies everything over, and frees the old one.

### Python notes
- Python `list` is a dynamic array of references.
- `list.append`, `list.pop()` → O(1). `list.insert(0, x)`, `list.pop(0)` → O(n).
- Slicing `a[i:j]` creates a copy → O(j - i).
- `x in list` → O(n). `x in set` → O(1) average.

---

## Part 3: Array Patterns to Know

1. **Two pointers**: one pointer at each end (or both moving the same way). Great for sorted arrays and in-place edits.
2. **Sliding window**: maintain a window `[l, r]` and update the running value instead of recomputing it.
3. **Prefix sums**: precompute `prefix[i] = sum(arr[:i])` so any range sum is O(1).
4. **Hash map lookup**: turn "find a pair" from O(n²) into O(n) (Two Sum).
5. **In-place modification**: overwrite using a write pointer to avoid O(n) extra space.
6. **Sorting first**: many problems get easier once sorted (O(n log n) cost).

---

## Part 4: Common Pitfalls
- Off-by-one errors in loop bounds; test with arrays of length 0, 1 and 2.
- Modifying a list while iterating over it.
- Forgetting that slicing and `in list` hide O(n) costs.
- Not asking whether the array is sorted, whether it has duplicates, or whether it can be empty.

---

## Part 5: Learning Checklist
- [ ] Explain why `arr[i]` is O(1) but insert is O(n)
- [ ] Explain amortized O(1) append
- [ ] Run `dynamic_array.py` and read through the implementation
- [ ] Solve every problem in `practice.py` (run it to check)
- [ ] For each solution, state the time and space complexity out loud
