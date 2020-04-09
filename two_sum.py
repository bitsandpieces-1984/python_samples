""" Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 """


class Solution:
    def twoSum(self, nums, target):
        lookup_value = {index_v: index_k for (
            index_k, index_v) in enumerate(nums)}
        for item_index, item in enumerate(nums):
            diff = target - item
            if diff in lookup_value.keys():
                if not item_index == lookup_value[diff]:
                    return sorted([item_index, lookup_value[diff]])
        return []
