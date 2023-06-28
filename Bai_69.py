#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        c = 1
        if x == 0 :
            return 0
        if x == 1 :
            return 1
        for i in range (1, x):
            if i*i <= x:
                c = i
            if i*i > x:
                break
        return c
# @lc code=end

