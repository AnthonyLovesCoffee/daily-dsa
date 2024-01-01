def romanToDecimal(num):
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(num)):
            if i < len(num) - 1 and m[num[i]] < m[num[i+1]]:
                ans -= m[num[i]]
            else:
                ans += m[num[i]]
        
        return ans

print(romanToDecimal("XXI"))