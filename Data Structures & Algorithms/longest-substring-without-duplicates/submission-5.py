class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = ""
        maxL = 0

        while right < len(s):
            if s[right] not in res:
                res += s[right]
                right += 1

            else:
                total = len(res)
                maxL = max(total, maxL)
                res = res[1:]
                left += 1
        maxL = max(maxL, len(res))
        return maxL