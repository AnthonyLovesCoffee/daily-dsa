# Roman to Integer
## Problem
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`. Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`.

## Solution(s)
In Roman numerals, when a smaller value appears before a larger value, it represents subtraction, while when a smaller value appears after or equal to a larger value, it represents addition. We create a map, mapping Roman numerals to their corrosponding integer value. The loop iterates over the input string and will check conditions to see if we need to subtract or add the interger value to/from the next integer value.