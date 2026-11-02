"""
PROBLEM 4: Move Zeroes                                          [Easy]
-----------------------------------------------------------------------
Move all 0s in the list to the END, keeping the relative order of the
non-zero elements. Modify the list IN PLACE (don't return a new list).

    nums = [0, 1, 0, 3, 12]  ->  nums becomes [1, 3, 12, 0, 0]

Target: O(n) time, O(1) extra space.    Pattern: write pointer

Run:  python problem04_move_zeroes.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES
# =======================================================================
# "In place" means you change the SAME list object rather than building
# a new one. Because lists are mutable, a function can change the
# caller's list:
#
#   def f(nums):
#       nums[0] = 99        # caller sees this change
#   def g(nums):
#       nums = [1, 2, 3]    # does NOT change caller's list (rebinds the name!)
#
# So don't write `nums = something_new`. Assign to `nums[i]` instead.
#
# Swapping two elements without a temp variable:
#   nums[i], nums[j] = nums[j], nums[i]
#
# THE WRITE POINTER IDEA:
#   Keep an index `w` = "where the next non-zero element should go".
#   Scan the list with another index (or a for loop). Each time you see
#   a non-zero value, place it at position w and move w forward.
#   Everything from w onward must then be zeros.
#
# HINT 1: After the scan, what do positions w .. len-1 need to be?
# HINT 2: Alternative: swap each non-zero with nums[w] while scanning, so
#         the zeros end up behind automatically (single pass).
# =======================================================================


def move_zeroes(nums):
    pass  # <-- your code here (modify nums in place, return nothing)


# ----------------------------------------------------------------- tests
def _run_tests():
    cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 0], [0, 0, 0]),
        ([], []),
        ([4, 0, 5, 0, 0, 6], [4, 5, 6, 0, 0, 0]),
    ]
    passed = 0
    for nums, expected in cases:
        arr = list(nums)
        move_zeroes(arr)
        ok = arr == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {nums}" + ("" if ok else f"  got={arr!r} expected={expected!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
