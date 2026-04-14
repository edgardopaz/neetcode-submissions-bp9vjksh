class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        table = {}
        
        l, maxF = 0, 0
        
        for r in range(len(s)):
            table[s[r]] = 1 + table.get(s[r], 0)
            maxF = max(maxF, table[s[r]])

            while (r - l + 1) - maxF > k:
                table[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res