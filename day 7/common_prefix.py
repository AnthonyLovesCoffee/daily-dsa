def commonPrefix(arr):
    ans = ""
    arr = sorted(arr)
    first = arr[0]
    last = arr[-1]
    for i in range(min(len(first),len(last))):
        if(first[i] != last[i]):
            return ans
        ans += first[i]
    return ans

print(commonPrefix(["flower","flow","flight"]))