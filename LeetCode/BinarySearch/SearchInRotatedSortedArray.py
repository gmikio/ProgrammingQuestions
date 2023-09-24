from typing import List
import unittest

class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums: List[int], target: int, left: int = 0, right:int = None) -> int:
            if right is None:
                right = len(nums) - 1
                
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
        
        def find_pivot(nums):
            left, right = 0, len(nums) - 1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid

            return left  # 'left' is the index of the pivot
        
        isRotated = None
        firstElementIndex = None
        n = len(nums)
        
        if nums[0] > nums[-1]:
            isRotated = True
        else: 
            isRotated = False
        
        if isRotated:
            firstElementIndex = find_pivot(nums)
            if target <= nums[-1]:
                return binarySearch(nums=nums, target=target, left = firstElementIndex, right = n-1)
            else:
                return binarySearch(nums, target, left = 0, right = firstElementIndex - 1)
            
        else:
            return binarySearch(nums, target)
            
        
        return -1


if __name__ == '__main__':
    import unittest
    f = Solution().search

    class Test(unittest.TestCase):
        
        def test_1(self):    
            self.assertEqual(f(nums = [4,5,6,7,0,1,2], target = 0), 4)
         
        def test_2(self):
            self.assertEqual(f(nums = [4,5,6,7,0,1,2], target = 3), -1)
            
        def test_3(self):
            self.assertEqual(f(nums = [1], target = 0), -1)

    unittest.main()
    
"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""