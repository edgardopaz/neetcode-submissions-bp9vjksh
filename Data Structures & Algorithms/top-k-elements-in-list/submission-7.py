class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        while k > 0:
            highest =(max(count, key=count.get))
            res.append(highest)
            count.pop(highest)
            k -= 1
            
        return res