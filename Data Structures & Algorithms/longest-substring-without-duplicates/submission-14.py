class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = []
        total = 0

        for r in range(len(s)):
            if s[r] in res:
                while s[r] in res:
                    res.pop(0)
                res.append(s[r])
                l = r
            else:
                res.append(s[r])
                total = max(len(res), total)

        return total