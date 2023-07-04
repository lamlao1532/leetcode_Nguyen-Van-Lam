class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pre = strs[0]
        n = len(strs)
        for i in range(1, n):
            while not strs[i].startswith(pre):
                pre = pre[:-1]
            if not pre:
                return ""
        return pre
        
