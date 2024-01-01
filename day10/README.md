# Sqrt(x)
## Problem
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well.

You must **not** use any built-in exponent function or operator.

## Solution(s)
Instead of using a traditional approach like repeatedly subtracting numbers until we reach 0 or using a library function, we'll use a smarter method called "Binary Search." Binary Search repeatedly narrows down the search range. We start with a range between 1 and x, narrowing down the search space iteratively. Using binary search, it continuously divides the range in half and adjusts boundaries based on whether the square of the midpoint is greater than, equal to, or less than x. Eventually, it finds the integer part of the square root or returns the closest integer lower than the square root if it's not a perfect square.