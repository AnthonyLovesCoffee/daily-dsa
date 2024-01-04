# Add Binary
## Problem
Given two binary strings `a` and `b`, return their sum as a binary string.

## Solution(s)
Start at the right end of each binary number, adding the digits and any carry-over value, and storing the result in a new string.
Next, move to the next digit on the left and repeat the process until it has gone through all the digits in both binary numbers.
If there is any carry-over value after adding all the digits, append it to the end of the new string.
Finally, the new string is reversed and returned as the sum of the two binary numbers.