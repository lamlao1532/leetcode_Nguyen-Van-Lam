class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        integer = 0
        n = len(s)
        for i in range (n - 1):
            if(roman[s[i]] < roman[s[i + 1]]):
                integer = integer - roman[s[i]]
            else:
                integer = integer + roman[s[i]]
        m = integer + roman[s[-1]]
        return m
