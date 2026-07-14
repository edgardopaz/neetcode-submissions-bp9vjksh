class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = {}

        for num in nums:
            res[num] = res.get(num, 0) + 1
        
        freq = []

        while res and k > 0:
            key = max(res, key = res.get)
            res.pop(key)
            freq.append(key)
            k -= 1

        return freq