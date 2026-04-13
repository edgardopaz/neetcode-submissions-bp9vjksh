class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        dup = set()
        res = 0

        while r < len(s):
            if s[r] in dup:
                dup.remove(s[l])
                print(f"dup after removing{dup}")
                l += 1
            else:
                dup.add(s[r])
                print(f"dup after adding {dup}")
                r += 1
            print(f"{r} - {l}")
            res = max(res, r - l)
        return res