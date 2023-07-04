# leetcode_Nguyen-Van-Lam
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        n = len(nums)
        for i in range(n):
            c = target - nums[i]
            if c in a:
                return [a[c], i]
            a[nums[i]] = i
        
