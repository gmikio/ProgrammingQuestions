import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == ")" and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif char == "]" and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif char == "}" and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)
            
        if len(stack) != 0:
            return False
        
        return True





if __name__ == '__main__':
    # import unittest
    
    Solution().isValid("()[]{}")
    
    f = Solution().isValid

    class Test(unittest.TestCase):
        
        def test_1(self):    
            self.assertEqual(f("parameter"), "valueOfComparison")
         
        def test_2(self):
            self.assertEqual(f("parameter"), "valueOfComparison")

    unittest.main()