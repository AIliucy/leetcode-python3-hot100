"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
from typing import List
import time


def clock(func):
    def clocked(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("函数{0}的运行时间为： {1}".format(func.__name__, end - start))
        return result
    return clocked


# 顺序遍历
# @clock
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = len(nums)
#         for i, value in enumerate(nums, start=0):
#             diff = target - value
#             j = i + 1
#             while j < length:
#                 if diff == nums[j]:
#                     return [i, j]
#                 else:
#                     j += 1

# 排序算法 左右递推
# @clock
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # 输出的是列表排序后的索引序列列表
#         sorted_id_lst = sorted(range(len(nums)), key=lambda x: nums[x])
#         print(sorted_id_lst)
#         left_point = 0
#         right_point = len(nums) - 1
#         while left_point < right_point:
#             sum = nums[sorted_id_lst[left_point]] + nums[sorted_id_lst[right_point]]
#             if sum == target:
#                 return [sorted_id_lst[left_point], sorted_id_lst[right_point]]
#             elif sum < target:
#                 left_point += 1
#             elif sum > target:
#                 right_point -= 1

# 哈希算法,以空间换事件
@clock
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in hash_map:
                return [hash_map.get(diff), i]
            hash_map[value] = i


def main():
    nums = [2, 11, 15, 7]
    target = 9
    print(Solution().twoSum(nums, target))


if __name__ == "__main__":
    main()
