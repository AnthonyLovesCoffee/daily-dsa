# Remove Suplicates from Sorted Array
## Problem
Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements, `k` within `nums`

## Solution(s)
Using two pointers, `i` and `j`, to iterate through the array, the variable `j` is used to keep track of the current index where a **unique** element should be placed. The initial value of `j` is 1 since the first element in the array is always unique and doesn't need to be changed. The code starts iterating from `i = 1` because we need to compare each element with its previous element to check for duplicates.
