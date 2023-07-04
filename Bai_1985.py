class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = []
        #Chuyen ve so
        for i in nums:
            arr.append(int(i))
        arr1 = sorted(arr ,reverse=True)
        ans = str(arr1[k-1])
        return ans
