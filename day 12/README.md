# Excel Sheet Column Title
## Problem
Given an integer `columnNumber`, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1  
B -> 2  
C -> 3  
...  
Z -> 26  
AA -> 27  
AB -> 28 

## Solution(s)
1) For the brute force approach, we continuously divide the given number by 26 and determine the remainder. This remainder gives us the current character of the Excel title, starting from the least significant character.