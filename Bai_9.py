#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        #Copying the original number
        temp = x

        #Finding Reverse
        while temp > 0:
            rev = (rev*10) + (temp %10);
            temp = temp//10

        #Comparing reverse with original number
        if rev == x :
            return True
        else:
            return False
# @lc code=end

