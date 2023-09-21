from typing import List
import unittest

class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        Example 1:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        
        Example 2:
        Input: n = 1
        Output: ["()"]
        '''
        outputList = []
        
        for i in range (1, n+1):
            stack = []
            
            
            
            
        
        
        
        return List[str]
        
if __name__ == '__main__':
    import unittest
    f = Solution().generateParentheses()

    class Test(unittest.TestCase):
        
        def test_1(self):    
            self.assertEqual(f("parameter"), "valueOfComparison")
         
        def test_2(self):
            self.assertEqual(f("parameter"), "valueOfComparison")

    unittest.main()