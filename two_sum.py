""" Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 """

class Solution:

    def twoSum(self, nums, target):

        number_lookup = {}
        output=[]

        for item_index, item in enumerate(nums,start=0):
            number_lookup[item] = item_index

        for item, item_index in number_lookup.items():
            remainder = target - item
            if remainder in number_lookup.keys():
                output.append(item)
                output.append(number_lookup[remainder])
                break
        