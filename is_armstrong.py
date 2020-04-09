""" The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

 

Example 1:

Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
Example 2:

Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
 """

class Solution:
    def isArmstrongv1(self, N):
        sum_total = sum([ int(x) ** len(str(N)) for x in str(N)])
        if sum_total == N:
            return True
        else:
            return False

    def isArmstrongv2(self, N):
        sum_total = sum(map(lambda x : int(x) ** len(str(N)), list(str(N))))
        if sum_total == N:
            return True
        else:
            return False


obj = Solution()
print(obj.isArmstrongv1(153))
print(obj.isArmstrongv1(153))