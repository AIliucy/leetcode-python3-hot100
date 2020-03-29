"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        # 无论字符串长度是奇是偶，插入字符后2×n+1，都转换成奇数字符串
        s_new = '#' + '#'.join(s) + '#'

        # 已遍历的回文子串的最大右边界
        mx = 0
        # mx对应的中心点
        mid = 0

        l = len(s_new)

        # 扩散半径数组，初始值1或者0都可以，只是代表刚开始的时候扩散半径是多少而已
        p = [1] * l

        # 1.找到遍历字符的回文半径 p[i]
        for i in range(l):
            # 1.1 当遍历出来的字符索引在已知最大的回文字符串的覆盖范围内
            if i < mx:
                # p[i]只可能等于或小于对称点的半径，小于的时候即为mx - i
                p[i] = min(mx - i, p[2 * mid - i])

            # 1.2 当遍历出来的字符索引在已知最大的回文字符串的覆盖范围外
            # 以当前遍历字符为中心，在整个字符串的范围内，半径从1逐渐增大循环遍历左右两边字符是否相等
            while i - p[i] >= 0 and i + p[i] < l and s_new[i - p[i]] == s_new[i + p[i]]:
                p[i] += 1

            # 更新mx和mid
            if i + p[i] > mx:
                mx = i + p[i]
                mid = i

        # 回文半径的最大值
        maxr = max(p)
        # 这个最大值在p数组中对应的第一个索引
        ans = p.index(maxr)

        # 因为跳出while循环前多加了1，所以实际上的扩散半径应该减1
        maxr -= 1

        return s_new[ans - maxr:ans + maxr + 1].replace('#', "")


def main():
    s = 'babad'
    a = Solution()
    print(a.longestPalindrome(s))


if __name__ == '__main__':
    main()
