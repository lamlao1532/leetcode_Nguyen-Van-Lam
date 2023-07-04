class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = sorted(heights)
        count = 0
        n = len(arr)
        for i in range(n):
            if heights[i] != arr[i]:
                count += 1
        return count
