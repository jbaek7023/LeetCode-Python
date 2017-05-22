import unittest
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # store index element
        for i in xrange(len(nums)):
            # 3 1 1
            # index : 2 0 0
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
            # -3 1 -1
        return [ i+1 for i in xrange(len(nums)) if nums[i] > 0 ]

class SolutionUnitTest(unittest.TestCase):
    def testArray(self):
        s = Solution()
        input = [4,3,2,7,8,2,3,1]
        output = [5,6]
        self.assertEqual(s.findDisappearedNumbers(input), output)

if __name__ == '__main__':
    a = 500
    print(a[1])
    unittest.main()


# Note
# xrange and range are the exact same in terms of functionality
# only difference is that xrange returns List
# range returns object
