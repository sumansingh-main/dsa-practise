"""
PROBLEM 5: Maximum Subarray Sum                                 [Easy/Medium]
-----------------------------------------------------------------------
Given a NON-EMPTY list of integers (may include negatives), return the
largest sum of any CONTIGUOUS subarray.

    max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])  -> 6   ([4, -1, 2, 1])
    max_subarray_sum([5])                              -> 5
    max_subarray_sum([-3, -1, -2])                     -> -1

Target: O(n) time, O(1) space.      Pattern: Kadane's algorithm (a simple DP)

Run:  python problem05_max_subarray_sum.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES
# =======================================================================
# A SUBARRAY is contiguous (no gaps). A subsequence is not. [4, -1, 2, 1]
# is a subarray of the example; [-2, 4, 1] is only a subsequence.
#
# Brute force: compute the sum of every (start, end) pair -> O(n^2)
# (or O(n^3) if you re-add each time).
#
# Kadane's insight -- at each index i, ask one question:
#     "What's the best sum of a subarray that ENDS at i?"
# Two choices:
#     (a) extend the best subarray ending at i-1 by adding nums[i], or
#     (b) start fresh at nums[i]  (better if the previous sum is negative,
#         since a negative prefix only drags you down).
#
#     best_ending_here = max(nums[i], best_ending_here + nums[i])
#
# The answer is the biggest best_ending_here seen at any index, so keep a
# second variable for the overall best.
#
# Watch out: if ALL numbers are negative, the answer is the least-negative
# one (not 0!). So don't initialise your answer to 0 -- initialise it from
# the first element.
#
# Useful syntax:
#   nums[1:]            # slice: everything except the first element (copy)
#   max(a, b)
#
# HINT 1: Variables you need: `current` and `best`, both starting at nums[0].
# HINT 2: Loop from the second element onward, updating current then best.
# =======================================================================


def max_subarray_sum(nums):
    pass  # <-- your code here


# ----------------------------------------------------------------- tests
def _run_tests():
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([5], 5),
        ([-3, -1, -2], -1),
        ([1, 2, 3, 4], 10),
        ([-1, 2, -1, 2], 3),
        ([0, -1, 0], 0),
    ]
    passed = 0
    for nums, expected in cases:
        got = max_subarray_sum(list(nums))
        ok = got == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {nums}" + ("" if ok else f"  got={got!r} expected={expected!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
