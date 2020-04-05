"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        # 如果是空列表，或者nums的长度小于n，直接返回结果[]
        if not nums or n < 3:
            return []
        # 排序
        nums.sort()
        # 遍历nums,遍历一个元素后，移动这个元素后的LR指针，依次求和判断
        for i in range(n):
            # 如果nums[i]>0，则后面任意两个数与其相加都不可能为0，遍历结束，返回结果res
            if nums[i] > 0:
                return res
            # 如果当前元素和上一个元素相等，为了避免出现重复结果，跳过此元素继续遍历
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 如果L，R对应元素和下一个元素相同，则为重复结果
                    # L，R指针一直移动到和当前结果不相等的元素上
                    while L < R and nums[L] == nums[L+1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R-1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                # 如果求和大于零，则右边的偏大，向左移动
                elif nums[i] + nums[L] + nums[R] > 0:
                    R = R - 1
                # 如果求和小于零，则左边的偏小，向右移动
                elif nums[i] + nums[L] + nums[R] < 0:
                    L = L + 1
        return res

def main():
    nums = [-4, -3, -3, -1, 0, 0, 4, 4, 6]
    a = Solution()
    print(a.threeSum(nums))


if __name__ == '__main__':
    main()
