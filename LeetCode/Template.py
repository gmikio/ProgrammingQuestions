import unittest

class Solution(object):
    def function(self,):
        """
        :type
        :rtype: int
        """


if __name__ == '__main__':
    import unittest
    f = Solution().function

    class Test(unittest.TestCase):
        
        def test_1(self):    
            self.assertEqual(f("parameter"), "valueOfComparison")
         
        def test_2(self):
            self.assertEqual(f("parameter"), "valueOfComparison")

    unittest.main()