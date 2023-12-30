# Find the Index of the First Occurrence in a String
## Problem
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"

Output: 0  
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

## Solution(s)
The brute force method checks all possible substrings of the `haystack` of the same length as the `needle` to determine if they match. While effective for small strings, this approach might be inefficient for large strings due to its time complexity, particularly when the `haystack` string is significantly longer than the `needle` string.