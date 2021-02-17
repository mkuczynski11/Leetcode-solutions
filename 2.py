# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/add-two-numbers/
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = 0
        head = ListNode(0,None)
        cur = head
        while (l1 is not None or l2 is not None):
            v1 = 0
            v2 = 0
            if l1 is not None:
                v1 = l1.val
                l1 = l1.next
            if l2 is not None:
                v2 = l2.val
                l2 = l2.next
            
            suma = v1 + v2 + n
            n = suma//10
            cur.next = ListNode(suma%10,None)
            cur = cur.next
        if(n != 0):
            cur.next = ListNode(n, None)
        return head.next