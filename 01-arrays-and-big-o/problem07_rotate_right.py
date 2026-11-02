"""
PROBLEM 7: Rotate Array                                         [Medium]
-----------------------------------------------------------------------
Rotate the list to the right by k steps, IN PLACE.

    nums = [1, 2, 3, 4, 5, 6, 7], k = 3  ->  [5, 6, 7, 1, 2, 3, 4]
    nums = [-1, -100, 3, 99],     k = 2  ->  [3, 99, -1, -100]

Target: O(n) time, O(1) extra space.    Pattern: three reversals

Run:  python problem07_rotate_right.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES
# =======================================================================
# Easy but costly approach: nums[:] = nums[-k:] + nums[:-k]  -> O(n) extra space.
# (`nums[:] = ...` assigns INTO the existing list, so it is still "in place"
#  from the caller's view, but it builds temporary copies.)
#
# O(1)-space trick: REVERSAL.
#   Start        : [1, 2, 3, 4, 5, 6, 7]   k = 3
#   Reverse all  : [7, 6, 5, 4, 3, 2, 1]
#   Reverse first k elements   : [5, 6, 7, 4, 3, 2, 1]
#   Reverse remaining elements : [5, 6, 7, 1, 2, 3, 4]   <- done
#
# Write a small helper that reverses nums between indices l and r using
# two pointers that move toward each other:
#     while l < r:
#         swap nums[l] and nums[r]
#         l += 1; r -= 1
#
# EDGE CASES:
#   - k can be larger than len(nums). Rotating by len(nums) gives the
#     same list back, so use the remainder:   k = k % len(nums)
#   - Empty list: k % 0 raises ZeroDivisionError -- guard against it.
#   - k == 0 (after the modulo): nothing to do.
#
# Useful syntax:
#   a, b = b, a                      # swap
#   nums[l], nums[r] = nums[r], nums[l]
#   def helper(l, r): ...            # a function defined INSIDE another
#                                    # function can read `nums` directly
#
# HINT 1: Reduce k first with the modulo.
# HINT 2: Three calls to your reverse helper, with the right (l, r) ranges.
# =======================================================================


def rotate_right(nums, k):
    pass  # <-- your code here (modify nums in place, return nothing)


# ----------------------------------------------------------------- tests
def _run_tests():
    cases = [
        (([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
        (([-1, -100, 3, 99], 2), [3, 99, -1, -100]),
        (([1, 2], 3), [2, 1]),          # k > len
        (([1, 2, 3], 0), [1, 2, 3]),
        (([1, 2, 3], 3), [1, 2, 3]),    # k == len
        (([1], 5), [1]),
        (([], 2), []),
    ]
    passed = 0
    for (nums, k), expected in cases:
        arr = list(nums)
        try:
            rotate_right(arr, k)
        except Exception as e:
            arr = f"raised {type(e).__name__}"
        ok = arr == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {nums}, k={k}" + ("" if ok else f"  got={arr!r} expected={expected!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
