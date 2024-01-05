# Single Number
## Problem
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Solution(s)
1) The brute force method would be to iterate through each element in `nums` and check if any element does not appear twice and return this element, this would result in O(n<sup>2</sup>)
2) A more efficient approach would be to iterate over `nums` and keep count of the frequency of each number in a hashmap. The time complexity would reuslt in O(n)