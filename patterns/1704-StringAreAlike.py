"""
You are given a string s of even length.

Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').

Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
"""
import re


class Solution(object):
    def halvesAreAlike(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        MASKS_STRING = "aeiouAEIOU"
        left = s[0 : int(len(s) / 2)]
        right = s[int(len(s) / 2) : len(s)]
        left_count = len(re.findall(f"[{MASKS_STRING}]", left))
        right_count = len(re.findall(f"[{MASKS_STRING}]", right))
        return left_count == right_count


new = Solution()
print(new.halvesAreAlike("textbook"))
print(new.halvesAreAlike("book"))
