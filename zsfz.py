"""
整数反转
"""


class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        g = number % 10
        s = int(number / 10 % 10)
        b = int(number / 100)
        return int(str(g) + str(s) + str(b))

if __name__ == '__main__':
    S = Solution()
    res = S.reverseInteger(100)
    print(res)
