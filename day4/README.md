# Remove Element
## Problem
Given an integer `x`, return `true` if `x` is a *palindrome*, and `false` otherwise.

## Solution(s)
We can reverse the input number and check if the reversed number is equal to the original number. If they are the same, then the number is a palindrome. In the code `reversed` is the variable that will store the reversed value of the number `x`. `temp` is a temporary placeholder to manipulate the input number without modifying the original value. Inside the loop, we extract the last digit of `temp` using `%` and store it in the `digit` variable. To reverse the number, we multiply the current value of `reversed` by 10 and add the extracted `digit`. We then divide `temp` by 10 to remove the last digit and move on to the next iteration until `temp` becomes zero.