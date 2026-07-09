class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortT = sorted(t)
        sortS = sorted(s)

        return sortT == sortS