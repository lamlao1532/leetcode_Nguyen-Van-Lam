class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr1 = []
        set1 = set()
        for i in nums:
            if i in set1:
               arr1.append(i)
            else:
               set1.add(i)
        return arr1[-1]
