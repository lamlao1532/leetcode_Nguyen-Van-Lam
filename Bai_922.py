class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i in nums:
            if i % 2 == 0 :
                arr1.append(i)
            else:
                arr2.append(i)
        arr = []
        for i in range(len(arr1)) :
            arr.append(arr1[i])
            arr.append(arr2[i])
        return arr
