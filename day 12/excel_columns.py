def convertToExcel(columnNumber):
    result = []
    while columnNumber:
        columnNumber, remainder = divmod(columnNumber - 1, 26)
        result.append(chr(65 + remainder))
    return ''.join(reversed(result))

print(convertToExcel(27)) # return AA