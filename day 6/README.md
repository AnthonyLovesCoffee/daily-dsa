# Valid Paranthesis
## Problem
Given a string `string` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1) Open brackets must be closed by the same type of brackets.  
2) Open brackets must be closed in the correct order.  
3) very close bracket has a corresponding open bracket of the same type.
## Solution(s)
We can use a stack data structure to keep track of opening brackets encountered and check if they match with the corresponding closing brackets.