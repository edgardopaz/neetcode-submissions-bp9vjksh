class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            diff = target - nums[i]
            if diff in seen and i != seen[diff]:
                return [seen[diff], i]

        return [0]