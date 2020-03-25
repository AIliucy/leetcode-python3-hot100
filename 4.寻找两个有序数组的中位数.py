"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
from typing import List


class Solution:
    # 这题很自然地想到归并排序，再取中间数，但是是nlogn的复杂度，题目要求logn
    # 所以要用二分法来巧妙地进一步降低时间复杂度
    # 思想就是利用总体中位数的性质和左右中位数之间的关系来把所有的数先分成两堆，然后再在两堆的边界返回答案
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        # 让nums2成为更长的那一个数组
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # 如果两个都为空的异常处理
        if n == 0:
            raise ValueError

        # nums1中index在imid左边的都被分到左堆，nums2中jmid左边的都被分到左堆
        imin, imax = 0, m

        # 二分答案
        while (imin <= imax):
            imid = imin + (imax - imin) // 2
            # 左堆最大的只有可能是nums1[imid-1],nums2[jmid-1]
            # 右堆最小只有可能是nums1[imid],nums2[jmid]
            # 让左右堆大致相等需要满足的条件是imid+jmid = m-imid+n-jmid 即 jmid = (m+n-2imid)//2
            # 为什么是大致呢？因为有总数为奇数的情况，这里用向下取整数操作，所以如果是奇数，右堆会多1
            jmid = (m + n - 2 * imid) // 2

            # 前面的判断条件只是为了保证不会index out of range
            if imid > 0 and nums1[imid - 1] > nums2[jmid]:
                # imid太大了，这是里精确查找，不是左闭右开，而是双闭区间，所以直接移动一位
                imax = imid - 1
            elif imid < m and nums2[jmid - 1] > nums1[imid]:
                imin = imid + 1
            # 满足条件
            else:
                # 边界情况处理，都是为了不out of index
                # 依次得到左堆最大和右堆最小
                if imid == m:
                    minright = nums2[jmid]
                elif jmid == n:
                    minright = nums1[imid]
                else:
                    minright = min(nums1[imid], nums2[jmid])

                if imid == 0:
                    maxleft = nums2[jmid - 1]
                elif jmid == 0:
                    maxleft = nums1[imid - 1]
                else:
                    maxleft = max(nums1[imid - 1], nums2[jmid - 1])

                # 前面也提过，因为取中间的时候用的是向下取整，所以如果总数是奇数的话，
                # 应该是右边个数多一些，边界的minright就是中位数
                if 1 == ((m + n) % 2):
                    return minright

                    # 否则我们在两个值中间做个平均
                return (maxleft + minright) / 2


def main():
    nums1 = [1, 3]
    nums2 = [2]
    a = Solution()
    print(a.findMedianSortedArrays(nums1, nums2))


if __name__ == '__main__':
    main()
