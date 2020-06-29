"""
字符串查找
"""


class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source == "" and target == "":
            return 0
        if source == "":
            return -1
        if target == "":
            return 0
        if source == target:
            return 0
        if len(target) > len(source):
            return -1
        else:
            if len(source) == len(target):
                return -1
            y = 0
            for i in range(0, len(source) - len(target) + 1):
                if source[i] == target[0]:
                    if target == source[i:i + len(target)]:
                        return i
                    else:
                        y = 1
                else:
                    y = 1
            if y > 0:
                return -1


if __name__ == '__main__':
    S = Solution()
    res = S.strStr("tartarget", "target")
    print(res)
