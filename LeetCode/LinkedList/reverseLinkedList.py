from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class LinkedList:
    def __init__(self, node=None):
        if node == None:
            self.head = None
        else:
            self.head = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linkedList = LinkedList(head)
        
        prev = None
        current = linkedList.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        linkedList.head = prev
        
        return linkedList.head
        


if __name__ == '__main__':
    import unittest
    f = Solution().function

    class Test(unittest.TestCase):
        
        def test_1(self):    
            self.assertEqual(f("parameter"), "valueOfComparison")
         
        def test_2(self):
            self.assertEqual(f("parameter"), "valueOfComparison")

    unittest.main()
    
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""