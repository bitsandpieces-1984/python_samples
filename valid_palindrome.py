import re

""" iven a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false """

class Solution:
    def filterAlphaNumeric(self, s):
        return re.sub(r'[^\w]+', '', s)

    def reverseString(self, s):
        return ''.join(reversed(s))

    def isPalindrome(self, s):

        filtered_string = self.filterAlphaNumeric(s).lower()
        reverse_string = self.reverseString(filtered_string)

        if not filtered_string == reverse_string:
            return False
        else:
            return True


obj = Solution()
print(obj.isPalindrome('A man, a plan, a canal: Panama'))
print(obj.isPalindrome( 'race a car'))