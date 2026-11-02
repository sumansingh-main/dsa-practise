"""
PROBLEM 6: Product of Array Except Self                         [Medium]
-----------------------------------------------------------------------
Return a list `out` where out[i] is the product of ALL elements of nums
except nums[i]. You may NOT use division.

    product_except_self([1, 2, 3, 4])  -> [24, 12, 8, 6]
    product_except_self([1, 0, 3])     -> [0, 3, 0]

Target: O(n) time, O(1) EXTRA space (the output list doesn't count).
Pattern: prefix products + suffix products

Run:  python problem06_product_except_self.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES
# =======================================================================
# Brute force: for each i, multiply all the others -> O(n^2).
# "Just divide the total product by nums[i]" breaks on zeros and is banned.
#
# Key decomposition:
#     out[i] = (product of everything LEFT of i) * (product of everything RIGHT of i)
#
# Example for [1, 2, 3, 4]:
#     left products : [1, 1, 2, 6]     (product of elements before each index)
#     right products: [24, 12, 4, 1]   (product of elements after each index)
#     multiply      : [24, 12, 8, 6]
#
# To use O(1) extra space, don't build two separate lists:
#   Pass 1 (left -> right): fill `out` with the left products, keeping a
#                           running variable `left` that you multiply as you go.
#   Pass 2 (right -> left): keep a running variable `right`, and multiply
#                           it into out[i].
#
# Useful syntax:
#   out = [1] * n                      # list of n ones
#   range(n - 1, -1, -1)               # n-1, n-2, ..., 0  (iterate backwards)
#   out[i] *= right                    # same as out[i] = out[i] * right
#
# HINT 1: In pass 1, write the running product into out[i] BEFORE
#         multiplying nums[i] into the running product. Why?
# HINT 2: Pass 2 is the mirror image, going backwards.
# =======================================================================


def product_except_self(nums):
    pass  # <-- your code here


# ----------------------------------------------------------------- tests
def _run_tests():
    cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([1, 0, 3], [0, 3, 0]),
        ([0, 0], [0, 0]),
        ([2, 3], [3, 2]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([5, 5, 5], [25, 25, 25]),
    ]
    passed = 0
    for nums, expected in cases:
        got = product_except_self(list(nums))
        ok = got == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {nums}" + ("" if ok else f"  got={got!r} expected={expected!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
