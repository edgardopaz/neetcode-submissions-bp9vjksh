class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[l] < nums[r]:
                # sorted so do normal binary search
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] == target:
                    return mid
                # find the deflection point and then search both sides for the target
                if nums[l] <= nums[mid]:
                    # the left is sorted
                    # check to see if the target is in left side or right side
                    if nums[l] <= target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if nums[mid] < target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
        return -1