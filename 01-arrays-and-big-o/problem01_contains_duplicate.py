"""
PROBLEM 1: Contains Duplicate                                   [Easy]
-----------------------------------------------------------------------
Given a list of integers, return True if any value appears at least
twice, otherwise False.

    contains_duplicate([1, 2, 3, 1])  -> True
    contains_duplicate([1, 2, 3])     -> False
    contains_duplicate([])            -> False

Target: O(n) time, O(n) space.      Pattern: hash set

Run:  python problem01_contains_duplicate.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES (read these before you start)
# =======================================================================
# Brute force: compare every pair with two nested loops -> O(n^2).
#
# A SET is a collection of unique values backed by a hash table.
#   - Checking membership (`x in s`) is O(1) on average.
#   - Adding (`s.add(x)`) is O(1) on average.
#   - A LIST's `x in lst` is O(n)  <-- this is the trap to avoid.
#
# Useful syntax:
#   seen = set()          # empty set  (NOT {} -- that makes a dict)
#   seen.add(5)
#   5 in seen             # True
#   len(seen)             # number of unique items
#   set([1, 1, 2])        # {1, 2}  -- builds a set from a list
#
# HINT 1: What do you need to remember as you walk through the list?
# HINT 2: For each number, have you seen it before? If yes, you're done.
# HINT 3 (one-liner idea): how does the length of the list compare to the
#         length of set(list) when there are no duplicates?
# =======================================================================


def contains_duplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if(nums[i] == nums[j]):
                return True
    return False

def contains_duplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

def contains_duplicate(nums):
    seen = set()
    return len(set(nums)) != len(nums)

# ----------------------------------------------------------------- tests
def _run_tests():
    cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3], False),
        ([], False),
        ([5], False),
        ([7, 7], True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10], True),
    ]
    passed = 0
    for nums, expected in cases:
        got = contains_duplicate(list(nums))
        ok = got == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {nums}" + ("" if ok else f"  got={got!r} expected={expected!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
