#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = ListNode(0,None)
        l.next = head
        firstP = l
        secondP = l
        for i in range(n + 1):
            firstP = firstP.next
        while(firstP is not None):
            firstP = firstP.next
            secondP = secondP.next
        secondP.next = secondP.next.next
        return l.next