"""
PROBLEM 3: Best Time to Buy and Sell Stock                      [Easy]
-----------------------------------------------------------------------
`prices[i]` is the price of a stock on day i. You may buy on one day and
sell on a LATER day. Return the maximum profit, or 0 if no profit is
possible.

    best_time_to_buy_sell([7, 1, 5, 3, 6, 4])  -> 5   (buy at 1, sell at 6)
    best_time_to_buy_sell([7, 6, 4, 3, 1])     -> 0   (prices only fall)

Target: O(n) time, O(1) space.      Pattern: one pass + running minimum

Run:  python problem03_best_time_to_buy_sell.py
"""

# =======================================================================
# THEORY / SYNTAX NOTES
# =======================================================================
# Brute force: try every (buy, sell) pair with buy < sell -> O(n^2).
#
# Better thinking: if you sell on day i, what's the BEST day to have
# bought? The cheapest price seen so far (before day i). So walk once,
# tracking two things:
#   1. the lowest price seen so far
#   2. the best profit seen so far
#
# This is a general trick: instead of looking backwards each time (O(n)),
# keep a running summary of the past (O(1) to update).
#
# Useful syntax:
#   float("inf")        # a value bigger than any number (good starting min)
#   min(a, b), max(a, b)
#   for p in prices:    # iterate values directly when you don't need indices
#
# HINT 1: At each price, first update the running minimum.
# HINT 2: Then ask: "if I sold today, what would my profit be?"
#         Keep the max of that.
# =======================================================================


def best_time_to_buy_sell(prices):
    pass  # <-- your code here


# ----------------------------------------------------------------- tests
def _run_tests():
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([5], 0),
        ([3, 3, 3], 0),
        ([2, 4, 1, 7], 6),
    ]
    passed = 0
    for prices, expected in cases:
        got = best_time_to_buy_sell(list(prices))
        ok = got == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {prices}" + ("" if ok else f"  got={got!r} expected={expected!r}"))
    print(f"\n{passed}/{len(cases)} passed")


if __name__ == "__main__":
    _run_tests()
