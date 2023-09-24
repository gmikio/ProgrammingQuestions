from typing import List
import unittest


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort() # For TwoPointers to work, we must sort the array first
        n = len(nums)
        i = 1
        
        while i < n:
            if i > 1:
                if nums[i-1] == nums[i-2]:
                    i += 1
                    continue
            number = nums[i-1]
            j, k = i, n-1
            target = number * (-1)
            while j < k:
                if nums[j] + nums[k] == target:
                    solution.append([number, nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while k < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                                    
                elif nums[j] + nums[k] < target:
                    j += 1
                
                else:
                    k -= 1
            
            i += 1

        return solution



if __name__ == '__main__':
    import unittest
    f = Solution().threeSum
    
    class Test(unittest.TestCase):

        def test_1(self):
                self.assertEqual(f([-1, 0, 1, 2, -1, -4]),
                             [[-1, -1, 2], [-1, 0, 1]])

        def test_2(self):
            self.assertEqual(f([0,1,1]), [])
            
        def test_3(self):
            self.assertEqual(f([0,0,0]), [[0,0,0]])

    unittest.main()
