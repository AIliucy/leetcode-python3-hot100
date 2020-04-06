"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
from typing import List


# 回溯算法
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if len(digits) == 0:
#             return []
#         phone = {
#             '2': ['a', 'b', 'c'],
#             '3': ['d', 'e', 'f'],
#             '4': ['g', 'h', 'i'],
#             '5': ['j', 'k', 'l'],
#             '6': ['m', 'n', 'o'],
#             '7': ['p', 'q', 'r', 's'],
#             '8': ['t', 'u', 'v'],
#             '9': ['w', 'x', 'y', 'z']
#         }
#         res = []
#
#         def backtrack(combination, nextdigit):
#             if len(nextdigit) == 0:
#                 res.append(combination)
#             else:
#                 for letter in phone[nextdigit[0]]:
#                     backtrack(combination + letter, nextdigit[1:])
#
#         backtrack('', digits)
#         return res


# 队列
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']
        for digit in digits:
            # 此for循环用来控制出队次数，队列中有几个元素，接下来就出队几次
            # 每个元素依次和新遍历出来的phone[digit]结合入队
            for _ in range(len(queue)):
                # 将队首元素出队
                tmp = queue.pop(0)
                # 将出队的元素和phone[digit]的每一个字符结合后入队
                # ord('2') == 50
                for letter in phone[ord(digit) - 50]:
                    queue.append(tmp + letter)
        return queue


def main():
    digits = '234'
    a = Solution()
    print(a.letterCombinations(digits))


if __name__ == '__main__':
    main()
