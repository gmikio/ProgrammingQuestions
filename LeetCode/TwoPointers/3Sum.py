from typing import List
import unittest


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two Pointers!
        solution = []
        aux = []
        nums.sort() # For TwoPointers to work, we must sort the array first
        
        def twoSum(A: List[int], target: int) -> List[int]:
            n = len(A)
            i = 0
            j = n - 1
            
            while i < j:
                if A[i] + A[j] == target:
                    return [A[i], A[j]]
                
                elif A[i] + A[j] < target:
                    i += 1
                
                else:
                    j -= 1
            
            return []
        
        k = 0
        for number in nums:
            newList = nums.copy()
            newList.remove(number)
            solution.append(twoSum(newList, number))
            print ( k, "-> solution till now = ", solution)
            k += 1 
            
        
        return solution



if __name__ == '__main__':
    import unittest
    f = Solution().threeSum
    
    print("caso de teste 1 -------------------------")
    f([-1, 0, 1, 2, -1, -4])
    print("caso de teste 2 -------------------------")
    f([0,1,1])

    # class Test(unittest.TestCase):

    #     def test_1(self):
    #             self.assertEqual(f([-1, 0, 1, 2, -1, -4]),
    #                          [[-1, -1, 2], [-1, 0, 1]])

    #     def test_2(self):
    #         self.assertEqual(f([0,1,1]), [])

    # unittest.main()
