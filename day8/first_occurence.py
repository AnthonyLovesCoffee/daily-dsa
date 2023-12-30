def firstOccur(haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i+len(needle)] == needle:
                return i
        return -1

print(firstOccur("sadbutsad", "sad")) # return 0
print(firstOccur("letcodeisfun", "leeto")) # return -1