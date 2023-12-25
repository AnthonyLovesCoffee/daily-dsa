# Remove Element
## Problem
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

## Solution(s)
Iterate through the array and keep track of two pointers: `index` and `i`. The `index` pointer is the position where the next non-target element should be placed. The `i` pointer iterates through the array elements. By overwriting the target elements with non-target elements, the solution effectively removes all occurrences of the target value from the array.