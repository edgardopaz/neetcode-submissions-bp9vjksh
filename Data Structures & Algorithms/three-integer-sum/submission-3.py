class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        target = 0
        res = []

        print(nums)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0 and [nums[i], nums[left], nums[right]] not in res:
                    res.append([nums[i], nums[left], nums[right]])
                if temp < 0:
                    left += 1
                else:
                    right -= 1

        return res    