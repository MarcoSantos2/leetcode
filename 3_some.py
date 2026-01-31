"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order."""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):

            # Skip duplicate fixed pointer
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # Now move both pointers
                    l += 1
                    r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res