# Number of 1 Bits
## Problem
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

## Solution(s)
Brian Kernighan’s algorithm is used here. Using `n& = (n-1)` to change the variable within the loop.

For `n& = (n-1)`, it means the least right most '1' is removed.