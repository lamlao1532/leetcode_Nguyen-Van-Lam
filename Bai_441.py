class Solution:
    def arrangeCoins(self, n: int) -> int:
        c = 1
        for i in range (1, n + 1):
            if n < (i*(i + 1))/2 :
                c = i - 1
                break
        return c
