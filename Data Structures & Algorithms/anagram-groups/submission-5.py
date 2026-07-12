class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = []
        for s in strs:
            key = "".join(sorted(s))
            pairs.append((key, s))
        pairs.sort()

        print(pairs)
        res = []
        i = 0
        while i < len(pairs):
            temp = [pairs[i][1]]
            while i + 1 < len(pairs) and pairs[i + 1][0] == pairs[i][0]:
                temp.append(pairs[i + 1][1])
                i += 1
            res.append(temp)
            i += 1
        return res