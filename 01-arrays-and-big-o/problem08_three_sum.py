"""
PROBLEM 8: 3Sum                                                 [Medium]
-----------------------------------------------------------------------
Return all UNIQUE triplets [a, b, c] from `nums` such that a + b + c == 0.
The result must not contain duplicate triplets. Order doesn't matter.

    three_sum([-1, 0, 1, 2, -1, -4])  -> [[-1, -1, 2], [-1, 0, 1]]
    three_sum([0, 0, 0])              -> [[0, 0, 0]]
    three_sum([1, 2, 3])              -> []

Target: O(n^2) time.                Pattern: sort + two pointers

Run:  python problem08_three_sum.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES
# =======================================================================
# Brute force: three nested loops -> O(n^3), plus de-duplication pain.
#
# Plan:
#   1. SORT the list (O(n log n)). Sorting makes duplicates adjacent and
#      lets us use two pointers.
#   2. Fix the first number nums[i] (the "anchor").
#   3. Now it's Two Sum on the rest: find l < r with
#          nums[l] + nums[r] == -nums[i]
#      using pointers l = i + 1 and r = len - 1:
#          sum too small  -> l += 1   (need a bigger number)
#          sum too big    -> r -= 1   (need a smaller number)
#          sum == 0       -> record the triplet, then move on
#
# TWO POINTERS works on a SORTED list because moving a pointer changes
# the sum in a predictable direction.
#
# AVOIDING DUPLICATES (the tricky part):
#   - Skip an anchor if it equals the previous anchor:
#         if i > 0 and nums[i] == nums[i - 1]: continue
#   - After recording a triplet, advance l past equal values:
#         l += 1
#         while l < r and nums[l] == nums[l - 1]: l += 1
#
# Useful syntax:
#   nums.sort()                      # sorts in place, O(n log n)
#   sorted(nums)                     # returns a new sorted list
#   continue                         # skip to the next loop iteration
#   result.append([a, b, c])
#
# HINT 1: The anchor loop only needs to run up to len(nums) - 2. Why?
# HINT 2: If nums[i] > 0 after sorting, no triplet can sum to 0 (optional
#         early exit).
# =======================================================================


def three_sum(nums):
    pass  # <-- your code here


# ----------------------------------------------------------------- tests
def _normalize(triplets):
    return sorted(sorted(t) for t in triplets) if triplets is not None else None


def _run_tests():
    cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 0, 0], [[0, 0, 0]]),
        ([1, 2, 3], []),
        ([], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),                      # duplicates must collapse
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
         [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2],
          [-2, -2, 4], [-2, 0, 2]]),
    ]
    passed = 0
    for nums, expected in cases:
        got = _normalize(three_sum(list(nums)))
        ok = got == _normalize(expected)
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {nums}" + ("" if ok else f"  got={got!r} expected={_normalize(expected)!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
