"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def node_to_list_result(self, merge_node: Optional[ListNode]):
        result = []
        while merge_node.next is not None:
            result.append(merge_node.val)
            merge_node = merge_node.next
        return result

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val <= list2.val:
            result = list1
            result.next = self.mergeTwoLists(list1.next, list2)
        else:
            result = list2
            result.next = self.mergeTwoLists(list1, list2.next)

        return result


Node1_3 = ListNode(4)
Node1_2 = ListNode(2, Node1_3)
Node1_1 = ListNode(1, Node1_2)

Node2_3 = ListNode(4)
Node2_2 = ListNode(3, Node2_3)
Node2_1 = ListNode(1, Node2_2)

new = Solution()

new_node = new.mergeTwoLists(Node1_1, Node2_1)
print(new.node_to_list_result(new_node))
