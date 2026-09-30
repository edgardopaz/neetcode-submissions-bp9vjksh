import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans('', '', string.punctuation)
        s = s.translate(translator)
        words = s.split()
        s = "".join(words)
        l, r = 0, len(s) - 1

        while l < r:
            print(s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False
            l += 1 
            r -= 1
        return True