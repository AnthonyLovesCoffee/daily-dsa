# Number of Good Pairs
## Problem
Given an array of integers nums, return the number of good pairs.

A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.

## Solution(s)
Count the number of good pairs without explicitly checking all pairs in a nested loop. By using a dictionary to keep track of the count of each number, you can determine how many good pairs can be formed with each number as you iterate through the array.