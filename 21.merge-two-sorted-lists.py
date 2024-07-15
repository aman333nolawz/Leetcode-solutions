#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        dummy = out
        while list1 is not None or list2 is not None:
            if list1 is None:
                while list2 is not None:
                    dummy.next = list2
                    dummy = dummy.next
                    list2 = list2.next
                break
            if list2 is None:
                while list1 is not None:
                    dummy.next = list1
                    dummy = dummy.next
                    list1 = list1.next
                break
            
            if list1.val <= list2.val:
                dummy.next = ListNode(list1.val) 
                dummy = dummy.next
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val)
                dummy = dummy.next
                list2 = list2.next
        return out.next
        
# @lc code=end

