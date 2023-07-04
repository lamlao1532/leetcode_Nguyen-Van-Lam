class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        sum = 0
        for i in nums:
            if i % 6 == 0:
                count += 1
                sum   += i
        if count == 0:
            return 0
        ans = sum // count
        return ans
