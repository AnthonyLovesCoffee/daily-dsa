# Length of Last Word
## Problem
Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

## Solution(s)
One way of solving this would be to use the `split()` method to split the words at the whitespaces, then return the length of the last word in the array. However, this is an inefficient solution due to having to split on every whitespace when we only need the last word.
An optimized solution would be to traverse the string from the back instead.