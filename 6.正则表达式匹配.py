"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        memo = {}

        # dp(i, j)表示 s[i]前的字符串和p[j]前的字符串匹配，记录结果
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            # 如果j = p_len, 说明p已经匹配完，如果此时i刚好也匹配完则返回true
            # 如果i不等于s_len则一定不能匹配成功，返回false
            if j == p_len:
                return i == s_len
            # x and y x为真，返回y，x为假，返回x
            # 1. 直接匹配，如果p[j]==s[i],或者p[j]=="."，则匹配成功
            pre = i < s_len and p[j] in {s[i], "."}
            # 2. 判断有下一个字符有 × 的情况
            if j <= p_len - 2 and p[j + 1] == "*":
                tmp = dp(i, j + 2) or pre and dp(i + 1, j)
            else:
                tmp = pre and dp(i + 1, j + 1)
            memo[(i, j)] = tmp
            return tmp

        return dp(0, 0)


def main():
    s = 'abbba'
    p = 'ab*a'
    a = Solution()
    print(a.isMatch(s, p))


if __name__ == '__main__':
    main()
