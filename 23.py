#https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        '''
        if lists == []: return None
        head = ListNode(0,None)
        li = head
        pointers = []
        for x in lists:
            if(x is not None):
                pointers.append(x)
        if(not pointers): return None
        while pointers:
            pointer = ListNode(float('inf'),None)
            index = 0
            i = 0
            for x in pointers:
                if(x.val < pointer.val):
                    pointer = x
                    index = i
                i+=1
            li.next = pointer
            li = li.next
            if(pointers[index].next is not None):
                pointers.pop(index)
                pointers.append(pointer.next)
            else:
                pointers.pop(index)
        return head.next
        '''
        length = len(lists)
        inc = 1
        while inc < length:
            for i in range(0, length - inc, inc*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+inc])
            inc *=2
        return lists[0] if length > 0 else None

    def merge2Lists(self, l1, l2):
        head = li = ListNode(0,None)
        while l1 and l2:
            if(l1.val <= l2.val):
                li.next = l1
                l1 = l1.next
            else:
                li.next = l2
                l2 = l2.next
            li = li.next
        if l1:
            li.next = l1
        else:
            li.next = l2
        return head.next
    
a = Solution()
b = ListNode(5,None)
c = ListNode(4,b)
d = ListNode(1,c)

e = ListNode(4,None)
f = ListNode(3, e)
g = ListNode(1, f)

h = ListNode(6, None)
i = ListNode(2, h)

myList = [d,g,i]
print(a.mergeKLists(myList))