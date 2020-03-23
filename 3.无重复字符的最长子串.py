"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 字符串为空则返回零
        if not s:
            return 0

        length_str = []  # 所有的最长子串
        window = []     # 滑动窗口数组
        max_length = 0  # 最长子串的长度

        # 遍历字符串
        for c in s:

            # 如果字符不在滑动窗口中，则直接扩展窗口
            if c not in window:
                # 使用当前字符扩展窗口
                window.append(c)
            # 如果字符在滑动窗口中
            else:
                # 1 .从窗口中移除重复字符及之前的字符串部分，新字符串即为无重复字符的字符串
                window[:] = window[window.index(c) + 1:]
                # 2 .扩展窗口
                window.append(c)

            # 更新最大长度
            max_length = max(len(window), max_length)
            if max_length <= len(window) and (window not in length_str):
                if ''.join(window) not in length_str:
                    length_str.append(''.join(window))

        all_length_str = [i for i in length_str if len(i) == max_length]
        print(all_length_str)
        return max_length if max_length != 0 else len(s)


def main():
    str_a = "pwwekw"
    a = Solution()
    print(a.lengthOfLongestSubstring(str_a))


if __name__ == '__main__':
    main()
