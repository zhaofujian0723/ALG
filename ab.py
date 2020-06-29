# -*- coding: utf-8 -*-
"""
A + B问题
"""


class Solution(object):

    def aplusb(self, a, b):
        """入口"""
        if ((a < 0) and (b > 0)) or ((b < 0) and (a > 0)):
            if a < 0:
                a = (a * -1)
                a2 = bin(a)[2:][::-1]
                b2 = bin(b)[2:][::-1]
                if a > b:
                    r = self.subtract(b2, a2, 0, "", 0) * -1
                else:
                    r = self.subtract(a2, b2, 0, "", 0)
            else:
                b = (b * -1)
                a2 = bin(a)[2:][::-1]
                b2 = bin(b)[2:][::-1]
                if a > b:
                    r = self.subtract(b2, a2, 0, "", 0)
                else:
                    r = self.subtract(a2, b2, 0, "", 0) * -1
        elif a < 0 and b < 0:
            a = (a * -1)
            b = (b * -1)
            a2 = bin(a)[2:][::-1]
            b2 = bin(b)[2:][::-1]
            if len(a2) > len(b2):
                r = self.plus(b2, a2, 0, "", 0) * -1
            else:
                r = self.plus(a2, b2, 0, "", 0) * -1
        else:
            a2 = bin(a)[2:][::-1]
            b2 = bin(b)[2:][::-1]
            if len(a2) > len(b2):
                r = self.plus(b2, a2, 0, "", 0)
            else:
                r = self.plus(a2, b2, 0, "", 0)
        return r

    def plus(self, num1, num2, x, c, y):
        """加法运算"""
        if len(num1) > x and len(num2) > x:
            if int(num1[x]) ^ int(num2[x]):
                if y == 1:
                    c += "0"
                    y = 1
                else:
                    c += "1"
                    y = 0
            else:
                if not int(num1[x]):
                    if y == 1:
                        c += "1"
                    else:
                        c += "0"
                    y = 0
                else:
                    if y == 1:
                        c += "1"

                    else:
                        c += "0"
                    y = 1
            x += 1
            return self.plus(num1, num2, x, c, y)
        else:
            if y == 1:
                num1 += "1"
                y = 0
                return self.plus(num1, num2, x, c, y)
            else:
                if len(num1) > len(num2):
                      c += num1[x:]
                else:
                    c += num2[x:]
                return int(c[::-1], 2)

    def subtract(self, num1, num2, x, c, y):
        """减法"""
        if len(num1) > x and len(num2) > x:
            if int(num1[x]) ^ int(num2[x]):
                if int(num1[x]) > int(num2[x]):
                    if y == 1:
                        c += "0"
                        y = 1
                    else:
                        c += "1"
                        y = 1
                else:
                    if y == 1:
                        c += "0"
                        y = 0
                    else:
                        c += "1"
                        y = 0
            else:
                if int(num2[x]) > 0:
                    if y == 1:
                        c += "1"
                        y = 1
                    else:
                        c += "0"
                        y = 0
                else:
                    if y == 1:
                        c += "1"
                        y = 1
                    else:
                        c += "0"
                        y = 0
            x += 1
            return self.subtract(num1, num2, x, c, y)
        else:
            if y == 1:
                if int(num2[x]) > 0:
                    c += "0"
                    y = 0
                else:
                    c += "1"
                    y = 1
                x += 1
                return self.subtract(num1, num2, x, c, y)
            else:
                c += num2[x:]
                return int(c[::-1], 2)

if __name__ == '__main__':
    s = Solution()
    res = s.aplusb(-100, -100)
    print(res)
