class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp1 = temp2 = True
        n= len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                temp1 = False
            if nums[i] > nums[i-1]:
                temp2 = False
        ans = temp1 or temp2        
        return ans
