"""
PROBLEM 2: Two Sum                                              [Easy]
-----------------------------------------------------------------------
Given a list of integers `nums` and an integer `target`, return the
indices [i, j] (i != j) of the two numbers that add up to `target`.
Exactly one solution exists. Each element may be used only once.

    two_sum([2, 7, 11, 15], 9)  -> [0, 1]     (2 + 7 = 9)
    two_sum([3, 2, 4], 6)       -> [1, 2]
    two_sum([3, 3], 6)          -> [0, 1]

Target: O(n) time, O(n) space.      Pattern: hash map (dict)

Run:  python problem02_two_sum.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES
# =======================================================================
# Brute force: try every pair -> O(n^2).
#
# Key idea: for each number x, the partner you need is (target - x).
# Instead of searching the list for it (O(n)), look it up in a DICT (O(1)).
#
# A DICT maps keys to values, backed by a hash table:
#   d = {}                    # empty dict
#   d[key] = value            # insert / overwrite
#   key in d                  # membership test, O(1) average
#   d[key]                    # read (KeyError if missing)
#   d.get(key, default)       # read, or `default` if missing
#
# enumerate gives you the index AND the value in one loop:
#   for i, x in enumerate(nums):
#       ...
#
# HINT 1: What should the dict store? (think: value -> its index)
# HINT 2: At each element, check whether its partner is ALREADY in the
#         dict *before* adding the current element. Why does the order
#         matter for input like [3, 3] with target 6?
# =======================================================================


def two_sum(nums, target):
    pass  # <-- your code here


# ----------------------------------------------------------------- tests
def _run_tests():
    cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
        (([-1, -2, -3, -4, -5], -8), [2, 4]),
        (([0, 4, 3, 0], 0), [0, 3]),
    ]
    passed = 0
    for (nums, target), expected in cases:
        got = two_sum(list(nums), target)
        got = sorted(got) if got else got  # order of the pair doesn't matter
        ok = got == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {nums}, target={target}" + ("" if ok else f"  got={got!r} expected={expected!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
