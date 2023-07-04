class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr1 = []
        set1 = set()
        for i in nums:
            if i in set1 :
                arr1.append(i)
            else:
                set1.add(i)
        if (len(arr1) > 0):
            return True
        return False
