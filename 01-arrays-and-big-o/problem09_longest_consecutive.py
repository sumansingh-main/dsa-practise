"""
PROBLEM 9: Longest Consecutive Sequence                         [Medium]
-----------------------------------------------------------------------
Given an UNSORTED list of integers, return the length of the longest run
of consecutive integers (e.g. 3, 4, 5, 6). The run's elements can appear
in any order in the list.

    longest_consecutive([100, 4, 200, 1, 3, 2])        -> 4   (1, 2, 3, 4)
    longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) -> 9   (0..8)
    longest_consecutive([])                            -> 0

Target: O(n) time.                  Pattern: hash set, count only from run starts

Run:  python problem09_longest_consecutive.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES
# =======================================================================
# Easy approach: sort, then scan for runs -> O(n log n). The challenge is
# to hit O(n), which means NO sorting.
#
# Idea: put everything in a SET so "is x present?" is O(1).
#
# Naive version: for every x, keep checking x+1, x+2, ... -> can be O(n^2)
# because you re-walk the same run from every element inside it.
#
# Fix: only start counting at the BEGINNING of a run.
#   x is the start of a run exactly when (x - 1) is NOT in the set.
# From a start, walk x+1, x+2, ... while they're in the set, counting.
# Each number is visited by at most one walk, so the total work is O(n).
#
# Duplicates: building a set removes them, so iterate over the SET, not
# the original list.
#
# Useful syntax:
#   s = set(nums)
#   for x in s: ...
#   while (x + length) in s:         # `while` + membership test
#       length += 1
#   max(best, length)
#
# HINT 1: Handle the empty list (answer 0).
# HINT 2: Inside the loop: `if x - 1 in s: continue` skips non-starts.
# HINT 3: Why is the nested `while` still O(n) overall?
# =======================================================================


def longest_consecutive(nums):
    pass  # <-- your code here


# ----------------------------------------------------------------- tests
def _run_tests():
    cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([5], 1),
        ([1, 1, 1], 1),
        ([1, 2, 0, 1], 3),
        ([-1, -2, -3, 10], 3),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
    ]
    passed = 0
    for nums, expected in cases:
        got = longest_consecutive(list(nums))
        ok = got == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {nums}" + ("" if ok else f"  got={got!r} expected={expected!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
