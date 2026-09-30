class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seq = 0
        nums_set = set(nums)
        i = 0

        if not nums:
            return 0
            
        for i in range(len(nums)):
            if (nums[i] - 1) not in nums_set:
                seq = 1
                while (nums[i] + seq) in nums_set:
                    seq += 1
            res = max(seq, res)
        
        return res