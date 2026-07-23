class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""

        for c in s:
            if c.isalnum():
                res += c.lower()
        
        left = 0
        right = len(res) - 1

        while left <= right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1

        return True    