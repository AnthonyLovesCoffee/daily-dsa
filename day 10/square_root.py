def customSqrt(x):
    if x == 0:
        return 0
    left, right = 1, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            right = mid - 1
        else:
            left = mid + 1
    return right

print(customSqrt(25)) # return 5