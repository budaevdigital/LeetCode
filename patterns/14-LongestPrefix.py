"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for index in strs:
            while not index.startswith(prefix):
                prefix = prefix[:-1]
        return prefix


new = Solution()
print(new.longestCommonPrefix(["flower", "flow", "flight"]))
print(new.longestCommonPrefix(["dog", "racecar", "car"]))
print(new.longestCommonPrefix(["a"]))
print(new.longestCommonPrefix(["", ""]))
