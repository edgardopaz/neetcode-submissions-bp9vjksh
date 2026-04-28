class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        snum = set(nums)
        
        for num in nums:
            if num in snum:
                snum.remove(num)
            else:
                return num