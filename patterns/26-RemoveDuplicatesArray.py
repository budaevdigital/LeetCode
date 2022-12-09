"""
Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.

It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
not allocate extra space for another array.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate = 1
        for index in range(len(nums) - 1):
            slow = nums[index]
            fast = nums[index + 1]
            if slow != fast:
                nums[duplicate] = nums[index]
                duplicate += 1
        return duplicate


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
test = Solution()

print(test.removeDuplicates(nums))
