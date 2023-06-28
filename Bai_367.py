class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        c = 1
        if num == 0 :
            return True
        if num == 1 :
            return True
        for i in range (1, num):
            if i*i == num:
                return True
            if i*i > num:
                break
        return False
