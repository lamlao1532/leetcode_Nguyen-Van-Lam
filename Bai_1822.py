class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 1
        for i in nums:
            count = count * i
        if count > 0:
            return 1
        elif count == 0:
            return 0
        else :
            return -1
