class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 1
        res = 0
        numsSet = set(nums)

        if not nums:
            return res

        for num in nums:
            if num - 1 not in numsSet:
                seq = 1
                while num + seq in numsSet:
                    seq += 1
            res = max(res, seq)
            
        return res