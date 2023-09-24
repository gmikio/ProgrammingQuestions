from typing import List
import unittest

class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        
        while left <= right:
            middleIndex = (right + left) // 2
            pivot = nums[middleIndex]
            
            if pivot == target:
                return middleIndex
            elif pivot < target:
                left = middleIndex + 1
            else:
                right = middleIndex - 1
        
        return -1

if __name__ == '__main__':
    import unittest
    f = Solution().search

    class Test(unittest.TestCase):
        
        def test_1(self):    
            self.assertEqual(f(nums = [-1,0,3,5,9,12], target = 9), 4)
         
        def test_2(self):
            self.assertEqual(f(nums = [-1,0,3,5,9,12], target = 2), -1)

    unittest.main()
    
    """
    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
    """