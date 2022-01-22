# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next = ListNode(4)

    solution = Solution()
    print(solution.mergeTwoLists(l1, l2))
