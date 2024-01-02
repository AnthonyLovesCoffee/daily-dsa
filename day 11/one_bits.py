# n is entered as an int type
def hammingWeightInt(n):
    count = 0
    while n != 0:
        n &= (n - 1)
        count += 1
    return count

# n is entered as string
def hammingWeightStr(n):
    return bin(n).count('1') 

print(hammingWeightInt(1001011))