import unittest
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums = [3, 1, 4, 1, 5]
        # k = 2
        seen = set()
        found = set()
        index = 0
        if len(nums) == 0:
            return 0
        if k < 0:
            return 0

        while index < len(nums):
            target = k + nums[index]
            target2 = -k + nums[index]
            if target in seen:
                found.add(
                    (min(target, nums[index]), max(target, nums[index]))
                    )
            if target2 in seen:
                found.add(
                    (min(target2, nums[index]), max(target2, nums[index]))
                    )
            seen.add(nums[index])
            index += 1
        return len(found)
    # User Solution
    def findPairs2(self, nums, k):
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0

class SolutionUnitTest(unittest.TestCase):
    def testArray(self):
        s = Solution()
        input = [3, 1, 4, 1, 5]
        input2 = 2
        output = 2

        self.assertEqual(s.findPairs2(input, input2), output)

# Shift Control B
if __name__ == '__main__':
    unittest.main()


# Note
# xrange and range are the exact same in terms of functionality
# only difference is that xrange returns List
# range returns object
