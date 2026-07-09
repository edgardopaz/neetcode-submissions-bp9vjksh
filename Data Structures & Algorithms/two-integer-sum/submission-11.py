class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for ind, num in enumerate(nums):
            res = target - num
            if res in track:
                return [track[res], ind]
            track[num] = ind
            