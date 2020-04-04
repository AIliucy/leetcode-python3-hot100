"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
import time


def clock(func):
    def clocked(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("函数{0}的运行时间为： {1}".format(func.__name__, end - start))
        return result
    return clocked


# 生成链表节点
# 链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 用来生成和的链表，创造头结点
        head_node = ListNode(0)
        current_node = head_node
        # 进位初始为0
        carry = 0
        while carry or l1 or l2:
            # divmod(进位+l1节点的值(三目运算判断如果l1不为空则取l1节点的值，为空则为0)+l2节点的值)，除以10）
            carry, cur = divmod(carry + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            # head_node.next指向第一个节点，current_node指向当前插入的节点
            current_node.next = ListNode(cur)
            current_node = current_node.next
            # 取下一位，如果当前节点为空，则下一节点也为空
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head_node.next


# 传入一个list，返回一个链表的第一个节点的引用
def generateList(l: list) -> ListNode:
    head_node = ListNode(0)
    current_node = head_node
    for val in l:
        current_node.next = ListNode(val)
        current_node = current_node.next
    return head_node.next


# 传入一个链表，依次输出节点内保存的值
def printList(l: ListNode):
    while l:
        print("%d , " % (l.val), end='')
        l = l.next
    print('')


@clock
def main():
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum_two_number = s.addTwoNumbers(l1, l2)
    printList(sum_two_number)


if __name__ == "__main__":
    main()
