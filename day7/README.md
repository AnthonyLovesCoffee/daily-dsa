# Longest Common Prefix
## Problem
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.
## Solution(s)
Sort the input list `arr` alphabetically because the common prefix should be common to all the strings, so we need to find the common prefix of the first and last string in the sorted list.
Iterate through the characters of the first and last string in the sorted list, stopping at the length of the shorter string.
If the current character of the first string is not equal to the current character of the last string, return the common prefix found so far.
Otherwise, append the current character to the `ans` string.