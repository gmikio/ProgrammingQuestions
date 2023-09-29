from typing import Optional
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = LinkedList(list1)
        list2 = LinkedList(list2)
        
        currentList1 = list1.head
        nextList1 = currentList1.next
        currentList2 = list2.head
        nextList2 = currentList2.val
        
        while currentList1 != None and currentList2 != None:
            if currentList2 < list1.head:
                currentList2.next = list1.head.next
                list1.head = currentList2
                currentList1 = currentList2
                currentList2 = nextList2
                nextList2 = currentList2.next
                
            while currentList2.val > nextList1.val:
                 currentList1 = nextList1
                 nextList1 = currentList1.next
                 
            
                
            
            
        return list1

if __name__ == '__main__':
    import unittest
    f = Solution().function

    class Test(unittest.TestCase):
        
        def test_1(self):    
            self.assertEqual(f("parameter"), "valueOfComparison")
         
        def test_2(self):
            self.assertEqual(f("parameter"), "valueOfComparison")

    unittest.main()