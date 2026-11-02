"""
PROBLEM 10: Subarray Sum Equals K                               [Medium/Hard]
-----------------------------------------------------------------------
Given a list of integers (which may include negatives and zeros) and an
integer k, return the NUMBER of contiguous subarrays whose sum equals k.

    subarray_sum_equals_k([1, 1, 1], 2)     -> 2   ([1,1] at two positions)
    subarray_sum_equals_k([1, 2, 3], 3)     -> 2   ([1,2] and [3])
    subarray_sum_equals_k([1, -1, 0], 0)    -> 3   ([1,-1], [0], [1,-1,0])

Target: O(n) time, O(n) space.      Pattern: prefix sum + hash map

Run:  python problem10_subarray_sum_equals_k.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES
# =======================================================================
# Brute force: for every (start, end), sum the slice -> O(n^2) or O(n^3).
# Sliding window does NOT work here, because negatives break the
# "grow window = bigger sum" assumption.
#
# PREFIX SUM: prefix[j] = nums[0] + ... + nums[j-1]   (prefix[0] = 0)
#   The sum of the subarray nums[i..j-1] = prefix[j] - prefix[i].
#
# We want that difference to equal k:
#       prefix[j] - prefix[i] = k   <=>   prefix[i] = prefix[j] - k
#
# So while scanning left to right with a running total:
#   - at each step, the number of valid subarrays ENDING here equals the
#     number of EARLIER prefix sums that were equal to (total - k).
#   - store a DICT: prefix sum -> how many times we've seen it.
#
# IMPORTANT: seed the dict with {0: 1}. It represents the empty prefix and
# lets subarrays that start at index 0 be counted.
#
# Useful syntax:
#   counts = {0: 1}
#   counts.get(key, 0)               # count or 0 if never seen
#   counts[total] = counts.get(total, 0) + 1
#   from collections import defaultdict   # dict with a default value
#   counts = defaultdict(int)             # missing keys start at 0
#
# HINT 1: Per element: update `total`, add counts[total - k] to the answer,
#         THEN record `total` in the dict. Why in that order?
# HINT 2: Trace [1, -1, 0] with k=0 on paper. Watch how the dict changes.
# =======================================================================


def subarray_sum_equals_k(nums, k):
    pass  # <-- your code here


# ----------------------------------------------------------------- tests
def _run_tests():
    cases = [
        (([1, 1, 1], 2), 2),
        (([1, 2, 3], 3), 2),
        (([1, -1, 0], 0), 3),
        (([], 0), 0),
        (([3], 3), 1),
        (([3], 4), 0),
        (([0, 0, 0], 0), 6),
        (([-1, -1, 1], 0), 1),
        (([1, 2, 1, 2, 1], 3), 4),
    ]
    passed = 0
    for (nums, k), expected in cases:
        got = subarray_sum_equals_k(list(nums), k)
        ok = got == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {nums}, k={k}" + ("" if ok else f"  got={got!r} expected={expected!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
