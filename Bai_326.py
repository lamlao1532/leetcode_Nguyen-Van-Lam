class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range ( 0, 31 ) :
            if 3**i == n :
                return True
        return False
