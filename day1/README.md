# Two Sum
## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

## Solution(s)
### Brute Force
Consider each possible pair of elements and check if their sum matches the target. This approach uses nested loops, with the outer loop spanning from the initial element to the second-to-last element, and the inner loop covering the next element to the end. However, this technique comes with a time complexity of O(n<sup>2</sup>), signifying its inefficiency for larger datasets.

### Hash Map
Using a hash table, iterate through the array and check if the `target` - `current element` exists in the hash table. If it does, that is the solution. Otherwise, we add `current element` to the hash table. This approach has a time complexity of O(n) since hash table lookups take constant time on average.