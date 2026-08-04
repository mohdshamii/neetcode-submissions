class Solution:
            def hasDuplicate(self, nums):
                    return len(nums) != len(set(nums))